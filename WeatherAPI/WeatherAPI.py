import os, requests, json
from dotenv import load_dotenv

def main():
  load_dotenv()

  BASE_URL_WEATHER = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

  location = os.getenv('WEATHER_LOCATION_API')
  date1 = os.getenv('WEATHER_DATE1')
  api_key = os.getenv('WEATHER_API_KEY')

  url = f"{BASE_URL_WEATHER}{location}/{date1}?unitGroup=metric&key={api_key}&contentType=json&elements=tempmax,tempmin,temp"

  try:
    response = requests.get(url)
    response.raise_for_status()
    WeatherData = response.json()
#!!! Доработать функцию вывода
    with open('./data.json', 'w') as file:
      json.dump(WeatherData, file,  sort_keys=True, indent=4)

  except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {str(http_err)}")
        raise
  except Exception as err:
        print(f"Other error occurred: {str(err)}")
        raise
