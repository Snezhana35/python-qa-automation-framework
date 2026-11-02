from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.get_by_text(
            "Products",
            exact=True
        )