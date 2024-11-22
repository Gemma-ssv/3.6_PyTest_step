import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: e.g. 'en', 'ru', 'es', 'fr', etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nstart browser for test with language: {user_language}..")
    
    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={user_language}")
    
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()