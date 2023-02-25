import pytest
from selene.support.shared import browser


@pytest.fixture
def window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture
def open_browser(window_size):
    browser.open('https://google.com')


@pytest.fixture
def open_browser_form(window_size):
    browser.open('https://demoqa.com/automation-practice-form')
