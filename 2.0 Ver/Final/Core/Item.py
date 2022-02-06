class Item(object):
    
    _song:str
    _singer:str
    _album:str
    _picURL:str
    _downloadURL:str
    _imgData:bytes
    
    def __init__(self):
        pass

    @property
    def song(self):
        return self._song

    @song.setter
    def song(self, name: str):
        self._song = name

    @property
    def singer(self):
        return self._singer

    @singer.setter
    def singer(self, name: str):
        self._singer = name

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, name: str):
        self._album = name

    @property
    def picURL(self):
        return self._picURL

    @picURL.setter
    def picURL(self, name: str):
        self._picURL = name

    @property
    def downloadURL(self):
        return self._downloadURL

    @downloadURL.setter
    def downloadURL(self, name: str):
        self._downloadURL = name
        
    @property
    def imgData(self):
        return self._imgData

    @imgData.setter
    def imgData(self, content:bytes):
        self._imgData = content

    def __str__(self):
        return f'''
        song:{self.song},
        singer:{self.singer},
        album:{self.album},
        picURL:{self.picURL},
        downloadURL:{self.downloadURL}
      '''


if __name__ == '__main__':
    item = Item()
    print(item)
