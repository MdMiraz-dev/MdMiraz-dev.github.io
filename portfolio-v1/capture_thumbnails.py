import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 720})
        
        # 1. Coffee shop
        try:
            print("Capturing Coffee Shop...", flush=True)
            await page.goto("http://127.0.0.1:8080/projects/coffee-shop/index.html", timeout=15000)
            await page.wait_for_timeout(1000)
            await page.screenshot(path="images/project_coffee_shop.png")
            print("Coffee Shop captured!", flush=True)
        except Exception as e:
            print("Coffee Shop error:", e, flush=True)

        # 2. Madrasha ERP
        try:
            print("Capturing Madrasha ERP...", flush=True)
            await page.goto("http://127.0.0.1:8080/madrasha-erp-demo.html", timeout=15000)
            await page.wait_for_timeout(1000)
            await page.screenshot(path="images/project_madrasha_erp.png")
            print("Madrasha ERP captured!", flush=True)
        except Exception as e:
            print("Madrasha ERP error:", e, flush=True)

        # 3. Hermes Agent
        try:
            print("Capturing Hermes Agent...", flush=True)
            await page.goto("http://127.0.0.1:8080/hermes-agent-demo.html", timeout=15000)
            await page.wait_for_timeout(1000)
            await page.screenshot(path="images/project_hermes_agent.png")
            print("Hermes Agent captured!", flush=True)
        except Exception as e:
            print("Hermes Agent error:", e, flush=True)

        # 4. 3D Portfolio
        try:
            print("Capturing 3D Portfolio...", flush=True)
            await page.goto("http://127.0.0.1:8080/projects/3d-portfolio/index.html", timeout=15000)
            await page.wait_for_timeout(2000)
            await page.screenshot(path="images/project_3d_portfolio.png")
            print("3D Portfolio captured!", flush=True)
        except Exception as e:
            print("3D Portfolio error:", e, flush=True)

        await browser.close()
        print("Done capturing all!", flush=True)

asyncio.run(main())
