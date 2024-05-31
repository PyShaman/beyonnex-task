import pytest

from selene import browser
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='browser to run tests'
    )


@pytest.fixture(scope='session', autouse=True)
def browser_setup(pytestconfig):
    browser_name = pytestconfig.getoption("browser")

    if browser_name == 'chrome':
        from selenium.webdriver.chrome.service import Service
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument('--start-maximized')
        browser.config.driver = webdriver.Chrome(service=Service('drivers/chromedriver'), options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument('--start-maximized')
        from selenium.webdriver.firefox.service import Service
        browser.config.driver = webdriver.Firefox(service=Service('drivers/geckodriver'), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield
    browser.quit()
