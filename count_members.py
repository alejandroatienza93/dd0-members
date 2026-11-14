import json
import os
import urllib.request
from datetime import datetime, timezone

HEADERS = {
    "Authorization": f"Bearer {os.environ['WHOP_API_KEY']}",
    "Accept": "application/json",
    "Api-Version-Date": "2026-11-04",
}


def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS)))


# API v1 (v2 se apaga el 13-nov-2026). v1 no tiene valid=true: en un producto de pago
# unico, los miembros con acceso son status=completed (32 = 32 con v2 el 4-nov-2026).
members = get(
    "https://api.whop.com/api/v1/memberships"
    "?product_id=prod_4owe4MnXDBpDd&status=completed&first=0&include_total_count=true"
)["page_info"]["total_count"]

stock = get("https://api.whop.com/api/v1/variants/plan_RH6r1KXrRvKra").get("stock")

with open("members.json", "w") as f:
    json.dump(
        {
            "count": members,
            "stock": stock,
            "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        },
        f,
    )
print(f"members: {members} | stock: {stock}")
