from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import BasketPageLocators
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.is_not_element_present(*BasketPageLocators.BASKET_TOTAL_FORM)
    page.basket_should_be_empty()
