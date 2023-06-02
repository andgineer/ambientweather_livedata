import requests
from lxml import html
from datetime import datetime


TITLE = 'LiveData'  # HTML live data page title


class SensorData(object):
    """
    time
    temp
    humidity
    abs_press
    rel_press
    battery ('Normal')
    """

    def parse(self, live_data_html):
        """
        Extract sensor's data from html (LiveData.html from your ObserverIP)
        Returns touple with (sensor1, sensor2 -> SensorData)
        """

        tree = html.fromstring(live_data_html)
        title = tree.xpath('//title/text()')
        if title[0] != TITLE:
            raise ValueError(f'Wrong html page. Good one have to have title {TITLE}')

        in_sensor = SensorData()
        time_str = tree.xpath('//input[@name="CurrTime"]/@value')[0]
        in_sensor.time = datetime.strptime(time_str, '%H:%M %m/%d/%Y')
        in_sensor.temp = float(tree.xpath('//input[@name="inTemp"]/@value')[0])
        in_sensor.humidity = float(tree.xpath('//input[@name="inHumi"]/@value')[0])
        in_sensor.abs_press = float(tree.xpath('//input[@name="AbsPress"]/@value')[0])
        in_sensor.rel_press = float(tree.xpath('//input[@name="RelPress"]/@value')[0])
        in_sensor.battery = tree.xpath('//input[@name="inBattSta"]/@value')[0]

        out_sensor = SensorData()
        out_sensor.time = in_sensor.time
        out_sensor.temp = float(tree.xpath('//input[@name="outTemp"]/@value')[0])
        out_sensor.humidity = float(tree.xpath('//input[@name="outHumi"]/@value')[0])
        out_sensor.abs_press = in_sensor.abs_press
        out_sensor.rel_press = in_sensor.rel_press
        out_sensor.battery = tree.xpath('//input[@name="outBattSta2"]/@value')[0]

        return in_sensor, out_sensor

    def get(self, url):
        """
        Load ObserverIP live data page from the URL and parse it

        Returns touple with (sensor1, sensor2 -> SensorData)
        """

        page = requests.get(url).content
        return self.parse(page)
