#! /usr/bin/env python3
#
# Requires requests
#

import json
import requests
import sys

WEATHER_URL = "https://example.net/api.php?degree=C&location="


def getWeather(city):
    url = WEATHER_URL + city
    response = requests.get(url)
    return response.text


def main():
    # This fails as the site does actually not exist
    data = getWeather(sys.argv[1])

    print('JSON result retrieved:')
    print(data)
    print()

    weather = json.loads(data)
    cur = weather['CurrentData']
    print(f'Vejret i {weather["LocationName"]}:')
    print(f'{cur["skyText"]} og {cur["temperature"]}')


if __name__ == '__main__':
    main()
