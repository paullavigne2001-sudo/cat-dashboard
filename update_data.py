import requests, json
from datetime import datetime

def get_fred(series):
    API_KEY = "9713ae41b71f0db52bfc7eb9035ef0ce"
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series}&api_key={API_KEY}&file_type=json"
    r = requests.get(url).json()["observations"]
    dates = [x["date"] for x in r][-365:]
    values = [float(x["value"]) if x["value"]!="." else None for x in r][-365:]
    return {"dates":dates,"values":values}

data = {
    "euribor": get_fred("EURIBOR3MD156N"),
    "inflation": get_fred("CP0000EZ19M086NEST"),
    "bce": get_fred("ECBDFR"),
    "oat": get_fred("IRLTLT01FRM156N"),
    "last_update": datetime.now().strftime("%Y-%m-%d %H:%M")
}

with open("data.json","w") as f:
    json.dump(data,f)
