import datetime

import errors
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from requests_html import HTMLSession


class WebServerValidator(object):
    def __init__(self, server_ip, schema='http'):
        self.session = HTMLSession()
        self._server_ip = server_ip
        self.server_address = f'{schema}://{server_ip}'

    def is_server_ok(self):
        status_code = requests.get(self.server_address).status_code
        if status_code == 200:
            return True
        else:
            raise errors.WebServerBadResponseError(server=self._server_ip, status_code=status_code)

    def is_content_valid(self):
        response = self.session.get(self.server_address)

        response.html.render()
        soup = BeautifulSoup(response.html.html, "lxml")
        divs = soup.find_all('div')
        content = divs[0].contents[0]
        current_date = parse(content)
        now = datetime.datetime.utcnow()
        if abs((now - current_date.replace(tzinfo=None)).seconds) < 60:
            return True
        else:
            raise errors.WebServerBadContentError(server=self._server_ip, content=content)
