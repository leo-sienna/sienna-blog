#!/usr/bin/env python3
"""
Gmail Registration - Direct DOM manipulation via CDP
Bypass Playwright's select limitations
"""

import asyncio
import json
from playwright.async_api import async_playwright

async def dom_manipulation():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:18800")
        context = browser.contexts[0]
        
        for page in context.pages:
            if "signup" in page.url:
                print(f"🎯 Target page: {page.url}")
                
                # ===== Method 1: Direct DOM via page.evaluate() =====
                print("\n🔧 Method 1: Direct DOM manipulation...")
                
                result = await page.evaluate("""() => {
                    // Set month dropdown value
                    const monthSelect = document.querySelector('select#month, select[name="Month"]');
                    if (monthSelect) {
                        monthSelect.value = '3';  // March
                        monthSelect.dispatchEvent(new Event('change', { bubbles: true }));
                        console.log('✅ Month set to: ' + monthSelect.value);
                    }
                    
                    // Set gender dropdown value
                    const genderSelect = document.querySelector('select#gender, select[name="Gender"]');
                    if (genderSelect) {
                        genderSelect.value = '2';  // Female
                        genderSelect.dispatchEvent(new Event('change', { bubbles: true }));
                        console.log('✅ Gender set to: ' + genderSelect.value);
                    }
                    
                    return {
                        month: monthSelect?.value || 'NOT FOUND',
                        gender: genderSelect?.value || 'NOT FOUND'
                    };
                }""")
                
                print(f"📊 Result: {json.dumps(result, indent=2)}")
                
                # ===== Method 2: Click and type if needed =====
                print("\n🔧 Method 2: Alternative approach...")
                
                # Just verify the page state
                await page.wait_for_timeout(1000)
                
                # Check current URL
                print(f"📍 Current URL: {page.url}")
                
                # Try clicking Next button
                print("\n➡️  Attempting to click Next...")
                
                next_js = """() => {
                    const nextBtn = document.querySelector('button:has-text("下一步")');
                    if (nextBtn) {
                        nextBtn.click();
                        return 'CLICKED';
                    }
                    return 'NOT FOUND';
                }"""
                
                click_result = await page.evaluate(next_js)
                print(f"🔘 Click result: {click_result}")
                
                await page.wait_for_load_state("networkidle")
                print(f"📍 After click URL: {page.url}")
                
                break
        
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(dom_manipulation())
