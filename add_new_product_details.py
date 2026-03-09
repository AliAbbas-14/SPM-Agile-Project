import requests
import json

# Jira credentials
JIRA_URL = "https://your-domain.atlassian.net"
EMAIL = "your-email@example.com"
API_TOKEN = "your-api-token"

# API endpoint
url = f"{JIRA_URL}/rest/api/3/issue"

# Headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def add_new_product(name, price, description):

    data = {
        "fields": {
            "project": {
                "key": "PROJ"   # Replace with your Jira project key
            },
            "summary": f"New Product: {name}",
            "description": description,
            "issuetype": {
                "name": "Task"
            }
        }
    }

    response = requests.post(
        url,
        headers=headers,
        auth=(EMAIL, API_TOKEN),
        data=json.dumps(data)
    )

    if response.status_code == 201:
        print("Product added successfully in Jira!")
    else:
        print("Error:", response.text)


# Example usage
if __name__ == "__main__":
    product_name = input("Enter Product Name: ")
    product_price = input("Enter Product Price: ")
    product_description = input("Enter Product Description: ")

    add_new_product(product_name, product_price, product_description)
