from PIL import ImageDraw
from datetime import datetime
from .base import draw_panel, inset
from ..utils.fonts import font_bold, font_regular

def draw_clock(img, rect):
    draw = ImageDraw.Draw(img)
    draw_panel(draw, rect, title=None)
    x, y, w, h = inset(rect, 16)

    now = datetime.now()
    time_s = now.strftime("%H:%M")
    date_s = now.strftime("%a, %d %b %Y")

    draw.text((x, y), time_s, font=font_bold(56), fill=0)
    draw.text((x, y+64), date_s, font=font_regular(22), fill=0)
