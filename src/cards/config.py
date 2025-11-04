import os
from dotenv import load_dotenv

load_dotenv()

EINK_DRIVER = os.getenv("EINK_DRIVER", "SIMULATOR")
EINK_WIDTH = int(os.getenv("EINK_WIDTH", 800))
EINK_HEIGHT = int(os.getenv("EINK_HEIGHT", 480))
ROTATION = int(os.getenv("ROTATION", 0))

BIND_HOST = os.getenv("BIND_HOST", "0.0.0.0")
BIND_PORT = int(os.getenv("BIND_PORT", 5000))

REFRESH_MINUTES = int(os.getenv("REFRESH_MINUTES", 30))

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
LOCATION = os.getenv("LOCATION", "Delhi,IN")
UNITS = os.getenv("UNITS", "metric")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUT_DIR = os.path.join(BASE_DIR, "out")
FONTS_DIR = os.path.join(BASE_DIR, "src", "utils", "fonts")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)
