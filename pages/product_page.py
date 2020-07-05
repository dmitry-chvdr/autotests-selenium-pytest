from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .locators import LoginPageLocators


class ProductPage(BasePage):

    def current_product_added_to_basket(self):
        self.click(*ProductPageLocators.BUTTON_ADDED_TO_BASKET)

    def compare_product_name_on_page_and_in_the_basket(self):
        assert self.text_value_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE) ==\
               self.text_value_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET),\
               'Product name on page and it the basket are not equal..'

    def compare_product_price_on_page_and_in_the_basket(self):
        assert self.text_value_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE) ==\
               self.text_value_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET),\
               'Product price on page and it the basket are not equal..'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.should_be_success_message_disappeared(),\
            'Success message is not disappeared, but should be'

    def current_url_should_be_login_page(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_PAGE, 'It is not login page, but should be'



