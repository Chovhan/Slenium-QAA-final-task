from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")

    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner>p>strong")

    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span>a.btn-default")


class BasketPageLocators():
    BASKET_GOODS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
