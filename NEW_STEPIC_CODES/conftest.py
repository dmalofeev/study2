import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# 1. Добавляем опцию --language в командную строку
def pytest_addoption(parser):
    parser.addoption(
        '--language', 
        action='store', 
        default='en', 
        help="Choose language: ru, en, es, etc."
    )

# 2. Фикстура для запуска браузера с выбранным языком
@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")
    print(f"\nЗапуск тестов с языком: {user_language}")

    # Получаем имя браузера из фикстуры (если она есть) или используем Chrome по умолчанию
    # Если у вас нет отдельной фикстуры для выбора браузера, просто используйте нужный вам вариант
    browser_name = request.config.getoption("--browser_name", "chrome") # "chrome" or "firefox"

    if browser_name == "chrome":
        # Настройка языка для Chrome
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        
        print("Запуск браузера Chrome...")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        # Настройка языка для Firefox
        fp = FirefoxOptions()
        # Для Firefox в новых версиях Selenium используется метод set_preference в объекте Options
        fp.set_preference("intl.accept_languages", user_language)
        
        print("Запуск браузера Firefox...")
        driver = webdriver.Firefox(options=fp)

    else:
        raise pytest.UsageError(f"--browser_name {browser_name} не поддерживается. Используйте 'chrome' или 'firefox'.")

    # Необязательно: развернуть окно на весь экран
    driver.maximize_window()

    # Передаем драйвер в тест
    yield driver

    # Действия после завершения теста (закрытие браузера)
    print("\nЗакрытие браузера...")
    driver.quit()