import requests

PRODUCT_ID = "4034"
SIZE = "L"
COLOR = "R107_P01"

BOT_TOKEN = "8703701255:AAHP0yakwBDuOEtU-LzzxUASkY_nHX194QY"
CHAT_ID = "402782250"

BUY_LINK = "https://www.canyon.com/de-de/rennrad/aero-rennrad/aeroad/cf-slx/aeroad-cf-slx-7-di2/4034.html?dwvar_4034_pv_rahmenfarbe=R107_P01&dwvar_4034_pv_rahmengroesse=L"

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
    print("API Fehler:", e)

if available:
    message = f"""🚨 AEROAD RESTOCK 🚨

Aeroad CF SLX 7 Di2 Weiß Größe L ist verfügbar!

Direkt kaufen:
{BUY_LINK}
"""

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
