import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help ="Choose from langs: (ru/en/es...)")

# For Chrome
options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': "language"})
# For Fifefox
options2 = OptionsFirefox()
options2.set_preference("intl.accept_languages", "language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options2)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
# browser = webdriver.Chrome(options=options)

# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# options = Options()
# options.set_preference("intl.accept_languages", user_language)
# driver_browser = webdriver.Firefox(options=options)