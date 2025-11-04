import requests
from PIL import ImageDraw
from .base import draw_panel, inset
from ..utils.fonts import font_bold, font_regular
from config import WEATHER_API_KEY, LOCATION, UNITS

API = "https://api.openweathermap.org/data/2.5/weather"

def _fetch_weather():
    if not WEATHER_API_KEY:
        return {"temp": "--", "desc": "no key", "city": LOCATION}
    try:
        r = requests.get(API, params={
            "q": LOCATION,
            "appid": WEATHER_API_KEY,
            "units": UNITS,
        }, timeout=5)
        j = r.json()
        main = j.get("main", {})
        weather = (j.get("weather") or [{}])[0]
        return {
            "temp": round(main.get("temp", 0)),
            "desc": weather.get("description", "--"),
            "city": j.get("name", LOCATION),
        }
    except Exception:
        return {"temp": "--", "desc": "offline", "city": LOCATION}

def draw_weather(img, rect):
    draw = ImageDraw.Draw(img)
    draw_panel(draw, rect, title=None)
    x, y, w, h = inset(rect, 16)

    data = _fetch_weather()
    temp = f"{data['temp']}°" if isinstance(data['temp'], int) else f"{data['temp']}"

    draw.text((x, y), data.get("city", ""), font=font_bold(24), fill=0)
    draw.text((x, y+34), temp, font=font_bold(48), fill=0)
    draw.text((x, y+90), data.get("desc", "").lower(), font=font_regular(20), fill=0)
