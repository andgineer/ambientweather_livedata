"""Extract data from Ambient Weather stations."""

from typing import Tuple, Optional
from datetime import datetime
import requests
from lxml import html  # pylint: disable=import-error

TITLE = "LiveData"  # HTML live data page title
TIMEOUT = 5  # seconds


class BaseSensorData:  # pylint: disable=too-few-public-methods
    """Base class for sensor data"""

    def __init__(self) -> None:
        self.time: Optional[datetime] = None
        self.temp: Optional[float] = None
        self.humidity: Optional[float] = None
        self.battery: Optional[str] = None


class IndoorSensorData(BaseSensorData):  # pylint: disable=too-few-public-methods
    """Indoor sensor data"""

    def __init__(self) -> None:
        super().__init__()
        self.abs_press: Optional[float] = None
        self.rel_press: Optional[float] = None


class OutdoorSensorData(BaseSensorData):  # pylint: disable=too-few-public-methods
    """Outdoor sensor data"""


class AmbientWeather:
    """Class to handle Ambient Weather data retrieval and parsing"""

    @staticmethod
    def parse(live_data_html: bytes) -> Tuple[IndoorSensorData, OutdoorSensorData]:
        """Extract sensor data from html (LiveData.html from your ObserverIP)."""
        tree = html.fromstring(live_data_html)
        title = tree.xpath("//title/text()")
        if title[0] != TITLE:
            raise ValueError(f"Wrong html page. Good one have to have title {TITLE}")

        in_sensor = IndoorSensorData()
        out_sensor = OutdoorSensorData()

        time_str = tree.xpath('//input[@name="CurrTime"]/@value')[0]
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
    def get(url: str) -> Tuple[IndoorSensorData, OutdoorSensorData]:
        """
        Load ObserverIP live data page from the URL and parse it
        """
        page = requests.get(url, timeout=TIMEOUT).content
        return AmbientWeather.parse(page)
