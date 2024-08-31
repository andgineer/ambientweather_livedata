[![Build Status](https://github.com/andgineer/ambientweather_livedata/workflows/ci/badge.svg)](https://github.com/andgineer/ambientweather_livedata/actions)
[![Coverage](https://raw.githubusercontent.com/andgineer/ambientweather_livedata/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/andgineer/ambientweather_livedata/blob/python-coverage-comment-action-data/htmlcov/index.html)
# Extract data from Ambient Weather stations

Python library that extracts information from [Ambient Weather stations](https://www.ambientweather.com/).

So if you have an Ambient Weather station and you want to get the data from it, this library is for you.

It collects sensor's data (temperature and humidity) from the [IPObserver](https://www.ambientweather.com/amobserverip.html) `LiveData` tab of the IPObserver web-page.
You can get this page from the IPObserver - just open the IPObserver IP adddress in your web-brawser to see it.

The library uses xpath and [lxml](http://lxml.de/).

[Example](src/example.py)


## Coverage report
* [Codecov](https://app.codecov.io/gh/andgineer/ambientweather_livedata/tree/master/src)
* [Coveralls](https://coveralls.io/github/andgineer/ambientweather_livedata)

