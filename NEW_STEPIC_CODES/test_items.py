import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ссылка на страницу товара
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_add_product_to_basket(browser):

    

    """
    Тест проверяет возможность добавления товара в корзину.
    1. Открывает страницу товара.
    2. Нажимает кнопку "Добавить в корзину".
    3. Проверяет появление сообщения о добавлении.
    """
    # 1. Открываем ссылку
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    # 2. Находим кнопку "Добавить в корзину" и нажимаем на неё.
    # Используем явное ожидание, чтобы дождаться, пока кнопка станет кликабельной.
    # Селектор: ищем кнопку по её тексту и типу.
    add_to_basket_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    add_to_basket_button.click()

    # 3. Проверяем, что появилось сообщение о добавлении в корзину.
    # Ожидаем появления элемента с классом 'alertinner'.
    # В реальном тесте здесь можно было бы проверить текст сообщения, но в задании требуется только наличие элемента.
    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.alertinner"))
    )

    # Проверка, что элемент действительно найден (является частью DOM)
    assert success_message is not None, "Сообщение о добавлении товара не появилось"

    # Дополнительная проверка: элемент должен быть видимым на странице.
    assert success_message.is_displayed(), "Сообщение о добавлении не отображается на странице"