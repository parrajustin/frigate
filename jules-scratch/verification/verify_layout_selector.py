from playwright.sync_api import sync_playwright, expect
import time

def run_verification(page):
    # Navigate to the live view
    # CI has a different port
    page.goto("http://localhost:5173/live")

    # Wait for the page to load by looking for a known element
    expect(page.get_by_text("Live", exact=True)).to_be_visible(timeout=10000)

    # Find the layout selector dropdown trigger
    # The initial text is "Auto"
    layout_selector_trigger = page.get_by_role("button", name="Auto")
    expect(layout_selector_trigger).to_be_visible()

    # Click to open the dropdown
    layout_selector_trigger.click()

    # Wait for dropdown to be visible
    expect(page.get_by_role("menuitem", name="2 Columns")).to_be_visible()

    # Take a screenshot of the open dropdown
    page.screenshot(path="jules-scratch/verification/01_dropdown_open.png")

    # Click the "2 Columns" option
    page.get_by_role("menuitem", name="2 Columns").click()

    # Wait for the layout to update
    expect(page.get_by_role("button", name="2 Columns")).to_be_visible()

    # Take a screenshot of the 2-column layout
    page.screenshot(path="jules-scratch/verification/02_two_column_layout.png")

    # Now test 4 columns
    layout_selector_trigger = page.get_by_role("button", name="2 Columns")
    expect(layout_selector_trigger).to_be_visible()
    layout_selector_trigger.click()

    expect(page.get_by_role("menuitem", name="4 Columns")).to_be_visible()
    page.get_by_role("menuitem", name="4 Columns").click()

    expect(page.get_by_role("button", name="4 Columns")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/03_four_column_layout.png")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            run_verification(page)
        finally:
            browser.close()

if __name__ == "__main__":
    main()
