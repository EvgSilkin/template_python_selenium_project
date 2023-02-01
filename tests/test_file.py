from pages.base_page import BasePage


def test_def(driver):
    page = BasePage(driver, "https://www.citilink.ru/rent/")
    page.open()