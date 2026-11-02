from playwright.sync_api import expect

from pages.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.locator(
            '[data-test="username"]'
        )

        self.password_input = page.locator(
            '[data-test="password"]'
        )

        self.login_button = page.locator(
            '[data-test="login-button"]'
        )

        self.error_message = page.locator(
            '[data-test="error"]'
        )

    def open_login_page(self):
        self.open(BASE_URL)

    def login(self, username: str, password: str):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self) -> str:
        return self.get_text(self.error_message)

    def should_show_error(self, expected_message: str):
        expect(self.error_message).to_have_text(
            expected_message
        )