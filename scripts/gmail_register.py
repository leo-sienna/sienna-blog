#!/usr/bin/env python3
"""
Gmail Registration Script using Playwright
Connects to OpenClaw's CDP port 18800
"""

import asyncio
from playwright.async_api import async_playwright

async def register_gmail():
    async with async_playwright() as p:
        # Connect to OpenClaw's Chrome via CDP
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        
        context = browser.contexts[0]
        page = context.pages[0]  # Get the Gmail signup page
        
        print(f"📧 Current page: {page.url}")
        print(f"📝 Page title: {await page.title()}")
        
        # Step 1: Fill name
        print("\n👤 Step 1: Filling name...")
        
        # Try to find and fill first name
        first_name_input = page.locator('input[name="firstName"]')
        if await first_name_input.count() > 0:
            await first_name_input.fill("Sienna")
            print("✅ Filled first name: Sienna")
        else:
            print("❌ First name input not found")
            
        # Click Next button
        print("\n➡️  Clicking Next...")
        next_button = page.locator('button:has-text("下一步")')
        if await next_button.count() > 0:
            await next_button.click()
            print("✅ Clicked Next button")
            await page.wait_for_load_state("networkidle")
        else:
            print("❌ Next button not found")
            
        print(f"\n📍 Current URL: {page.url}")
        
        # Keep browser open for user interaction
        print("\n⏸️  Browser remains open. Press Ctrl+C to close.")
        
        # Keep running
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(register_gmail())
