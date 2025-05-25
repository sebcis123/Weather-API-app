# Weather API App
This is a simple weather application written in Python that uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch current weather data for a given city.
## Features
- Get current temperature, humidity, and weather description.
- Supports metric units and Polish language output.
- Includes basic error handling for:
  - Invalid city names
  - Network issues
  - Incorrect API key
  - Unexpected API responses
- Uses `.env` file to store the API key securely.
## Requirements
- Python 3.7+
- An OpenWeatherMap API key (free: https://openweathermap.org/api)
