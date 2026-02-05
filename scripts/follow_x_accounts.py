#!/usr/bin/env python3
"""Follow accounts on X using Playwright CDP"""

import asyncio
from playwright.async_api import async_playwright

async def follow_account(username):
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        # Navigate to the account
        page = await context.new_page()
        await page.goto(f"https://x.com/{username}")
        await page.wait_for_load_state("networkidle")
        
        print(f"\n📱 Following: @{username}")
        
        # Try to find and click follow button
        try:
            # Method 1: Find by text content
            follow_buttons = page.locator('button:has-text("关注")')
            count = await follow_buttons.count()
            
            if count > 0:
                print(f"✅ Found {count} follow button(s)")
                for i in range(min(count, 1)):  # Click first one
                    btn = follow_buttons.nth(i)
                    text = await btn.inner_text()
                    print(f"  Button {i+1}: {text}")
                    await btn.click()
                    print(f"  ✅ Clicked!")
            else:
                print("❌ No follow button found")
                
                # Check if already following
                following = page.locator('button:has-text("正在关注")')
                if await following.count() > 0:
                    print("✅ Already following!")
                    
        except Exception as e:
            print(f"⚠️  Error: {e}")
        
        await asyncio.sleep(2)

async def main():
    accounts = ["GoogleAI", "DeepLearningAI", "AndrewYNg", "aigclink", "FuSheng_0306", "SchmidhuberAI"]
    
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        for username in accounts:
            print(f"\n{'='*50}")
            await follow_account(username)
        
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
