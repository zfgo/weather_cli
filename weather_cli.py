import json
import geopy 
import requests
import sys

from geopy.geocoders import Nominatim


def main():
    # get input
    print("Enter a location or type 'quit' to exit.")
    prompt = "Location: "
    in_str = input(prompt)

    while in_str != 'quit':
        if in_str == "":
            in_str = "Eugene"
        
        try:
            geolocator = Nominatim(user_agent="HTG")
            loc = geolocator.geocode(in_str)

        except geopy.exc.GeocodeQueryError as err:
            print(f"Error: Couldn't get location for {in_str}.")

        url = f"https://api.weather.gov/points/{loc.latitude},{loc.longitude}"

        try:
            result = requests.get(url)
        
        except requests.ConnectionError:
            print("Error: Couldn't connect to NWS API.")
        except requests.RequestException as err:
            print(f"Error: API request exception: {err}")

        data = result.json()
        # print(data)
        try:
            weather_fc_data = requests.get(data['properties']['forecast'])
            weather_fc_json = weather_fc_data.json()
            current_fc = weather_fc_json['properties']['periods'][0]

            print(f"Current weather for {loc.address}:")
            print(f"Temperature: {current_fc['temperature']} F")
            print(f"Wind speed: {current_fc['windSpeed']}")
            print(f"Wind direction: {current_fc['windDirection']}")

        except KeyError:
            print("Error: Something went wrong.")

        # request input again
        print()
        print("========================")
        print()
        in_str = input(prompt)

    return 


if __name__ == "__main__":
    main()
