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
            raise Exception('Wrong html page. Good one have to have title {}'.format(TITLE))

        inSensor = SensorData()
        time_str = tree.xpath('//input[@name="CurrTime"]/@value')[0]
        inSensor.time = datetime.strptime(time_str, '%H:%M %m/%d/%Y')
        inSensor.temp = float(tree.xpath('//input[@name="inTemp"]/@value')[0])
        inSensor.humidity = float(tree.xpath('//input[@name="inHumi"]/@value')[0])
        inSensor.abs_press = float(tree.xpath('//input[@name="AbsPress"]/@value')[0])
        inSensor.rel_press = float(tree.xpath('//input[@name="RelPress"]/@value')[0])
        inSensor.battery = tree.xpath('//input[@name="inBattSta"]/@value')[0]

        outSensor = SensorData()
        outSensor.time = inSensor.time
        outSensor.temp = float(tree.xpath('//input[@name="outTemp"]/@value')[0])
        outSensor.humidity = float(tree.xpath('//input[@name="outHumi"]/@value')[0])
        outSensor.abs_press = inSensor.abs_press
        outSensor.rel_press = inSensor.rel_press
        outSensor.battery = tree.xpath('//input[@name="outBattSta2"]/@value')[0]

        return inSensor, outSensor

    def get(self, url):
        """
        Load ObserverIP live data page from the URL and parse it

        Returns touple with (sensor1, sensor2 -> SensorData)
        """

        page = requests.get(url).content
        return self.parse(page)
