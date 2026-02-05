#!/usr/bin/env python3
"""
Gmail Registration - Step 2 continued: Month, Day, Gender
"""

import asyncio
from playwright.async_api import async_playwright

async def complete_step2():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        for page in context.pages:
            if "signup" in page.url:
                print(f"📍 Processing: {page.url}")
                
                # Fill month (select by visible text)
                print("\n📅 Selecting month...")
                try:
                    month_select = page.locator('select#month, select[name="Month"], select[aria-label*="月"]')
                    if await month_select.count() > 0:
                        await month_select.select_option(label="三月")
                        print("✅ Selected month: March")
                except Exception as e:
                    print(f"⚠️  Month selection: {e}")
                
                # Fill day
                print("\n📆 Filling day...")
                try:
                    day_input = page.locator('input#day, input[name="Day"]')
                    if await day_input.count() > 0:
                        await day_input.fill("15")
                        print("✅ Filled day: 15")
                except Exception as e:
                    print(f"⚠️  Day input: {e}")
                
                # Select gender (Female)
                print("\n👤 Selecting gender...")
                try:
                    gender_select = page.locator('select#gender, select[name="Gender"]')
                    if await gender_select.count() > 0:
                        await gender_select.select_option("2")  # Female
                        print("✅ Selected gender: Female")
                except Exception as e:
                    print(f"⚠️  Gender selection: {e}")
                
                # Click Next
                print("\n➡️  Clicking Next...")
                try:
                    next_btn = page.locator('button:has-text("下一步")')
                    if await next_btn.count() > 0:
                        await next_btn.click()
                        await page.wait_for_load_state("networkidle")
                        print("✅ Clicked Next")
                except Exception as e:
                    print(f"⚠️  Next button: {e}")
                
                print(f"\n📍 Current URL: {page.url}")
                break
        
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(complete_step2())
