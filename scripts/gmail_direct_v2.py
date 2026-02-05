#!/usr/bin/env python3
"""
Gmail Registration - Direct CDP Session with Native Execution
Uses Chrome DevTools Protocol directly via WebSocket
"""

import asyncio
import json

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌ Playwright not installed")
    exit(1)

def fill_birthday_gender():
    with sync_playwright() as p:
        # Connect directly via CDP
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        # Find the signup page
        signup_page = None
        for page in context.pages:
            if "signup" in page.url:
                signup_page = page
                break
        
        if not signup_page:
            print("❌ Signup page not found")
            return
        
        print(f"📍 Found page: {signup_page.url}")
        
        # Use native Playwright methods (not CDP bridging)
        print("\n🔧 Using native Playwright selectors...")
        
        # Wait for page to be ready
        signup_page.wait_for_load_state("domcontentloaded")
        
        # Try different selector strategies for month
        month_selectors = [
            'select[name="Month"]',
            'select#month', 
            'select[aria-label*="月"]',
            'select:below("textbox[id="day"]")'
        ]
        
        month_filled = False
        for selector in month_selectors:
            try:
                el = signup_page.locator(selector)
                if el.count() > 0:
                    print(f"✅ Found month selector: {selector}")
                    # Try select by value
                    try:
                        el.select_option("3")
                        print("✅ Selected month: 3")
                        month_filled = True
                        break
                    except:
                        pass
            except:
                continue
        
        if not month_filled:
            print("⚠️  Could not fill month via selectors")
            # Try clicking to expand dropdown
            try:
                signup_page.click('div[role="listbox"][aria-label*="月"]')
                print("✅ Clicked month dropdown")
            except:
                pass
        
        # Try gender
        gender_selectors = [
            'select[name="Gender"]',
            'select#gender'
        ]
        
        for selector in gender_selectors:
            try:
                el = signup_page.locator(selector)
                if el.count() > 0:
                    print(f"✅ Found gender selector: {selector}")
                    el.select_option("2")  # Female
                    print("✅ Selected gender: Female")
                    break
            except:
                continue
        
        # Take screenshot
        signup_page.screenshot(path="/tmp/gmail_step2_updated.png")
        print("📸 Screenshot saved: /tmp/gmail_step2_updated.png")
        
        # Try clicking Next
        try:
            signup_page.click('button:has-text("下一步")')
            print("✅ Clicked Next button")
            signup_page.wait_for_load_state("networkidle")
            print(f"📍 New URL: {signup_page.url}")
        except Exception as e:
            print(f"⚠️  Click failed: {e}")
        
        browser.close()
        print("\n✅ Script completed")

if __name__ == "__main__":
    fill_birthday_gender()
