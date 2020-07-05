from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators
from pages.locators import BasketPageLocators
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


@pytest.mark.add_product_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = (str(time.time()) + "@mail.ru")
        password = 'A1334587b'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.current_product_added_to_basket()
        page.compare_product_name_on_page_and_in_the_basket()
        page.compare_product_price_on_page_and_in_the_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(self, browser):
    page = ProductPage(browser, link)
    page.open()
    page.current_product_added_to_basket()
    page.compare_product_name_on_page_and_in_the_basket()
    page.compare_product_price_on_page_and_in_the_basket()


def test_guest_cant_see_success_message(self, browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.current_product_added_to_basket()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.current_product_added_to_basket()
    page.should_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    assert page.browser.current_url == LoginPageLocators.LOGIN_PAGE, 'It is not login page, but should be'


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.is_not_element_present(*BasketPageLocators.BASKET_TOTAL_FORM)
    assert page.text_value_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY) == \
        BasketPageLocators.TEXT_BASKET_IS_EMPTY_WHICH_EXPECTED, 'Text on page is not what is expected..'
