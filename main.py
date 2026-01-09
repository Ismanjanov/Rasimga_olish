import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.showmyip.com/")
        await page.wait_for_timeout(4000)
        await page.screenshot(path="showmyip.png")
        await browser.close()

asyncio.run(run())
