from PIL import ImageDraw
from .base import draw_panel, inset
from ..utils.fonts import font_regular
from ..storage import load_json

def draw_notes(img, rect):
    draw = ImageDraw.Draw(img)
    draw_panel(draw, rect, title="notes")
    x, y, w, h = inset(rect, 12)

    data = load_json("notes.json", {"items": []})
    items = data.get("items", [])[:5]

    yy = y + 8
    for it in items:
        draw.text((x, yy), f"• {it.get('text','')}", font=font_regular(20), fill=0)
        yy += 26
