#!/usr/bin/env python3
"""Extract Elon Musk's recent tweets using Playwright CDP"""

import asyncio
from playwright.async_api import async_playwright

async def extract_tweets():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        # Navigate to Elon Musk's profile
        page = None
        for p in context.pages:
            if "elonmusk" in p.url:
                page = p
                break
        
        if not page:
            page = await context.new_page()
            await page.goto("https://x.com/elonmusk")
        
        await page.wait_for_load_state("networkidle")
        
        # Scroll down to load more tweets
        print("📜 Scrolling to load more tweets...")
        for i in range(5):
            await page.evaluate("window.scrollBy(0, 1000)")
            await asyncio.sleep(1)
        
        # Extract tweets
        print("\n📊 Extracting Elon Musk's tweets...")
        
        # Try to find tweet articles
        tweets = await page.locator('article').all()
        print(f"Found {len(tweets)} tweet elements")
        
        # Also try to get timeline content
        timeline = await page.locator('[data-testid="primaryColumn"]').first()
        
        # Print visible text content
        content = await page.content()
        
        # Save to file
        with open("/tmp/elon_tweets.html", "w") as f:
            f.write(content)
        
        print(f"\n📄 Saved page content to /tmp/elon_tweets.html")
        print(f"📏 Content length: {len(content)} characters")
        
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(extract_tweets())
