import json
import re
import time
from threading import Thread

import requests
from tqdm import tqdm

try:
    import Core.DataLoader as DataLoader
    from Core.Item import Item
    from Core.Spider import Spider
except:
    import DataLoader
    from Item import Item
    from Spider import Spider


class Pipeline(object):
    def __init__(self, spider: Spider):
        self._name = spider._name
        self._data = spider._response
        self._items = []
        self.process()

    def save(self):
        with open(f'{self._name}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self._data, indent=4, ensure_ascii=False))

    def cloud(self, info: dict):
        if 'chargeInfoList' in info.keys():
            return
        item = Item()
        item.song = info['name']
        item.singer = "&".join([singer['name'] for singer in info['ar']])
        item.album = info['al']['name']
        item.picURL = info['al']['picUrl']
        item.downloadURL = f"http://music.163.com/song/media/outer/url?id={info['id']}.mp3"
        item.imgData = requests.get(item.picURL).content
        self._items.append(item)

    def kugou(self, info: dict):
        if "hash_offset" in info['trans_param'].keys():
            return
        item = Item()
        data_url = DataLoader.DATABASE['Kugou']['Download']
        headers = {'User-Agent': DataLoader.DATABASE['User-Agent']}
        params = DataLoader.DATABASE['Kugou']['GetMusic']
        params['hash'] = info['FileHash']
        params['album_id'] = info['AlbumID']
        item.song = info['SongName']
        item.singer = "&".join([singer['name']
                                for singer in info['Singers']])
        item.album = info['AlbumName']
        response = requests.get(
            url=data_url, headers=headers, params=params).text
        response = json.loads(re.findall("^.*?(\{.*\}).*?$", response)[0])
        item.picURL = response['data']['img']
        item.downloadURL = response['data']['play_backup_url']
        item.imgData = requests.get(item.picURL).content
        self._items.append(item)

    def kuwo(self, info: dict):
        item = Item()
        data_url = DataLoader.DATABASE['Kuwo']['Download']
        headers = {'User-Agent': DataLoader.DATABASE['User-Agent']}
        params = DataLoader.DATABASE['Kuwo']['GetMusic']
        params['mid'] = info['rid']
        item.song = info['name']
        item.singer = info['artist']
        item.album = info['album']
        item.picURL = str(info['pic']).replace("120", "500")
        item.downloadURL = requests.get(
            url=data_url, headers=headers, params=params).json()['data']['url']
        item.imgData = requests.get(item.picURL).content
        self._items.append(item)

    def process(self):
        func = {
            "Cloud": self.cloud,
            "Kugou": self.kugou,
            "Kuwo": self.kuwo
        }
        src = {
            "Cloud": ("result", "songs"),
            "Kugou": ("data", "lists"),
            "Kuwo": ("data", "list")
        }

        threads = [Thread(target=func[self._name], args=(info, ))
                   for info in self._data[src[self._name][0]][src[self._name][1]]]
        for thread in threads:
            thread.start()
        # for thread in threads:
        for thread in tqdm(threads, unit="item"):
            thread.join()

    @property
    def items(self):
        return self._items


if __name__ == '__main__':
    sp = Spider('Cloud', '傲七爷')
    tm = time.time()
    pipe = Pipeline(sp)
    # pipe.save()
    # for item in pipe._items:
    #     print(item)
    print(f"Time Cost:{time.time() - tm} seconds!")
