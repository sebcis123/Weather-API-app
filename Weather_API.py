import requests
import os
from dotenv import load_dotenv

# Wczytaj zmienne z pliku .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pl"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Rzuci wyjątek jeśli nie 2xx

        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        return {
            "city": city,
            "temp": temp,
            "weather": weather,
            "humidity": humidity
        }

    except requests.exceptions.RequestException as e:
        print("Błąd połączenia lub serwera:", e)
        return None

def main():
    city = input("Podaj nazwę miasta: ")
    result = get_weather(city)

    if result:
        print(f"\nPogoda w {result['city']}:")
        print(f"Temperatura: {result['temp']}°C")
        print(f"Opis: {result['weather']}")
        print(f"Wilgotność: {result['humidity']}%")
    else:
        print("Nie udało się pobrać danych.")

if __name__ == "__main__":
    main()
