import base64
import hashlib
import json
import re

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

try:
    import Core.DataLoader as DataLoader
except:
    import DataLoader


class Spider(object):
    def __init__(self, name: str, keyword: str):
        self._ua = DataLoader.DATABASE['User-Agent']
        self._headers = {
            'User-Agent': self._ua
        }
        if name in DataLoader.DATABASE.keys():
            self._name = name
        else:
            self._name = None
            raise Exception("Undefined Name!")
        self._params = DataLoader.DATABASE[self._name]['Scrapy']
        self._keyword = keyword
        self._response = {}
        self._url = DataLoader.DATABASE[self._name]['Src']
        self.scrapy()

    def cloud(self):
        self._params['s'] = self._keyword
        iv = '0102030405060708'.encode('utf-8')
        key1 = '0CoJUm6Qyw8W8jud'.encode('utf-8')
        key2 = 'azbpr6SvijnCVi86'.encode('utf-8')
        target1 = str(self._params)
        cryptor1 = AES.new(key1, AES.MODE_CBC, iv)
        target1 = pad(target1.encode('utf-8'), AES.block_size)
        target2 = base64.b64encode(cryptor1.encrypt(target1)).decode('utf-8')
        cryptor2 = AES.new(key2, AES.MODE_CBC, iv)
        target2 = pad(target2.encode('utf-8'), AES.block_size)
        self._params = {}
        self._params['params'] = base64.b64encode(
            cryptor2.encrypt(target2)).decode('utf-8')
        self._params['encSecKey'] = '476c5abe84f2044d3d8bc7624a13bc1f68483b88f7ea29c5969ac' +\
            '617986314a682968784883c8d710d81dc68c748354afbb65c0442a78f91b72af3a3e523297ba0ac0' +\
            '0a8691a7e54598001ae7db4d0e730cd4cb359d620958cfc7653fe95f3f5b2d1bb35c66f3fd074cb9' +\
            '9916fd91915a0368caa65028d0e787ca24c1aaf508a'

    def kugou(self):
        temp_list = []
        self._params['keyword'] = self._keyword
        for key, value in self._params.items():
            if key != 'signature' and key != 'fix':
                temp_list.append(str(key) + "=" + str(value))
        temp_list.append(self._params['fix'])
        temp_list.insert(0, self._params['fix'])
        temp_str = "".join(temp_list)
        hs = hashlib.md5()
        hs.update(temp_str.encode(encoding='utf-8'))
        self._params['signature'] = hs.hexdigest().upper()
        del self._params['fix']

    def kuwo(self):
        self._keyword = self._keyword.encode('utf-8')
        self._headers['Cookie'] = DataLoader.DATABASE[self._name]['Header']['Cookie']
        self._headers['csrf'] = DataLoader.DATABASE[self._name]['Header']['csrf']
        self._headers['Referer'] = f'http://www.kuwo.cn/search/list?key={self._keyword}'
        self._params['key'] = self._keyword

    def scrapy(self):
        func = {
            "Cloud": self.cloud,
            "Kugou": self.kugou,
            "Kuwo": self.kuwo
        }
        eval("func[self._name]()")
        if self._name == 'Cloud':
            self._response = requests.post(
                url=self._url, headers=self._headers, data=self._params).text
        else:
            self._response = requests.get(
                url=self._url, headers=self._headers, params=self._params).text
        self._response = self._response.replace("<\/em>", "").replace("<em>", "")
        self._response = json.loads(re.findall("^.*?(\{.*\}).*?$", self._response)[0])

    @property
    def response(self):
        return self._response


if __name__ == '__main__':
    sp = Spider('Cloud', '傲七爷')
    print(sp.response)
