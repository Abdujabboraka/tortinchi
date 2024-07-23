from pprint import pprint
from requests import get


class Dummyjson:
    def __init__(self):
        self.url = "https://dummyjson.com/users"

    def request(self):
       file = get(self.url).json()
       return file["users"]

ded = Dummyjson()

pprint(ded.request())