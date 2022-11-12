import requests
import variables as v
from urllib.parse import quote

class Mysession:
    def __init__(self) -> None:
        self.s = requests.Session() # Session Objects get created
        self.s.headers = {
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://googolplex.live/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Linux"',
        }

    def login(self, username, password):
        json_data = {
            'email': username,
            'password': password,
        }
        return self.s.post(v.LOGIN_API, json=json_data)
    
    def update_parameter(self, dict_data):
        self.s.headers.update(dict_data)

    def remove_parameter(self, parameter):
        self.s.headers.pop(parameter, None)

    def getMethod(self, get_url):
        return self.s.get(get_url)

    def searchby_keyword(self, search_url, keyword):
        search_url_with_keyword = f'{search_url}/{quote(keyword)}'
        return self.s.get(search_url_with_keyword)
