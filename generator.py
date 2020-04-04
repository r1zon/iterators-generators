import json
import hashlib
from iterators import CountriesUrl

def md5hash(path):
    for i,countries in enumerate(CountriesUrl(path)):
        countries_md5 = hashlib.md5(json.dumps(countries, sort_keys=True).encode('utf-8')).hexdigest()
        for key, value in countries.items():
            yield {f"{key}: {value}": countries_md5}

if __name__ == '__main__':
    for hash in md5hash("countries.json"):
        print(hash)