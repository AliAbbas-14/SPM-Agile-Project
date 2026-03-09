using namespace std
import datetime

# Sample product database (temporary)
products = [
    {"name": "Laptop", "price": 1200, "stock": 10, "date_added": "2026-03-08"},
    {"name": "Mouse", "price": 25, "stock": 50, "date_added": "2026-03-09"},
    {"name": "Keyboard", "price": 45, "stock": 5, "date_added": "2026-03-09"}
]

def dashboard_overview():

    total_products = len(products)

    today = str(datetime.date.today())
    products_added_today = 0
    low_stock = 0

    for product in products:
        if product["date_added"] == today:
            products_added_today += 1

        if product["stock"] < 10:
            low_stock += 1

    print("\n------ DASHBOARD OVERVIEW ------")
    print("Total Products:", total_products)
    print("Products Added Today:", products_added_today)
    print("Low Stock Products:", low_stock)
    print("--------------------------------")

dashboard_overview()
