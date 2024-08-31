import pytest
from unittest.mock import patch
import sys
from io import StringIO

from example import show_weather
from ambientweather import AmbientWeather, IndoorSensorData, OutdoorSensorData


def test_show_weather(ambientweather_data):
    """Test the show_weather function from example.py."""
    in_sensor, out_sensor = AmbientWeather.parse(ambientweather_data.encode('utf-8'))

    # Mock the AmbientWeather.get method to return our parsed data
    with patch('ambientweather.AmbientWeather.get', return_value=(in_sensor, out_sensor)):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        show_weather()

        # Restore stdout
        sys.stdout = sys.__stdout__

    # Get the captured output
    output = captured_output.getvalue()

    # Assert that the output contains expected information
    assert f"Time: {in_sensor.time}" in output
    assert "Indoor" in output
    assert f"Temperature: {in_sensor.temp}" in output
    assert f"Humidity: {in_sensor.humidity}" in output
    assert f"Absolute pressure: {in_sensor.abs_press}" in output
    assert f"Relative pressure: {in_sensor.rel_press}" in output
    assert f"Battery status: {in_sensor.battery}" in output
    assert "Outdoor" in output
    assert f"Temperature: {out_sensor.temp}" in output
    assert f"Humidity: {out_sensor.humidity}" in output
    assert f"Battery status: {out_sensor.battery}" in output
