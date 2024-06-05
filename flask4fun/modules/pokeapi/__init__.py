from flask4fun.modules.pokeapi.models import NamedAPIResourceList
import requests
import json

class PokeApi:
    baseUrl = "https://pokeapi.co/api/v2/"

    def get_items(self, limit = '20', offset = '0'):
        res = requests.get(f"{self.baseUrl}/pokemon", {
            'limit': limit,
            'offset': offset,
        })
        body = res.content.decode()
        return json.loads(body)
    def get_item_by_id(self, id = 0):
        res = requests.get(f"{self.baseUrl}/pokemon/{id}")
        return res.content