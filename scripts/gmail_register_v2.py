#!/usr/bin/env python3
"""
Gmail Registration Automation using Playwright
Connects to OpenClaw's Chrome CDP for seamless automation
"""

import asyncio
from playwright.async_api import async_playwright

async def register_gmail():
    print("🔗 Connecting to OpenClaw Chrome CDP...")
    
    async with async_playwright() as p:
        # Connect to OpenClaw's existing Chrome session
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        
        # Get all pages
        context = browser.contexts[0]
        pages = context.pages
        
        # Find or create signup page
        signup_page = None
        for page in pages:
            if "signup" in page.url:
                signup_page = page
                break
        
        if not signup_page:
            print("📧 Opening Gmail signup page...")
            signup_page = await context.new_page()
            await signup_page.goto("https://accounts.google.com/signup")
        
        print(f"📍 Current URL: {signup_page.url}")
        print(f"📝 Page title: {await signup_page.title()}")
        
        await signup_page.wait_for_load_state("networkidle")
        
        # Step 1: Fill name
        print("\n👤 Step 1: Filling name...")
        
        try:
            first_name = signup_page.locator('input[name="firstName"]')
            await first_name.fill("Sienna")
            print("✅ Filled first name: Sienna")
            
            # Click Next
            print("\n➡️  Clicking Next...")
            next_btn = signup_page.locator('button:has-text("下一步")')
            await next_btn.click()
            await signup_page.wait_for_load_state("networkidle")
            print("✅ Clicked Next button")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print(f"\n📍 Current URL: {signup_page.url}")
        
        # Keep browser open for continued automation
        print("\n🎉 Gmail registration automation ready!")
        print("   Continue with step 2: Birthday and gender...")
        
        # Wait for user to continue
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(register_gmail())
