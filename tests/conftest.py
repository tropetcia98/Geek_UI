import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'https://www.chookgeek.ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

