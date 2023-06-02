from ambientweather import SensorData
from datetime import datetime


def test_ambientweather_data(ambientweather_data: str):
    sensor_data = SensorData()
    in_sensor, out_sensor = sensor_data.parse(ambientweather_data)

    print(f'Time: {in_sensor.time}\n')
    print('''Indoor\n{delimiter}\nTemperature: {temp}\nHumidity: {humidity}
Absolute preassure: {abs_press}\nRelative preassure: {rel_press}\nBattery status: {battery}\n'''.format(
        delimiter='='*20,
        temp=in_sensor.temp,
        humidity=in_sensor.humidity,
        abs_press=in_sensor.abs_press,
        rel_press=in_sensor.rel_press,
        battery=in_sensor.battery
    ))
    print('''Outdoor\n{delimiter}\nTemperature: {temp}\nHumidity: {humidity}
Battery status: {battery}\n'''.format(
        delimiter='='*20,
        temp=in_sensor.temp,
        humidity=in_sensor.humidity,
        battery=in_sensor.battery
    ))

    assert in_sensor.time == datetime.strptime('2017/10/06 13:55:00', '%Y/%m/%d %H:%M:%S')
    assert in_sensor.temp == 21.9
    assert in_sensor.humidity == 50.0
    assert in_sensor.abs_press == 744.29
    assert in_sensor.rel_press == 728.31
    assert in_sensor.battery == 'Normal'
    assert out_sensor.temp == 10.1
    assert out_sensor.humidity == 71.0
    assert out_sensor.battery == 'Normal'




