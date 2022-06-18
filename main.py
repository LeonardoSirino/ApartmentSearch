import re
from abc import abstractmethod
from pprint import pprint

from bs4 import BeautifulSoup as bs
from selenium.webdriver import Chrome

url = r'https://www.zapimoveis.com.br/imovel/aluguel-apartamento-1-quarto-paraiso-zona-sul-sao-paulo-sp-57m2-id-2561479368/'


class Extractor:
    def __init__(self, url: str, driver: Chrome) -> None:
        self._url = url
        self._driver = driver

    @abstractmethod
    def get_links_on_page(self):
        raise NotImplementedError


driver = Chrome()
driver.get(url)
soup = bs(driver.page_source, features='html.parser')

pattern = r'^\/aluguel\/'
links = soup.find_all('a')
links = filter(lambda link: re.search(pattern, link['href']), links)
links = map(lambda link: link['href'], links)
pprint(list(links))
