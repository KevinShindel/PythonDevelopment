# паралеллизм и будущие объекты
import collections
import os
import sys
import time
import urllib.error
from enum import Enum
from urllib.request import Request, urlopen

HTTPStatus = Enum('Status', 'ok not_found error')
Result = collections.namedtuple('Result',  'status data')

class FetchError(Exception):  # <1>
    def __init__(self, country_code):
        self.country_code = country_code

class BaseParser:
    POP20_CC = (
        'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR AF AL AS DZ AO AQ AG AR AM AW AT AZ BS BH BY BE BO BF BI').split()
    BASE_URL = 'https://www.worldometers.info/img/flags'
    DEST_DIR = 'downloads/'
    MAX_WORKERS = 20
    CPU_WORKERS = os.cpu_count() * 4
    WORKERS = max(MAX_WORKERS, CPU_WORKERS, len(POP20_CC))

    def check_path(self):
        if not os.path.exists(self.DEST_DIR):
            os.mkdir(self.DEST_DIR)

    def download_one(self, cc):
        ''' метод сохранения флага '''
        image = self.get_flag(cc)
        self.show(cc)
        if image:
            self.save_flag(img=image, filename=cc.lower()+'.gif')
        return cc

    def save_flag(self, img, filename):
        path = os.path.join(self.DEST_DIR, filename)
        with open(path, 'wb') as handler:
            handler.write(img)

    def get_flag(self, cc: str):
        url = '{}/{cc}.gif'.format(self.BASE_URL, cc=cc.lower()+'-flag')
        request = Request(url=url)
        request.add_header('User-agent',
                           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36')
        try:
            response = urlopen(request)
        except urllib.error.HTTPError:
            return None
        return response.read()

    @staticmethod
    def show(text):
        print(text, end=' ')
        sys.stdout.flush()

    def download_many(self, cc_list):
        for cc in sorted(cc_list):
            image = self.get_flag(cc)
            self.show(cc)
            if image:
                self.save_flag(img=image, filename=cc.lower()+'.gif')
        return len(cc_list)

    def main(self):
        self.check_path()
        t0 = time.time()
        count = self.download_many(self.POP20_CC)
        files = len(os.listdir(self.DEST_DIR))
        elapsed = time.time() - t0
        msg = '\n {}/{} flags downloaded in {:.2f}s'
        print(msg.format(files, count, elapsed))


if __name__ == '__main__':
    BaseParser().main() # 5.59s
