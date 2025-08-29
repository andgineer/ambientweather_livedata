[![Build Status](https://github.com/andgineer/ambientweather_livedata/workflows/ci/badge.svg)](https://github.com/andgineer/ambientweather_livedata/actions)
[![Coverage](https://raw.githubusercontent.com/andgineer/ambientweather_livedata/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/andgineer/ambientweather_livedata/blob/python-coverage-comment-action-data/htmlcov/index.html)

# Ambient Weather Data Extractor

Python script that extracts current sensor data from [Ambient Weather stations](https://www.ambientweather.com/) via their [IPObserver](https://www.ambientweather.com/amobserverip.html) web interface.

Parses the IPObserver's LiveData HTML page to extract temperature, humidity, pressure, and battery status using XPath and [lxml](http://lxml.de/).

## Usage

Open your IPObserver's IP address in a browser (`http://YOUR_IP/LiveData.html`) to verify it works, then use that URL with the script.

See [example.py](src/example.py) for usage.

## Coverage Reports
* [Codecov](https://app.codecov.io/gh/andgineer/ambientweather_livedata/tree/master/src)
* [Coveralls](https://coveralls.io/github/andgineer/ambientweather_livedata)
