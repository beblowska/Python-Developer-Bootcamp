import sys
import csv
import json
import requests
from datetime import datetime, timedelta

weather_csv = []

next_day_date = datetime.today() + timedelta(days=1)
next_day_date_user = next_day_date.strftime("%Y-%m-%d")

if len(sys.argv) == 1:
	print("Podaj klucz API: ")
	exit()
else:
	api = sys.argv[1]

if len(sys.argv) == 3:
	date = sys.argv[2]
else:
	date = next_day_date_user

def add_api():
	url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

	querystring = {"q": "warszawa,pl", "lat": "35", "lon": "139", "cnt": "10", "units": "metric or imperial"}

	headers = {
		"X-RapidAPI-Key": api,
		"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	out = response.json()
	with open("from_api.json", "w") as file:
		json.dump(out, file)

def json_file():
	with open("from_api.json") as json_file:
		out = json.load(json_file)
		return out

def forecast_csv():
	with open("forecast.csv", "w", newline=" ") as file:
		csvwriter = csv.writer(file)
		csvwriter.writerows(weather_csv)

def from_dict():
	out = json_file()
	for item in range(len(out['list'])):
		new = out["list"][item]["dt"]
		date_now = str(datetime.fromtimestamp(new).date())
		weather_now = out["list"][item]["weather"][0]["main"]
		weather_csv.append([date_now, weather_now])
		forecast_csv()

def check_csv(weather_csv, date):
	for item in weather_csv:
		if item[0] == date:
			return item[1]

add_api()
from_dict()
check_csv(weather_csv, date)
weather_file = check_csv(weather_csv, date)

if weather_file == "Rain" or weather_file == "Snow":
	print(f"W dniu {date} będzie padać")
if weather_file == "Sun" or weather_file == "Clouds" or weather_file == "Clear":
	print(f"W dniu {date} nie będzie padać")
if weather_file is None:
	add_api()
	check_csv(weather_csv, date)
	if weather_file == "Rain" or weather_file == "Snow":
		print(f"W dniu {date} będzie padać")
	if weather_file == "Sun" or weather_file == "Clouds" or weather_file == "Clear":
		print(f"W dniu {date} nie będzie padać")
		if weather_file is None:
			print("Nie wiem")

