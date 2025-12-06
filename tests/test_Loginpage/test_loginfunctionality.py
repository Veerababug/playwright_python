from logging import log
import re
from playwright.sync_api import Page, expect


def test_loginfunctionality(page):
    page.goto("https://www.google.com/?zx=1763794504740&no_sw_cr=1")
    log.info("Navigated to Google homepage")
    page.get_by_role("combobox", name="Search").click()
    log.info("Clicked on the search combobox")
    page.get_by_role("combobox", name="Search").fill("Microsoft")
    log.info("Filled 'Microsoft' in the search combobox")
    expect(page.get_by_text("About this page")).to_be_visible()
    log.info("Verified that 'About this page' text is visible on the page")
