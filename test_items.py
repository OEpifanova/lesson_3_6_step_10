from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_check_button(browser):
    browser.get(link)
    time.sleep(30)
    button=browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "Кнопка добавления в корзину не найдена"