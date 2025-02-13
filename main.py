import requests


def get_weather_forecast():
    cities = ["san_francisco", "london", "svo", "череповец"]
    params = {
        "3": "", "T": "", "n": "", "M": "", "lang": "ru"
    }

    for city in cities:
        url = f"https://wttr.in/{city}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather = response.text
        print(weather)


if __name__ == "__main__":
    get_weather_forecast()
