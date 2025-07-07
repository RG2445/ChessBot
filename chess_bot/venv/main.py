import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  
        context = await browser.new_context()
        page = await context.new_page()
        
       
        await page.goto("https://www.chess.com/play/computer")

   
        await page.wait_for_selector(".board")  
        print("Chess.com loaded and board ready")

        await asyncio.sleep(99999)  

        await browser.close()

asyncio.run(main())
