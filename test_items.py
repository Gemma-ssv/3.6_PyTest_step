"""
test_items.py

Этот модуль содержит тесты для проверки функциональности веб-страницы.
Он использует фикстуру browser из conftest.py для настройки браузера с указанным языком.
"""

from selenium.webdriver.common.by import By

# Ссылка на тестируемую страницу
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    """
    Тест, который проверяет наличие ссылки для входа на странице.

    Параметры:
    browser (webdriver.Chrome): Настроенный экземпляр браузера Chrome.

    Ожидаемый результат:
    Ссылка для входа должна быть найдена на странице.
    """
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")