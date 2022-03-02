import requests
import xmltodict
import json
import decimal

def currency_rates(curr_key):
    try:
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        decoded_response = r.content.decode('windows-1251')
        response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))

        for el in response_json.get("ValCurs").get("Valute"):
            if el.get("CharCode").upper() == curr_key.upper():
                return decimal.Decimal(el.get("Value").replace(',', '.'))
    except Exception:
        return None
print(currency_rates("EUR"))
print(currency_rates("usd"))
print(currency_rates("аа"))