import requests
# import os
from twilio.rest import Client

account_sid = YOUR-ACC-SID
auth_token = YOUR-TOKEN
NUMBER_FROM = NUMBER-FROM
NUMBER_TO = NUMBER-TO
API_KEY = YOR-API-KEY

parametrs = {
    'lat': '60.6',
    'lon': '56.8',
    'exclude': 'current,minutely,daily,alerts',
    'appid': API_KEY
}


response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parametrs)
response.raise_for_status()
data = response.json()
hourly_weather = data['hourly'][:12]
print(hourly_weather)

rain = False
for hour_data in hourly_weather:
    precipitation_code = hour_data['weather'][0]['id']
    if precipitation_code < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Take an umbrella with you!☔️",
        from_=NUMBER_FROM,
        to=NUMBER_TO
    )

    print(message.status)


