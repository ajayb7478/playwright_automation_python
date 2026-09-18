import playwright
import pytest
from playwright.sync_api import Page, Playwright, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/")
    print(page.title())

    assert page.title() == "Rahul Shetty Academy | QA Automation, Playwright, AI Testing & Online Training"

    browser.close()


def test_playwrightShortcut(page: Page):
    page.goto("https://rahulshettyacademy.com/")
    print(page.title())

    assert page.title() == "Rahul Shetty Academy | QA Automation, Playwright, AI Testing & Online Training"

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractice/")
    page.get_by_label("UserName").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefoxBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/")
    print(page.title())

    assert page.title() == "Rahul Shetty Academy | QA Automation, Playwright, AI Testing & Online Training"

    browser.close()