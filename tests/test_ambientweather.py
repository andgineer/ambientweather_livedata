import pytest
from unittest.mock import patch
import requests
from ambientweather import AmbientWeather
from datetime import datetime


def test_ambientweather_data(ambientweather_data: str):
    in_sensor, out_sensor = AmbientWeather.parse(ambientweather_data.encode("utf-8"))

    assert in_sensor.time == datetime.strptime("2017/10/06 13:55:00", "%Y/%m/%d %H:%M:%S")
    assert in_sensor.temp == 21.9
    assert in_sensor.humidity == 50.0
    assert in_sensor.abs_press == 744.29
    assert in_sensor.rel_press == 728.31
    assert in_sensor.battery == "Normal"
    assert out_sensor.temp == 10.1
    assert out_sensor.humidity == 71.0
    assert out_sensor.battery == "Normal"


def test_parse_wrong_title():
    """Test parsing HTML with wrong title raises ValueError."""
    html_wrong_title = b"""<html><head><title>WrongTitle</title></head><body></body></html>"""

    with pytest.raises(ValueError, match="Wrong html page. Good one have to have title LiveData"):
        AmbientWeather.parse(html_wrong_title)


def test_parse_missing_elements():
    """Test parsing HTML missing required elements raises IndexError."""
    html_missing_elements = b"""<html><head><title>LiveData</title></head><body></body></html>"""

    with pytest.raises(IndexError):
        AmbientWeather.parse(html_missing_elements)


def test_parse_invalid_numeric_values():
    """Test parsing HTML with invalid numeric values raises ValueError."""
    html_invalid_numbers = b"""
    <html><head><title>LiveData</title></head>
    <body>
        <input name="CurrTime" value="13:55 10/06/2017">
        <input name="inTemp" value="invalid">
        <input name="inHumi" value="50">
        <input name="AbsPress" value="744.29">
        <input name="RelPress" value="728.31">
        <input name="inBattSta" value="Normal">
        <input name="outTemp" value="10.1">
        <input name="outHumi" value="71">
        <input name="outBattSta2" value="Normal">
    </body></html>"""

    with pytest.raises(ValueError):
        AmbientWeather.parse(html_invalid_numbers)


def test_parse_invalid_datetime():
    """Test parsing HTML with invalid datetime format raises ValueError."""
    html_invalid_datetime = b"""
    <html><head><title>LiveData</title></head>
    <body>
        <input name="CurrTime" value="invalid-date">
        <input name="inTemp" value="21.9">
        <input name="inHumi" value="50">
        <input name="AbsPress" value="744.29">
        <input name="RelPress" value="728.31">
        <input name="inBattSta" value="Normal">
        <input name="outTemp" value="10.1">
        <input name="outHumi" value="71">
        <input name="outBattSta2" value="Normal">
    </body></html>"""

    with pytest.raises(ValueError):
        AmbientWeather.parse(html_invalid_datetime)


@patch("ambientweather.requests.get")
def test_get_request_timeout(mock_get):
    """Test GET request timeout handling."""
    mock_get.side_effect = requests.exceptions.Timeout()

    with pytest.raises(requests.exceptions.Timeout):
        AmbientWeather.get("http://example.com/LiveData.html")


@patch("ambientweather.requests.get")
def test_get_connection_error(mock_get):
    """Test GET request connection error handling."""
    mock_get.side_effect = requests.exceptions.ConnectionError()

    with pytest.raises(requests.exceptions.ConnectionError):
        AmbientWeather.get("http://192.168.1.999/LiveData.html")


@patch("ambientweather.requests.get")
def test_get_http_error(mock_get):
    """Test GET request HTTP error handling."""
    mock_response = mock_get.return_value
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

    # The current implementation doesn't check status, but let's test what happens
    mock_response.content = b"<html><head><title>404 Not Found</title></head></html>"

    with pytest.raises(ValueError, match="Wrong html page"):
        AmbientWeather.get("http://example.com/nonexistent")
