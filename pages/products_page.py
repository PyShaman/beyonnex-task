from selene import be, query
from selene.support.shared.jquery_style import s, ss


class ProductsPage:

    PRODUCTS_TITLE = '.title'
    MENU_BUTTON = '//button[@id="react-burger-menu-btn"]'
    LOGOUT_BUTTON = '//a[@id="logout_sidebar_link"]'
    SORTING_BUTTON = '.product_sort_container'
    SORTING_OPTION = '[value="{}"]'
    ADD_TO_CART_BUTTON = '//button[normalize-space()="Add to cart"]'
    PRODUCT_NAME = '.inventory_item_name '
    PRODUCT_PRICE = '.inventory_item_price'
    REMOVE_FROM_CART_BUTTON = '//button[normalize-space()="Remove"]'
    SHOPPING_CART_BUTTON = '.shopping_cart_link'

    def return_products_page_title(self):
        return s(self.PRODUCTS_TITLE).should(be.visible).get(query.text)

    def click_menu_button(self):
        s(self.MENU_BUTTON).should(be.visible and be.clickable).click()

    def click_logout_button(self):
        s(self.LOGOUT_BUTTON).should(be.visible and be.clickable).click()

    def click_on_sorting_button(self, option):
        """
        Options of sorting
        - from A to Z: 'az'
        - from Z to A: 'za'
        - from lowest to highest: 'lohi'
        - from highest to lowest: 'hilo'
        """
        s(self.SORTING_BUTTON).should(be.visible and be.clickable).s(self.SORTING_OPTION.format(option)).click()

    def add_products_to_cart(self, quantity):
        added_products = {}
        for i in range(quantity):
            s(self.ADD_TO_CART_BUTTON).should(be.visible and be.clickable).click()
            added_products[self.return_product_name_and_price(i)[0]] = \
                self.return_product_name_and_price(i)[1]
        return added_products

    def return_product_name_and_price(self, index):
        product = ss(self.PRODUCT_NAME)[index].get(query.text)
        price = ss(self.PRODUCT_PRICE)[index].get(query.text)
        return [product, price]

    def return_number_of_added_items(self):
        return int(s(self.SHOPPING_CART_BUTTON).get(query.text))

    def click_on_cart_button(self):
        s(self.SHOPPING_CART_BUTTON).click()
