# Ambient Weather IPObserver sensor's data extractor

Python3 library that search for sensor's temperature and humidity data on IPObserver page `LiveData`.
Uses xpath and [lxml](http://lxml.de/).

Example:

        import ambientweather_livedata

        inSensor, outSensor = ambientweather_livedata.get('http://10.0.0.176/LiveData.html')
        print('Time: {}\n'.format(inSensor.time))
        print('''Indoor\n{delimiter}\nTemperature: {temp}\nHumidity: {humidity}
    Absolute preassure: {abs_press}\nRelative preassure: {rel_press}\nBattery status: {battery}\n'''.format(
            delimiter='='*20,
            temp=inSensor.temp,
            humidity=inSensor.humidity,
            abs_press=inSensor.abs_press,
            rel_press=inSensor.rel_press,
            battery=inSensor.battery
        ))
        print('''Outdoor\n{delimiter}\nTemperature: {temp}\nHumidity: {humidity}
    Battery status: {battery}\n'''.format(
            delimiter='='*20,
            temp=inSensor.temp,
            humidity=inSensor.humidity,
            battery=inSensor.battery
        ))


