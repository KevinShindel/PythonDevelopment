# выполнение нескольких запроссов для каждой операции
import asyncio

import aiohttp
from aiohttp import web

from Chapter_17.base import HTTPStatus, FetchError, Result


@asyncio.coroutine
def http_get(url):
    response = yield from aiohttp.request('GET', url)
    if response.status == 200:
        ctype = response.headers.get('Content-type', '').lower()
        if 'json' in ctype or url.endswith('json'): # определяем тип содержимого
            data = yield from response.json() # вызываем метод json
        else:
            data = yield from response.read() # вызываем метод read
        return data
    elif response.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.http.HttpProcessingError(
            code=response.status, message=response.reason,
            headers=response.headers
        )


@asyncio.coroutine
def get_country(base_url, cc):
    url = '{}/{cc}.json'.format(base_url, cc=cc.lower() + '-flag')
    metadata = yield from http_get(url)
    return metadata['country'] # записывает country в словарь из reponse


@asyncio.coroutine
def get_flag(base_url, cc):
    url = '{}/{cc}.gif'.format(base_url, cc=cc.lower() + '-flag')
    return (yield from http_get(url)) # скобки необходимы потому что python видит подряд три слова


@asyncio.coroutine
def download_one(cc, base_url, semaphore):
    try:
        with (yield from semaphore):
            image = yield from get_flag(base_url, cc)
        with (yield from semaphore):
            country = yield from get_country(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as Err:
        raise FetchError(cc) from Err
    else:
        country = country.replace(' ', '_')
        filename = '{}-{}.gif'.format(country, cc)
        loop = asyncio.get_event_loop()
        args = (image, filename)
        loop.run_in_executor(executor=None, func=save_flag, *args)
        status = HTTPStatus.ok
        msg = 'ok'

    return Result(status, cc)




