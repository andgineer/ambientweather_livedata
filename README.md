[![Build Status](https://github.com/andgineer/ambientweather_livedata/workflows/ci/badge.svg)](https://github.com/andgineer/ambientweather_livedata/actions)
# Extract data from Ambient Weather stations

Python3 library that extracts information from [Ambient Weather stations](https://www.ambientweather.com/).

It collects sensor's data (temperature and humidity) from the [IPObserver](https://www.ambientweather.com/amobserverip.html) `LiveData` tab of the IPObserver web-page.
You can get this page from the IPObserver - just open the IPObserver IP adddress in your web-brawser to see it.

The library uses xpath and [lxml](http://lxml.de/).

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


