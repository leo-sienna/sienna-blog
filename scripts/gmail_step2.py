#!/usr/bin/env python3
"""
Gmail Registration - Step 2: Birthday and Gender
"""

import asyncio
from playwright.async_api import async_playwright

async def step2_birthday_gender():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        # Find signup page
        signup_page = None
        for page in context.pages:
            if "signup" in page.url:
                signup_page = page
                break
        
        if signup_page:
            print(f"📍 Current URL: {signup_page.url}")
            
            # Fill birthday
            print("\n🎂 Step 2: Filling birthday...")
            await signup_page.wait_for_load_state("networkidle")
            
            # Fill year
            year_input = signup_page.locator('input[id="year"]')
            await year_input.fill("1999")
            print("✅ Filled year: 1999")
            
            # Select month
            print("\n📅 Selecting month...")
            month_dropdown = signup_page.locator('select[id="month"]')
            await month_dropdown.select_option("3")  # March
            print("✅ Selected month: March")
            
            # Fill day
            print("\n📆 Filling day...")
            day_input = signup_page.locator('input[id="day"]')
            await day_input.fill("15")
            print("✅ Filled day: 15")
            
            # Select gender
            print("\n👤 Selecting gender...")
            gender_dropdown = signup_page.locator('select[id="gender"]')
            await gender_dropdown.select_option("2")  # Female
            print("✅ Selected gender: Female")
            
            # Click Next
            print("\n➡️  Clicking Next...")
            next_btn = signup_page.locator('button:has-text("下一步")')
            await next_btn.click()
            await signup_page.wait_for_load_state("networkidle")
            print("✅ Clicked Next")
            
            print(f"\n📍 Current URL: {signup_page.url}")
            print("\n🎉 Step 2 complete! Moving to Step 3...")
            
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(step2_birthday_gender())
