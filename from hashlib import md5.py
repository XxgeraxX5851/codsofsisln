import json
from hashlib import md5
from requests import get 
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = 'aa878a55dd11ce5696f3d78f679399b5'
    priv_key = '2cbe46c97d42c699bf1d925aa2a567dc4a9aa381'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params

    def get_heroes(self):
        params = {'ts':self.timestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters',params=params)

        data=results.json()
        print(data)

rest=RestMarvel()
rest.get_heroes() 

