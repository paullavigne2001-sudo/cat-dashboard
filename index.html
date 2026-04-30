import requests, json
from datetime import datetime

API_KEY = "9713ae41b71f0db52bfc7eb9035ef0ce"

# Séries FRED utilisées :
# EURIBOR3MD156N  → Euribor 3 mois (taux en %)
# CP0000EZ19M086NEST → Inflation zone euro HICP (indice base 100 = 2015)
# ECBDFR          → Taux directeur BCE Deposit Facility Rate
# IRLTLT01FRM156N → OAT France 10 ans

def get_fred(series, limit=None):
    """
    Récupère les observations d'une série FRED.
    limit : nombre de derniers points à conserver (None = tout)
    """
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


# Récupération de toutes les séries
# On garde jusqu'à 30 ans de données pour permettre des vues historiques longues
euribor   = get_fred("EURIBOR3MD156N")      # mensuel → ~360 points sur 30 ans
inflation = get_fred("CP0000EZ19M086NEST")  # mensuel
bce       = get_fred("ECBDFR")              # quotidien → limité à 365 jours
oat       = get_fred("IRLTLT01FRM156N")     # mensuel

# Pour la BCE (données quotidiennes), on garde les 365 derniers jours seulement
# car afficher 30 ans de données quotidiennes serait trop lourd
bce_daily = get_fred("ECBDFR", limit=365)

data = {
    "euribor":    euribor,
    "inflation":  inflation,
    "bce":        bce_daily,
    "oat":        oat,
    "last_update": datetime.now().strftime("%Y-%m-%d %H:%M")
}

with open("data.json", "w") as f:
    json.dump(data, f, separators=(',', ':'))

print(f"\n✅ data.json mis à jour — {data['last_update']}")
