import json
import os
import urllib.request
from datetime import datetime, timezone

HEADERS = {
    "Authorization": f"Bearer {os.environ['WHOP_API_KEY']}",
    "Accept": "application/json",
}


def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS)))


members = get(
    "https://api.whop.com/api/v2/memberships"
    "?product_id=prod_4owe4MnXDBpDd&valid=true&per=100"
)["pagination"]["total_count"]

stock = get("https://api.whop.com/api/v2/plans/plan_RH6r1KXrRvKra").get("stock")

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
