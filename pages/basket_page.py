from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_total(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL_FORM)
