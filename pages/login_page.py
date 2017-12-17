from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):
    locator_dictionary = {
    'login_btn': (By.LINK_TEXT, 'LOGIN'),
    'login_popup':  (By.CSS_SELECTOR, '.b-loginform__body'), 
    'user_field': (By.NAME, 'user'),
    'password_field': (By.NAME, 'password'),
    'submit_login': (By.CSS_SELECTOR, 
                    '[class="b-loginform-btn b-loginform-btn--login"]'
    ),
    }
    def login(self, user, password):
        self.login_btn.click()
        self.login_popup
        self.user_field.send_keys(user)
        self.password_field.send_keys(password)
        self.submit_login.click()
