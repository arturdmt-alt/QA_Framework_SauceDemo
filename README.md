# QA Framework - SauceDemo

[![Tests](https://github.com/arturdmt-alt/QA_Framework_SauceDemo/actions/workflows/tests.yml/badge.svg)](https://github.com/arturdmt-alt/QA_Framework_SauceDemo/actions/workflows/tests.yml)

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.57-green.svg)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-9.0-red.svg)](https://pytest.org/)
[![Tests](https://img.shields.io/badge/Tests-15%20passed-brightgreen.svg)]()

> Professional test automation framework using Python, Playwright and Page Object Model for E2E testing of SauceDemo.

---

## Features

-  **Page Object Model (POM)** - Scalable and maintainable architecture
-  **Pytest Markers** - Smoke, Regression, E2E tests organized
-  **Screenshots on Failure** - Automatic error capture
-  **Allure Reports** - Professional dashboards with graphs
-  **15 Test Cases** - Complete coverage of critical functionalities
-  **CI/CD Ready** - Prepared for continuous integration

---

## Tech Stack

- Python 3.11+
- Playwright 1.57.0
- Pytest 9.0.2
- Allure 2.36.0

---

## Project Structure
```
QA_Framework_SauceDemo/
├── pages/              # Page Object Models
├── tests/              # Test suites
├── core/               # Core utilities
├── reports/            # Allure reports
├── screenshots/        # Failure screenshots
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## Installation
```bash
# Clone repository
git clone https://github.com/arturdmt-alt/QA_Framework_SauceDemo.git
cd QA_Framework_SauceDemo

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
playwright install chromium
```

---

## Usage
```bash
# Run all tests
pytest -v

# Run smoke tests
pytest -m smoke -v

# Run with Allure report
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## Test Cases (15 total - 100% passing)

- **Login:** Valid credentials
- **Products:** Add single/multiple products, sorting functionality
- **Cart:** View items, remove products
- **Checkout:** Complete flow with validations
- **E2E:** Full purchase journey

---

## Reports

Allure reports include:
- Dashboard with metrics
- Execution timeline
- Success rate graphs
- Test case details
- Failure screenshots

---

## Test Reports

This framework generates professional Allure reports with detailed test execution analytics.

### Latest Test Results
-  **15/15 tests passing** (100% success rate)
-  **Execution time:** ~50 seconds
-  **Last run:** December 15, 2025

### Sample Reports

#### Overview Dashboard
![Allure Overview](docs/allure-overview.jpg)
*15 automated tests with 100% pass rate*

#### Test Suites
![Test Suites](docs/allure-suites.jpg)
*Complete test coverage across all features*

#### Timeline
![Timeline](docs/allure-timeline.jpg)
*Fast and efficient test execution*

#### Test Behaviors
![Behaviors](docs/allure-behaviors.jpg)
*Detailed view of all 15 test cases*

### Generate Reports Locally
```bash
# Run tests with Allure
pytest --alluredir=reports/allure-results

# View report
allure serve reports/allure-results
```

---

## Troubleshooting & Lessons Learned

### CI/CD Debugging Process (Dec 14, 2024)

**Challenge:** Initial CI/CD implementation revealed cascading failures across workflows #1-#15

**Root Cause:** 
Tests for product sorting functionality were written before implementing the required methods in the Page Object Model, causing `AttributeError` when tests tried to call `get_product_names()` and `get_product_prices()`.

**Solution:**
Added missing getter methods to `ProductsPage` class with proper Playwright waits and data transformations.

**Current Status:**
-  All 15 automated tests passing
-  CI/CD pipeline stable (workflows #16, #17, #18)
-  Full test coverage: Login, Products, Cart, Checkout, E2E flows

**Key Takeaway:** 
This debugging journey demonstrates real-world problem-solving and the value of CI/CD for catching integration issues early.

---

## Author

**Artur Dmytriyev**
- LinkedIn: www.linkedin.com/in/arturdmytriyev
- GitHub: https://github.com/arturdmt-alt 

---
