import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("http://127.0.0.1:8080/", timeout=15000)
        await page.wait_for_timeout(1000)
        await page.screenshot(path="C:/Users/mdtus/.gemini/antigravity/brain/f89021bc-d7cb-4aeb-8c8d-17364251a84f/no_emoji_verified.png")
        print("Captured verification screenshot!")
        await browser.close()

asyncio.run(run())
