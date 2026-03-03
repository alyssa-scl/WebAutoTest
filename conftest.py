# -*- coding: utf-8 -*-
#  author:  scl
#  date:    2025/8/8  
from playwright.async_api import async_playwright,Playwright  
import asyncio
import pytest

@pytest.fixture(scope="session")
async def browser(browser_name="chrome"):
    async with async_playwright() as playwright:
        if browser_name == "chrome":
            chromium = playwright.chromium
            browser = await chromium.launch(headless=False, args=["--lang=en-US"]) 
        elif browser_name == "firefox":
            firefox = playwright.firefox
            browser = await firefox.launch(headless=False, args=["--lang=en-US"])
        elif browser_name == "webkit":
            webkit = playwright.webkit
            browser = await webkit.launch(headless=False, args=["--lang=en-US"])    
        yield browser
        await browser.close()

@pytest.fixture
async  def page(brower, url):
    page = await brower.new_page()
    await page.goto(url, wait_until="domcontentloaded")
    yield page
    await page.close()