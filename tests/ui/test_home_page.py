import re

from playwright.sync_api import Page, expect


def test_home_page_is_open(page: Page):
    page.goto("https://automationexercise.com/")

    expect(page).to_have_title(
        re.compile("Automation Exercise")
    )