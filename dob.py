from datetime import datetime

expiry_input = input("Enter expiry date (YYYY-MM-DD): ")

expiry_date = datetime.strptime(expiry_input, "%Y-%m-%d").date()
today = datetime.today().date()

if expiry_date < today:
    print("Product is expired")
else:
    print("Product is not expired")
