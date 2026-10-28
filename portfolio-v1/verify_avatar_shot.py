import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("http://127.0.0.1:8080/", timeout=15000)
        await page.wait_for_timeout(1000)
        
        # Locate avatar frame and screenshot it
        frame = await page.query_selector('.avatar-frame')
        if frame:
            await frame.screenshot(path="C:/Users/mdtus/.gemini/antigravity/brain/f89021bc-d7cb-4aeb-8c8d-17364251a84f/avatar_new_crop.png")
            print("Captured avatar frame screenshot!")
        else:
            print("Avatar frame not found")
        await browser.close()

asyncio.run(run())
