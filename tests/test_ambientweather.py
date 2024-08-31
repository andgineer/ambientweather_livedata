from ambientweather import AmbientWeather
from datetime import datetime


def test_ambientweather_data(ambientweather_data: str):
    in_sensor, out_sensor = AmbientWeather.parse(ambientweather_data.encode('utf-8'))

    assert in_sensor.time == datetime.strptime('2017/10/06 13:55:00', '%Y/%m/%d %H:%M:%S')
    assert in_sensor.temp == 21.9
    assert in_sensor.humidity == 50.0
    assert in_sensor.abs_press == 744.29
    assert in_sensor.rel_press == 728.31
    assert in_sensor.battery == 'Normal'
    assert out_sensor.temp == 10.1
    assert out_sensor.humidity == 71.0
    assert out_sensor.battery == 'Normal'