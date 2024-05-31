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
        options.add_argument("--headless")
        browser.config.driver = webdriver.Chrome(service=Service(), options=options)
        browser.driver().maximize_window()
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        from selenium.webdriver.firefox.service import Service
        browser.config.driver = webdriver.Firefox(service=Service(), options=options)
        browser.driver().maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield
    browser.quit()
