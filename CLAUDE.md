# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python library that extracts sensor data from Ambient Weather IPObserver devices by scraping their LiveData HTML interface. The library parses temperature, humidity, pressure, and battery status using XPath selectors.

## Development Commands

### Environment Setup
```bash
source activate.sh  # Creates/activates Python 3.12 venv and installs dependencies
```

### Testing
```bash
make test                                    # Run all tests
python -m pytest -s -v --doctest-modules   # Verbose test output with coverage
python -m pytest tests/test_ambientweather.py -v  # Run specific test file
```

### Code Quality
```bash
ruff check .          # Lint entire project
ruff format .         # Format code
pre-commit run mypy --all-files  # Type checking (installs stubs automatically)
pre-commit run --all-files  # Run all pre-commit hooks
```

### Manual Testing
```bash
cd src && python example.py  # Run usage example (requires live IPObserver device)
```

## Architecture

### Core Components

**Data Classes** (`src/ambientweather.py`):
- `BaseSensorData`: Common sensor fields (time, temp, humidity, battery)
- `IndoorSensorData`: Extends base with pressure readings (abs_press, rel_press)
- `OutdoorSensorData`: Basic outdoor sensor without pressure

**Main Class**:
- `AmbientWeather`: Static methods for fetching (`get()`) and parsing (`parse()`) HTML data

### XPath-Based Parsing
The library uses lxml with XPath selectors to extract sensor readings from the IPObserver's HTML table structure. All XPath expressions are defined as constants in the main module.

### Testing Strategy
- Fixture-based testing using sample HTML from `tests/resources/LiveData.html`
- Covers both parsing logic and HTTP fetching scenarios
- Test data represents actual IPObserver output format

## Development Notes

### Code Quality Standards
- Line length: 99 characters
- Full type annotations required (MyPy enforced)
- Comprehensive Ruff linting rules including security, complexity, and Pylint compatibility
- Pre-commit hooks ensure code quality before commits

### Python Version Support
Supports Python 3.10, 3.11, and 3.12. The development environment uses Python 3.12.

### Dependencies
- **Core**: `lxml` (HTML parsing), `requests` (HTTP client)
- **Dev**: `pytest`, `mypy`, `ruff`, `pre-commit`, `pylint`

### CI/CD Pipeline
Multi-platform testing (Ubuntu, macOS, Windows) with coverage reporting to Coveralls, Codecov, and GitHub PR comments.
