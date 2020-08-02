# Comand-line interface application
import requests

other = input("Podaj walutę: ")
response = requests.get("http://data.fixer.io/api/latest",
                        params= {'access_key':'032053b70cf616de08638aeaeb1cfd1d',
                                'symbols': other.upper()}
                        )
if response.status_code != 200:
    raise Exception("Error: Api request unsuccessful")

data = response.json()
if data.get('rates'):
    res = data.get('rates').get(other.upper())
    print(f"1 EURO to {res} {other.upper()}")
else:
    print("Nie rozpoznano waluty.")