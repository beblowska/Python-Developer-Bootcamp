import sys
import json
import csv
from datetime import datetime, timedelta
import requests

weather_csv = []
next_day_date = datetime.today() + timedelta(days=1)
date = datetime.strptime(sys.argv[2], "%Y-%m-%d").date() if len(sys.argv) == 3\
    else next_day_date.date()
city = "Warszawa"

class WeatherForcast:
    def __init__(self, api_key):
        self.api_key = api_key
        self.cached = {}
        self.date_cached = []

    def __getitem__(self, item):
        return self.cached.get(item, "nie wiem")

    def __iter__(self):
        return iter(self.cached)

    def items(self):
        for item in self.date_cached:
            yield item[0], item[1]

    def add_api(self):
        url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

        querystring = {"q": f"{city},pl", "lat": "35", "lon": "139", "cnt": "10", "units": "metric"}

        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        out = response.json()
        with open("form_api.json", "w") as file:
            json.dump(out, file)

    def json_file(self):
        with open("from_api.json") as json_file:
            out = json.load(json_file)
            return out

    def read_cache(self, date):
        with open('forecast.csv', newline="") as fp:
            reader = csv.reader(fp)
            for line in reader:
                date_from_str = datetime.strptime(line[0], "%Y-%m-%d").date()
                self.cached[date_from_str] = line[1]
                if date_from_str == date:
                    if line[1] in ['Snow', 'Rain']:
                        return "będzie padać"
                    return "nie będzie padać"

    def forecast_csv(self):
        with open('forecast.csv', 'w', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(self.date_cached)
        return weather_csv

    def from_dict(self):
        out = self.json_file()
        for item in range(len(out['list'])):
            new = out['list'][item]['dt']
            date_now = str(datetime.fromtimestamp(new).date())
            weather_now = out['list'][item]['weather'][0]['main']
            weather_csv.append([date_now, weather_now])
            self.date_cached.append([date_now, weather_now])
            date_from_str = datetime.strptime(date_now, "%Y - %m - %d").date()
            self.cached[date_from_str] = weather_now
            self.forecast_csv()

    def check_csv(self, date):
        for item in self.cached:
            if item[0] == date:
                return item[1]

wf = WeatherForcast(api_key = sys.argv[1])
if date in wf.cached:
    wf.from_dict()
    wf.__getitem__(date)
else:
    if date not in wf.cached:
        wf.add_api()
        wf.from_dict()
        wf.__getitem__(date)
        wf.read_cache(date)

print("1. wf[date] da odpowiedź na temat pogody dla podanej daty: ")
print(f"Podana data: {date}")
print(wf[date])
print(wf.read_cache(date))
print("2. wf.items() zwróci generator tupli w formacie (data, pogoda) "
      "dla już zcache’owanych rezultatów przy wywołaniu")
for data, pogoda in wf.items():
    print(data, pogoda)
print("3. wf to iterator zwracający wszystkie daty, "
      "dla których znana jest pogoda")
for data in wf:
    print(data)




