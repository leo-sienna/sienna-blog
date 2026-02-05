#!/usr/bin/env python3
"""Extract footer links from mygif.fun"""

import asyncio
from playwright.async_api import async_playwright

async def extract_footer():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        page = None
        for p in context.pages:
            if "mygif" in p.url:
                page = p
                break
        
        if not page:
            page = await context.new_page()
            await page.goto("https://mygif.fun/")
        
        await page.wait_for_load_state("networkidle")
        
        # Scroll down multiple times to load content
        print("Scrolling down...")
        for i in range(5):
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await asyncio.sleep(2)
        
        # Get page content
        content = await page.content()
        
        # Save for analysis
        with open("/tmp/mygif_content.html", "w") as f:
            f.write(content)
        
        print(f"Saved {len(content)} characters to /tmp/mygif_content.html")
        
        # Try to find footer links
        footer = await page.locator("footer").first()
        if await footer.count() > 0:
            footer_text = await footer.inner_html()
            print(f"\n--- Footer Content ---\n{footer_text[:5000]}")
        else:
            print("No footer found, searching for links...")
            links = await page.locator("a").all()
            print(f"Found {len(links)} total links")
            
            # Print all links
            for link in links[:50]:
                href = await link.get_attribute("href")
                text = await link.inner_text()
                if href and ("http" in href or "/" in href):
                    print(f"  - {text[:50]}: {href[:100]}")
        
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(extract_footer())
