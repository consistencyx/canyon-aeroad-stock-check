import requests

PRODUCT_ID = "4034"
SIZE = "L"

BOT_TOKEN = "8703701255:AAHP0yakwBDuOEtU-LzzxUASkY_nHX194QY"
CHAT_ID = "402782250"

url = f"https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en/Product-Variation?pid={PRODUCT_ID}"

r = requests.get(url)

try:
    data = r.json()
except:
    print("API Antwort nicht lesbar")
    exit()

attrs = data.get("variationAttributes")

if not attrs:
    print("Keine Variationsdaten gefunden")
    exit()

for attr in attrs:
    if attr.get("id") == "frameSize":
        for v in attr.get("values", []):
            if v.get("displayValue") == SIZE and v.get("selectable"):
                requests.get(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    params={
                        "chat_id": CHAT_ID,
                        "text": "Aeroad CF SLX 7 Di2 Weiß Größe L verfügbar!"
                    }
                )
                print("Bike verfügbar")
