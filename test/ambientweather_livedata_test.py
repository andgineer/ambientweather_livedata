from ambientweather import SensorData
from _datetime import datetime


def test():
    with open('LiveData.html', 'r') as f:
        page = f.read()

    sensor_data = SensorData()
    inSensor, outSensor = sensor_data.parse(page)

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

    assert inSensor.time == datetime.strptime('2017/10/06 13:55:00', '%Y/%m/%d %H:%M:%S')
    assert inSensor.temp == 21.9
    assert inSensor.humidity == 50.0
    assert inSensor.abs_press == 744.29
    assert inSensor.rel_press == 728.31
    assert inSensor.battery == 'Normal'
    assert outSensor.temp == 10.1
    assert outSensor.humidity == 71.0
    assert outSensor.battery == 'Normal'




