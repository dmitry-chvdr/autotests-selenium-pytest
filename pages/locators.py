from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, 'div.page_inner a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTER_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_1_REGISTER_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_2_REGISTER_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTER_SUBMIT = (By.CSS_SELECTOR, '#register_form .btn')


class ProductPageLocators():
    BUTTON_ADDED_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert .alertinner strong')


class BasketPageLocators():
    BASKET_TOTAL_FORM = (By.CSS_SELECTOR, '#total_basket')
    TEXT_BASKET_IS_EMPTY_ON_PAGE = (By.CSS_SELECTOR, 'div#content_inner p')
    TEXT_BASKET_IS_EMPTY_WHICH_EXPECTED = 'Your basket is empty.'
