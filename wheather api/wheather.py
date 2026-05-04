import requests

city=input("Enter city\n")

base="https://api.openweathermap.org/data/2.5/weather?q="
key="49f074163498b7eac89137f0aeacfe58"

url=f"{base}{city}&appid={key}"
response=requests.get(url)
output=response.json()
print(output["main"]["temp"])
