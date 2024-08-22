import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather forecast for {city} is as follows:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather Conditions: {data['weather'][0]['description']}")
            print(f"Relative Humidity: {data['main']['humidity']}%")
            print(f"The speed of wind is: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    api_key = 'afb2de52b3afe8fdc5e3a3c5bb539a21'  
    city = input("Enter the city name here: ")

    get_weather(api_key, city)

if __name__ == "__main__":
    main()
