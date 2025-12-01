"""Extract data from Ambient Weather stations."""

from dataclasses import dataclass
from datetime import datetime

import requests
from lxml import html  # pylint: disable=import-error
from lxml.html import HtmlElement

TITLE: str = "LiveData"  # HTML live data page title
TIMEOUT: int = 5  # seconds


@dataclass
class BaseSensorData:
    """Base class for sensor data"""

    time: datetime | None = None
    temp: float | None = None
    humidity: float | None = None
    battery: str | None = None


@dataclass
class IndoorSensorData(BaseSensorData):
    """Indoor sensor data"""

    abs_press: float | None = None
    rel_press: float | None = None


@dataclass
class OutdoorSensorData(BaseSensorData):
    """Outdoor sensor data"""


class AmbientWeather:
    """Class to handle Ambient Weather data retrieval and parsing"""

    @staticmethod
    def parse(live_data_html: bytes) -> tuple[IndoorSensorData, OutdoorSensorData]:
        """Extract sensor data from html (LiveData.html from your ObserverIP)."""
        tree: HtmlElement = html.fromstring(live_data_html)
        title: list[str] = tree.xpath("//title/text()")
        if title[0] != TITLE:
            raise ValueError(f"Wrong html page. Good one have to have title {TITLE}")

        in_sensor: IndoorSensorData = IndoorSensorData()
        out_sensor: OutdoorSensorData = OutdoorSensorData()

        time_str: str = tree.xpath('//input[@name="CurrTime"]/@value')[0]
        in_sensor.time = out_sensor.time = datetime.strptime(time_str, "%H:%M %m/%d/%Y")

        in_sensor.temp = float(tree.xpath('//input[@name="inTemp"]/@value')[0])
        in_sensor.humidity = float(tree.xpath('//input[@name="inHumi"]/@value')[0])
        in_sensor.abs_press = float(tree.xpath('//input[@name="AbsPress"]/@value')[0])
        in_sensor.rel_press = float(tree.xpath('//input[@name="RelPress"]/@value')[0])
        in_sensor.battery = tree.xpath('//input[@name="inBattSta"]/@value')[0]

        out_sensor.temp = float(tree.xpath('//input[@name="outTemp"]/@value')[0])
        out_sensor.humidity = float(tree.xpath('//input[@name="outHumi"]/@value')[0])
        out_sensor.battery = tree.xpath('//input[@name="outBattSta2"]/@value')[0]

        return in_sensor, out_sensor

    @staticmethod
    def get(url: str) -> tuple[IndoorSensorData, OutdoorSensorData]:
        """
        Load ObserverIP live data page from the URL and parse it
        """
        response: requests.Response = requests.get(url, timeout=TIMEOUT)
        page: bytes = response.content
        return AmbientWeather.parse(page)
