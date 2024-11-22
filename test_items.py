import pytest
from selenium.webdriver.common.by import By

def test_add_to_cart_button_is_present(browser):
    # Открываем страницу товара
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    
    # Убеждаемся, что кнопка найдена
    assert len(add_to_cart_button) > 0, "Add to cart button is not found"