import requests


def get_weather_forecast():
    cities = ["san_francisco", "london", "svo", "череповец"]
    payload = {
        "3": "", "T": "", "n": "", "?M": "", "lang": "ru"
        }

    for city in cities:
        url = f"https://wttr.in/{city}"
        response = requests.get(url, params=payload)
        response.raise_for_status()
        weather = response.text
        print(weather)


if __name__ == "__main__":
    get_weather_forecast()
