import requests

PRODUCT_ID = "4034"
SIZE = "L"
COLOR = "R107_P01"

BOT_TOKEN = "8703701255:AAHP0yakwBDuOEtU-LzzxUASkY_nHX194QY"
CHAT_ID = "402782250"

url = f"https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en/Product-Variation?pid={PRODUCT_ID}"

available = False

try:
    r = requests.get(url)
    data = r.json()

    attrs = data.get("variationAttributes", [])

    size_ok = False
    color_ok = False

    for attr in attrs:

        if attr.get("id") == "frameSize":
            for v in attr.get("values", []):
                if v.get("displayValue") == SIZE and v.get("selectable"):
                    size_ok = True

        if attr.get("id") == "color":
            for v in attr.get("values", []):
                if v.get("value") == COLOR and v.get("selectable"):
                    color_ok = True

    if size_ok and color_ok:
        available = True

except Exception as e:
    message = f"Canyon Check Fehler: {e}"

if available:
    message = "Aeroad CF SLX 7 Di2 Weiß Größe L: VERFÜGBAR"
else:
    message = "Aeroad CF SLX 7 Di2 Weiß Größe L: NICHT verfügbar"

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": message
    }
)
