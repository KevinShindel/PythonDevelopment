# BEGIN FLAGS2_ASYNCIO_TOP
import argparse
import asyncio
import collections
import os
import string
import sys
import time
from collections import namedtuple
from enum import Enum

import aiohttp
import tqdm
from aiohttp import web

from Chapter_17.base import FetchError

DEFAULT_CONCUR_REQ = 10
MAX_CONCUR_REQ = 1000


Result = namedtuple('Result', 'status data')

HTTPStatus = Enum('Status', 'ok not_found error')

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()


DEST_DIR = 'downloads/'
COUNTRY_CODES_FILE = 'country_codes.txt'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def initial_report(cc_list, actual_req):
    if len(cc_list) <= 10:
        cc_msg = ', '.join(cc_list)
    else:
        cc_msg = 'from {} to {}'.format(cc_list[0], cc_list[-1])
    msg = 'Searching for {} flag{}: {}'
    plural = 's' if len(cc_list) != 1 else ''
    print(msg.format(len(cc_list), plural, cc_msg))
    plural = 's' if actual_req != 1 else ''
    msg = '{} concurrent connection{} will be used.'
    print(msg.format(actual_req, plural))


def final_report(cc_list, counter, start_time):
    elapsed = time.time() - start_time
    print('-' * 20)
    msg = '{} flag{} downloaded.'
    plural = 's' if counter[HTTPStatus.ok] != 1 else ''
    print(msg.format(counter[HTTPStatus.ok], plural))
    if counter[HTTPStatus.not_found]:
        print(counter[HTTPStatus.not_found], 'not found.')
    if counter[HTTPStatus.error]:
        plural = 's' if counter[HTTPStatus.error] != 1 else ''
        print('{} error{}.'.format(counter[HTTPStatus.error], plural))
    print('Elapsed time: {:.2f}s'.format(elapsed))


def expand_cc_args(every_cc, all_cc, cc_args, limit):
    codes = set()
    A_Z = string.ascii_uppercase
    if every_cc:
        codes.update(a+b for a in A_Z for b in A_Z)
    elif all_cc:
        with open(COUNTRY_CODES_FILE) as fp:
            text = fp.read()
        codes.update(text.split())
    else:
        for cc in (c.upper() for c in cc_args):
            if len(cc) == 1 and cc in A_Z:
                codes.update(cc+c for c in A_Z)
            elif len(cc) == 2 and all(c in A_Z for c in cc):
                codes.add(cc)
            else:
                msg = 'each CC argument must be A to Z or AA to ZZ.'
                raise ValueError('*** Usage error: '+msg)
    return sorted(codes)[:limit]


def process_args(default_concur_req):
    parser = argparse.ArgumentParser(
        description='Download flags for country codes. '
                    'Default: top 20 countries by population.')
    parser.add_argument('cc', metavar='CC', nargs='*',
                        help='country code or 1st letter (eg. B for BA...BZ)')
    parser.add_argument('-a', '--all', action='store_true',
                        help='get all available flags (AD to ZW)')
    parser.add_argument('-e', '--every', action='store_true',
                        help='get flags for every possible code (AA...ZZ)')
    parser.add_argument('-l', '--limit', metavar='N', type=int,
                        help='limit to N first codes', default=sys.maxsize)
    parser.add_argument('-m', '--max_req', metavar='CONCURRENT', type=int,
                        default=default_concur_req,
                        help='maximum concurrent requests (default={})'
                        .format(default_concur_req))
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='output detailed progress info')
    args = parser.parse_args()
    if args.max_req < 1:
        print('*** Usage error: --max_req CONCURRENT must be >= 1')
        parser.print_usage()
        sys.exit(1)
    if args.limit < 1:
        print('*** Usage error: --limit N must be >= 1')
        parser.print_usage()
        sys.exit(1)
    try:
        cc_list = expand_cc_args(args.every, args.all, args.cc, args.limit)
    except ValueError as exc:
        print(exc.args[0])
        parser.print_usage()
        sys.exit(1)

    if not cc_list:
        cc_list = sorted(POP20_CC)
    return args, cc_list


def main(download_many, default_concur_req, max_concur_req):
    args, cc_list = process_args(default_concur_req)
    actual_req = min(args.max_req, max_concur_req, len(cc_list))
    initial_report(cc_list, actual_req)
    base_url = 'https://www.worldometers.info/img/flags'
    t0 = time.time()
    counter = download_many(cc_list, base_url, args.verbose, actual_req)
    assert sum(counter.values()) == len(cc_list), \
        'some downloads are unaccounted for'
    final_report(cc_list, counter, t0)


async def get_flag(base_url, cc): # <2>
    url = '{}/{cc}.gif'.format(base_url, cc=cc.lower() + '-flag')
    async with aiohttp.request('GET', url) as response:
        if response.status == 200:
            image = await response.read()
            return image
        elif response.status == 404:
            raise web.HTTPNotFound()
        else:
            raise aiohttp.http.HttpProcessingError(
                code=response.status, message=response.reason,
                headers=response.headers)


async def download_one(cc, base_url, semaphore):
    try:
        await semaphore.acquire()
        image = await get_flag(base_url, cc)
        semaphore.release()
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop = asyncio.get_event_loop()  # получаем ссылку на обьект цикла обработки событий
        loop.run_in_executor(None,  # первый аргумент экземляр исполнителя
                save_flag, image, cc.lower() + '.gif')  # остальные аргументы передаются в функцию
        status = HTTPStatus.ok

    return Result(status, cc)


async def downloader_coro(cc_list, base_url, verbose, concur_req):  # <1>
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)  # <2>
    to_do = [download_one(cc, base_url, semaphore) for cc in sorted(cc_list)]  # <3>

    to_do_iter = asyncio.as_completed(to_do)  # <4>
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))  # <5>
    for future in to_do_iter:  # <6>
        try:
            res = await future  # <7>
        except FetchError as exc:  # <8>
            country_code = exc.country_code  # <9>
            try:
                error_msg = exc.__cause__.args[0]  # <10>
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__  # <11>
            msg = '*** Error for {}: {}'
            print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status

        counter[status] += 1  # <12>

    return counter  # <13>


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)  # <14>
    loop.close()  # <15>

    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
