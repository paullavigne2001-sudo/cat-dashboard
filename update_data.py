import requests, json
from datetime import datetime

def get_fred(series):
    API_KEY = "9713ae41b71f0db52bfc7eb9035ef0ce"

    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series}&api_key={API_KEY}&file_type=json"

    try:
        response = requests.get(url)
        data = response.json()

        # 🔎 Vérification clé
        if "observations" not in data:
            print(f"Erreur API pour {series} :", data)
            return {"dates": [], "values": []}

        obs = data["observations"]

        dates = []
        values = []

        for x in obs[-365:]:
            dates.append(x["date"])

            if x["value"] in (".", "", None):
                values.append(None)
            else:
                try:
                    values.append(float(x["value"]))
                except:
                    values.append(None)

        return {"dates": dates, "values": values}

    except Exception as e:
        print(f"Erreur globale pour {series} :", e)
        return {"dates": [], "values": []}

data = {
    "euribor": get_fred("EURIBOR3MD156N"),
    "inflation": get_fred("CP0000EZ19M086NEST"),
    "bce": get_fred("ECBDFR"),
    "oat": get_fred("IRLTLT01FRM156N"),
    "last_update": datetime.now().strftime("%Y-%m-%d %H:%M")
}

with open("data.json","w") as f:
    json.dump(data,f)
