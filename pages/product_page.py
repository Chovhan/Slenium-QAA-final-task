from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket button' was not founded on page"

    def put_confirmation_number_to_alert(self):
        self.solve_quiz_and_get_code()

    def should_be_equal_product_price_on_page_and_price_in_basket(self):
        product_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price_in_basket == product_price_on_page, f"Product price is not equals. Should be '{product_price_on_page}' but not '{product_price_in_basket}'"

    def should_be_equal_product_name_on_page_and_price_in_basket(self):
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name_in_basket == product_name_on_page, f"Product names is not equals. Should be '{product_name_on_page}' but not '{product_name_in_basket}'"

    def should_be_message_about_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is not presented, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_on_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is not disappeared, but should be"