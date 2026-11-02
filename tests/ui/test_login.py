from playwright.sync_api import expect

from pages.inventory_page import InventoryPage

from config.settings import (
    VALID_USERNAME,
    VALID_PASSWORD,
    LOCKED_USERNAME,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVENTORY_URL,
)

def test_username_field_is_displayed(login_page):
    """Verify username field is displayed on the page."""

    login_page.open_login_page()

    expect(login_page.username_input).to_be_visible()

def test_active_login_button(login_page):
    """Verify Login button is active."""

    login_page.open_login_page()

    expect(login_page.login_button).to_be_enabled()

def test_successful_login(login_page):
    """Verify login with valid credentials."""

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.page).to_have_url(INVENTORY_URL)

def test_successful_navigate_to_inventory(login_page):
    """Verify navigating to inventory page."""

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    inventory_page = InventoryPage(login_page.page)

    expect(inventory_page.page_title).to_be_visible()

def test_login_with_invalid_password(login_page):
    """Verify login with an invalid password."""

    login_page.login(
        VALID_USERNAME,
        INVALID_PASSWORD
    )

    login_page.should_show_error(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_with_invalid_username(login_page):
    """Verify login with an invalid username."""

    login_page.login(
        INVALID_USERNAME,
        VALID_PASSWORD
    )

    login_page.should_show_error(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_login_with_empty_username(login_page):
    """Verify login with empty username and password."""

    login_page.login("", VALID_PASSWORD)

    login_page.should_show_error(
        "Epic sadface: Username is required"
    )

def test_login_with_empty_password(login_page):
    """Verify login with empty username and password."""

    login_page.login(VALID_USERNAME, "")

    login_page.should_show_error(
        "Epic sadface: Password is required"
    )


def test_login_with_empty_credentials(login_page):
    """Verify login with empty username and password."""

    login_page.login("", "")

    login_page.should_show_error(
        "Epic sadface: Username is required"
    )


def test_login_with_locked_user(login_page):
    """Verify that a locked user cannot log in."""

    login_page.login(
        LOCKED_USERNAME,
        VALID_PASSWORD
    )

    login_page.should_show_error(
        "Epic sadface: Sorry, this user has been locked out."
    )