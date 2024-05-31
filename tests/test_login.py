import pytest

from assertpy import assert_that
from selene import browser

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from resources import generic as gen


users = [
    gen.standard_user,
    gen.locked_out_user,
    gen.problem_user,
    gen.performance_glitch_user,
    gen.error_user,
    gen.visual_user
]


class TestCriticalPath:

    login = LoginPage()
    products = ProductsPage()

    @pytest.mark.parametrize('username', users)
    def test_01_login(self, username):
        browser.open('https://www.saucedemo.com/')
        self.login.login_user(username, gen.password)
        if username == 'locked_out_user':
            assert_that(self.login.return_error_message()).contains('Sorry, this user has been locked out.')
        else:
            assert_that(self.products.return_products_page_title()).is_equal_to('Products')
            self.products.click_menu_button()
            self.products.click_logout_button()
