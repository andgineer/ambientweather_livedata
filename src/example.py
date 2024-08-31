"""Example script to demonstrate the usage of the AmbientWeather class."""

from ambientweather import AmbientWeather


def show_weather() -> None:
    """Retrieve and display weather data from an Ambient Weather station."""
    in_sensor, out_sensor = AmbientWeather.get("http://10.0.0.176/LiveData.html")
    delimiter = "=" * 20

    print(f"Time: {in_sensor.time}\n")

    print(f"Indoor\n{delimiter}")
    print(f"Temperature: {in_sensor.temp}")
    print(f"Humidity: {in_sensor.humidity}")
    print(f"Absolute pressure: {in_sensor.abs_press}")
    print(f"Relative pressure: {in_sensor.rel_press}")
    print(f"Battery status: {in_sensor.battery}\n")

    print(f"Outdoor\n{delimiter}")
    print(f"Temperature: {out_sensor.temp}")
    print(f"Humidity: {out_sensor.humidity}")
    print(f"Battery status: {out_sensor.battery}")


if __name__ == "__main__":
    show_weather()
