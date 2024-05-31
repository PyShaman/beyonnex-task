from selene import be, query
from selene.support.shared.jquery_style import s


class LoginPage:

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = 'h3[data-test="error"]'

    def login_user(self, username, password):
        s(self.USERNAME_INPUT).should(be.visible).send_keys(username)
        s(self.PASSWORD_INPUT).should(be.visible).send_keys(password)
        s(self.LOGIN_BUTTON).should(be.visible and be.clickable).click()

    def return_error_message(self):
        return s(self.ERROR_MESSAGE).should(be.visible).get(query.text)
