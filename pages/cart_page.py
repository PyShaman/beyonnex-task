from selene import be, query
from selene.support.shared.jquery_style import s, ss


class CartPage:

    CART_PAGE_TITLE = '.title'
    CART_ITEM_NAME = '.inventory_item_name '
    CART_ITEM_PRICE = '.inventory_item_price'
    CART_CHECKOUT_BUTTON = '//button[@id="checkout"]'

    def return_cart_page_title(self):
        return s(self.CART_PAGE_TITLE).should(be.visible).get(query.text)

    def return_inventory_cart_name_and_price(self, quantity):
        added_products = {}
        for x in range(quantity):
            name = ss(self.CART_ITEM_NAME)[x].should(be.visible).get(query.text)
            price = ss(self.CART_ITEM_PRICE)[x].should(be.visible).get(query.text)
            added_products[name] = price
        return added_products

    def click_on_checkout_button(self):
        s(self.CART_CHECKOUT_BUTTON).should(be.visible and be.clickable).click()
