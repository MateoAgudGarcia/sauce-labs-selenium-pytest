# Sauce Labs - Selenium - Pytest ![Status](https://github.com/MateoAgudGarcia/sauce-labs-selenium-pytest/actions/workflows/main-branch-deployment.yml/badge.svg)

## Description

This project is a proof of concept (POC) demonstrating the integration of Selenium for browser automation with Poetry for dependency management and packaging. It showcases how to set up and manage a Python project using modern tools and practices, including automated testing with Pytest and generating detailed test reports with Allure.

The primary goal of this project is to provide a clear and concise example of how to:

- Use Poetry to manage project dependencies and virtual environments.
- Automate browser interactions and tests using Selenium.
- Write and organize tests using Pytest.
- Generate and visualize test reports with Allure.

By following this POC, developers can quickly get started with these tools and apply similar setups to their own projects.

## Installation

1. Clone the repository:

   ```sh
   git clone git@github.com:mateoagudgarcia/sauce-labs-selenium-pytest.git
   cd sauce-labs-selenium-pytest
   ```

2. Activate the environment using Poetry:

   ```sh
   poetry activate env
   ```

3. Install the dependencies using Poetry:
   ```sh
   poetry install
   ```

## Running Tests

To run the tests, use the following command:

```sh
poetry run pytest
```

### Last 30 builds deployed using GH Pages: [Sauce Labs - Selenium & Pytest - Github Page](https://mateoagudgarcia.github.io/sauce-labs-selenium-pytest)

## Test Reports - Locally

Generate and open the Allure report by running the provided script

```sh
./create_reports.sh
```

## Project Structure

```sh
sauce-labs-selenium-pytest/
├── src/
│   ├── authorized_pages/
│   │   └── authorized_page.py
│   └── login/
│       └── login_page.py
├── tests/
│   ├── conftest.py
│   └── test_selenium.py
├── utilities/
│   └── utils.py
├── .flake8
├── .gitignore
├── .pylintrc
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
└── poetry.lock
```
