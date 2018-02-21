"""今日の天気を取得する

参照:
http://weather.livedoor.com/weather_hacks/webservice
"""

import json
import urllib.request


def get_weather(city):
    with urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=' + city) as response:
        d = json.loads(response.read().decode('utf-8'))
    return d['forecasts'][0]['telop']


if __name__ == '__main__':
    # 東京
    print(get_weather('130010'))
