import requests

PRODUCT_ID = "4034"
COLOR = "R107_P01"
SIZE = "L"

BOT_TOKEN = "8703701255:AAHP0yakwBDuOEtU-LzzxUASkY_nHX194QY"
CHAT_ID = "402782250"

url = f"https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en/Product-Variation?pid={PRODUCT_ID}"

r = requests.get(url)
data = r.json()

size_available = False

for attr in data["variationAttributes"]:
    if attr["id"] == "frameSize":
        for v in attr["values"]:
            if v["displayValue"] == SIZE and v["selectable"]:
                size_available = True

if size_available:
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": "Aeroad CF SLX 7 Di2 weiß Größe L verfügbar"
        }
    )
