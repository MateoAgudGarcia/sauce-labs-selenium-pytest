# POC Poetry Selenium

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
    git clone https://github.com/mateoagudelo80/poc-poetry-selenium.git
    cd poc-poetry-selenium
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

## Test Reports
Generate and open the Allure report by running the provided script

```sh
./create_reports.sh
```

## Project Structure
```
poc-poetry-selenium/
├── tests/
│   ├── __init__.py
│   └── test_selenium.py
├── pyproject.toml
└── README.md
```
