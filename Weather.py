from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()

config_dict['language'] = 'ru'

owm = OWM('68b9a097a845cb77fafedc969f39aa85',)

mgr = owm.weather_manager()

place = input("В каком городе/стране?: ")

observation = mgr.weather_at_place(place)

w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В горде " + (place) + " сейчас " + w.detailed_status)

print( "Температура сейчас в районе " + str(temp))

if temp < 10:

	print ("Сейчас нереально холодно, одевайся как капуста!")

elif temp  < 20:

	print("Сейчас холодно, оденься потеплее")

elif temp  < 25:

	print("Температура норм, надевай что угодно")

else:

	print("На улице жара! Ну удачи тебе")