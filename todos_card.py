from PIL import ImageDraw
from .base import draw_panel, inset
from ..utils.fonts import font_regular
from ..storage import load_json

def draw_todos(img, rect):
    draw = ImageDraw.Draw(img)
    draw_panel(draw, rect, title="todos")
    x, y, w, h = inset(rect, 12)

    data = load_json("todos.json", {"items": []})
    items = data.get("items", [])[:7]

    yy = y + 8
    for it in items:
        box = "[x]" if it.get("done") else "[ ]"
        draw.text((x, yy), f"{box} {it.get('text','')}", font=font_regular(20), fill=0)
        yy += 26
