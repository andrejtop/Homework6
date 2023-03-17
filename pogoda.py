from pyowm import OWM


def pogoda():
    City = input('Какой город Вас интересует: ')

    owm = OWM('***************************')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(City)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    print('В городе ' + City + ' сейчас ' + str(temperature))
    print('А также ' + w.detailed_status)


if __name__ == '__main__':
    pogoda()
