from assertpy import assert_that, soft_assertions
from selene import browser

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from resources import generic as gen


class CartProducts:
    _initial_data = {}

    def __init__(self):
        self.__dict__ = self._initial_data
        self.cart = None


class TestAddToCart:

    cart = CartPage()
    checkout = CheckoutPage()
    login = LoginPage()
    products = ProductsPage()
    cart_products = CartProducts()
    quantity_of_products = 3

    @staticmethod
    def get_net_gross(dict_data):
        total_net = 0
        for value in dict_data.values():
            float_value = float(value.split('$')[1])
            total_net += float_value
        total_gross = total_net * 1.08
        return total_net, total_gross

    def test_01_login(self):
        browser.open('https://www.saucedemo.com/')
        self.login.login_user(gen.standard_user, gen.password)
        assert_that(self.products.return_products_page_title()).is_equal_to('Products')

    def test_02_add_to_cart(self):
        self.products.click_on_sorting_button('hilo')
        self.cart_products.cart = self.products.add_products_to_cart(self.quantity_of_products)
        number_of_products = self.products.return_number_of_added_items()
        assert_that(number_of_products).is_equal_to(self.quantity_of_products)

    def test_03_verify_added_products(self):
        self.products.click_on_cart_button()
        products_in_cart = self.cart.return_inventory_cart_name_and_price(self.quantity_of_products)
        with soft_assertions():
            assert_that(self.cart.return_cart_page_title()).is_equal_to('Your Cart')
            assert_that(self.cart_products.cart).is_equal_to(products_in_cart)

    def test_04_go_to_checkout(self):
        self.cart.click_on_checkout_button()
        assert_that(self.checkout.return_checkout_page_title()).is_equal_to('Checkout: Your Information')

    def test_05_fill_checkout_information(self):
        persona_a = gen.persona_a
        self.checkout.fill_checkout_information(persona_a['first_name'],
                                                persona_a['last_name'],
                                                persona_a['postal_code'])

    def test_06_verify_order(self):
        net_value, gross_value = self.get_net_gross(self.cart_products.cart)
        net_value_checkout, gross_value_checkout = self.checkout.return_net_gross()
        with soft_assertions():
            assert_that(self.checkout.return_checkout_page_title()).is_equal_to('Checkout: Overview')
            assert_that(net_value).is_equal_to(net_value_checkout)
            assert_that(gross_value).is_equal_to(gross_value_checkout)

    def test_07_verify_order_confirmation(self):
        self.checkout.click_finish_button()
        with soft_assertions():
            assert_that(self.checkout.return_checkout_page_title()).is_equal_to('Checkout: Complete!')
            assert_that(self.checkout.return_order_confirmation_message()).is_equal_to('Thank you for your order!')
