import requests, json
from datetime import datetime

API_KEY = "9713ae41b71f0db52bfc7eb9035ef0ce"

def get_fred(series, limit=None):
    url = (
        f"https://api.stlouisfed.org/fred/series/observations"
        f"?series_id={series}&api_key={API_KEY}&file_type=json"
    )
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "observations" not in data:
            print(f"[ERREUR] API FRED pour {series} :", data.get("error_message", data))
            return {"dates": [], "values": []}

        obs = data["observations"]
        if limit:
            obs = obs[-limit:]

        dates, values = [], []
        for x in obs:
            dates.append(x["date"])
            v = x["value"]
            if v in (".", "", None):
                values.append(None)
            else:
                try:
                    values.append(float(v))
                except (ValueError, TypeError):
                    values.append(None)

        print(f"[OK] {series} — {len(dates)} points, dernier : {dates[-1] if dates else '—'}")
        return {"dates": dates, "values": values}

    except requests.RequestException as e:
        print(f"[ERREUR RÉSEAU] {series} :", e)
        return {"dates": [], "values": []}
    except Exception as e:
        print(f"[ERREUR] {series} :", e)
        return {"dates": [], "values": []}


euribor   = get_fred("IR3TIB01EZM156N")
inflation = get_fred("FPCPITOTLZGEMU")
bce       = get_fred("ECBDFR", limit=365)
oat       = get_fred("IRLTLT01FRM156N")

data = {
    "euribor":     euribor,
    "inflation":   inflation,
    "bce":         bce,
    "oat":         oat,
    "last_update": datetime.now().strftime("%Y-%m-%d %H:%M")
}

with open("data.json", "w") as f:
    json.dump(data, f, separators=(',', ':'))

print(f"\n✅ data.json mis à jour — {data['last_update']}")
