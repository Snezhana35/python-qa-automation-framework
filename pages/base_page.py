from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def fill(self, locator, value: str):
        locator.fill(value)

    def get_text(self, locator) -> str:
        return locator.inner_text()

    def is_visible(self, locator) -> bool:
        return locator.is_visible()