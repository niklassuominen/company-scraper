import azure.functions as func
from playwright.sync_api import sync_playwright
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    company_name = req.params.get('company_name')
    if not company_name:
        return func.HttpResponse(
            "Please pass a company_name on the query string",
            status_code=400
        )

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'https://www.finder.fi/search?search={company_name}')

        # This is a placeholder. You may need to adjust selectors based on actual page structure.
        company_info = {
            'name': 'Example Company',
            'revenue': '10M €',
            'profit': '1M €',
            'employees': '50',
            'revenue_per_employee': '200k €',
            'industry': 'Technology',
            'founded_year': '2000',
            'address': 'Example Street 1, Helsinki'
        }

        browser.close()

    return func.HttpResponse(
        json.dumps(company_info),
        mimetype="application/json"
    )
