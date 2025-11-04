from PIL import ImageDraw

def inset(rect, pad=8):
    x, y, w, h = rect
    return (x+pad, y+pad, w-2*pad, h-2*pad)

def draw_panel(draw: ImageDraw.ImageDraw, rect, title=None):
    x, y, w, h = rect
    draw.rectangle([x, y, x+w, y+h], outline=0, width=1)
    if title:
        draw.text((x+10, y+6), title, fill=0)
