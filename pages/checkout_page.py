from selene import be, query
from selene.support.shared.jquery_style import s


class CheckoutPage:

    CHECKOUT_PAGE_TITLE = '.title'
    FIRST_NAME_INPUT = '#first-name'
    LAST_NAME_INPUT = '#last-name'
    POSTAL_CODE_INPUT = '#postal-code'
    CONTINUE_BUTTON = '#continue'
    NET_PRICE = '.summary_subtotal_label'
    TOTAL_PRICE_LABEL = '.summary_total_label'
    FINISH_BUTTON = '#finish'
    ORDER_CONFIRMATION_LABEL = '.complete-header'

    def return_checkout_page_title(self):
        return s(self.CHECKOUT_PAGE_TITLE).should(be.visible).get(query.text)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        s(self.FIRST_NAME_INPUT).should(be.visible).send_keys(first_name)
        s(self.LAST_NAME_INPUT).should(be.visible).send_keys(last_name)
        s(self.POSTAL_CODE_INPUT).should(be.visible).send_keys(postal_code)
        s(self.CONTINUE_BUTTON).should(be.visible and be.clickable).click()

    def return_net_gross(self):
        price_string = s(self.NET_PRICE).should(be.visible).get(query.text)
        net = float(price_string.split('$')[1])
        gross = net * 1.08
        return net, gross

    def click_finish_button(self):
        s(self.FINISH_BUTTON).should(be.visible and be.clickable).click()

    def return_order_confirmation_message(self):
        return s(self.ORDER_CONFIRMATION_LABEL).should(be.visible).get(query.text)
