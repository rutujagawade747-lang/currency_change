import requests

def currencyconverter(fromcurrency, tocurrency, amount):
    url = "https://api.frankfurter.app/latest"
    
    params = {
        "from": fromcurrency.upper(),
        "to": tocurrency.upper(),
        "amount": amount
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
         #200 → ✅ Success (everything is fine, server gave proper response).
        # 404 → ❌ Not Found (URL doesn’t exist).
        # 500 → ❌ Internal Server Error (problem on the server side).
        # 403 → ❌ Forbidden (you are not allowed to access this).
        data = response.json()
        converted = data['rates'][tocurrency.upper()]
        print(f"💱 {amount} {fromcurrency.upper()} = {converted:.2f} {tocurrency.upper()}")  #.2f meas upto 2 vales after decimal
    else:
        print("Error fetching exchange rates.")


fromcurrency = input("From currency (e.g. USD): ")
tocurrency = input("To currency (e.g. INR): ")
amount = float(input("Amount: "))

currencyconverter(fromcurrency, tocurrency, amount)
