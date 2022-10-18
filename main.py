from time import strftime
from config import open_weather_token
import requests
from pprint import pprint
import datetime


def get_weather(city, open_weather_token):
    
    smile_dict = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F328"
    }
    
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        current_weather = data['main']['temp']
        description  = data['weather'][0]['main']
        if description in smile_dict:
            desc = smile_dict[description]
        else:
            desc = "К сожалению, не могу разобраться с погодой в этом городе((("
        feels_weather = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset'])-datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f' Сегодня {datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")}\n Погода в городе: {city}\n Температура: {current_weather} C {desc}\n Ощущается: {feels_weather} C\n Влажность: {humidity} %\n Скорость ветра достигает: {wind} м\с\n Давление: {pressure} мм.рт.ст.\n Восход: {sunrise_timestamp}\n Закат: {sunset_timestamp}\n Продолжительность дня составляет: {length_of_the_day}\n Отличного Вам дня!!!\n'
              f' Прогноз погоды какого города Вы бы ещё хотели узнать?')


    except Exception as ex:
        print(ex)
        print("Проверьте название города ")



def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
