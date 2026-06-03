💱 Currency Converter (Python API Project)

A simple Python-based Currency Converter that uses the Frankfurter API to convert one currency into another in real time.

FEATURES:
Convert any currency using live exchange rates
Uses free and reliable API (Frankfurter API)
Simple command-line interface
Supports all major currencies (USD, INR, EUR, GBP, etc.)

  TECHNOLOGY USED:
Python 
Requests library 
Frankfurter Exchange Rate API

 INSTALLATION:
1. Clone the repository
git clone https://github.com/your-username/currency-converter.git
2. Go to project folder
cd currency-converter
3. Install required library
pip install requests

HOW TO RUN :
python main.py
EXAMPLE: 
From currency (e.g. USD): USD
To currency (e.g. INR): INR
Amount: 10
Output:
💱 10 USD = 832.50 INR

HOW ITS WORK:
User enters source currency, target currency, and amount
Program sends request to:
https://api.frankfurter.app/latest
API returns live exchange rates
Program calculates and displays converted value.

POSSIBLE ERROR:
Invalid currency code → will not return conversion
No internet connection → API request fails
API downtime → response error

AUTHOR
Rutuja Gawade
