import json

countries_dict = {}
url = 'https://en.wikipedia.org/wiki/'

class CountriesUrl():
    def __init__(self, path):
        self.file = open(path, encoding="utf-8")
        self.json_data = json.load(self.file)
        self.len = len(self.json_data)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.len - 1:
            raise StopIteration
        country_name = self.json_data[self.i]['name']['common'].replace(" ", "_")
        self.i += 1
        return {self.json_data[self.i]['name']['common']: url + country_name}

if __name__ == '__main__':
    for countries in CountriesUrl("countries.json"):
        countries_dict.update(countries)
    with open("countries_url.json", "w", encoding="utf-8") as f:
        json.dump(countries_dict, f, ensure_ascii=False, indent=2)
    print('Файл успешно записан')
