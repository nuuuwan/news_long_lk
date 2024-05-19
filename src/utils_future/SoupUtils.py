import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from utils import Log

log = Log('SoupUtils')


class SoupUtils:
    @staticmethod
    def get_soup_static(url: str):
        log.debug(f'{url=}')
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    @staticmethod
    def get_soup_dynamic(url: str):
        options = Options()
        options.add_argument('--headless')
        driver = Firefox(options=options)
        log.debug(f'{url=}')
        driver.get(url)
        html = driver.page_source

        driver.quit()
        return BeautifulSoup(html, 'html.parser')

    @staticmethod
    def get_soup(url: str, is_dynamic: bool):
        if is_dynamic:
            return SoupUtils.get_soup_dynamic(url)
        return SoupUtils.get_soup_static(url)
