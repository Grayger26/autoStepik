from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину
def test_stepik(browser):
    browser.implicitly_wait(5)

    browser.get(link)
    browser.maximize_window()

    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

