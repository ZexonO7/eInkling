from PIL import Image, ImageDraw
from config import EINK_WIDTH, EINK_HEIGHT
from .eink import display_frame
from .cards.clock_card import draw_clock
from .cards.weather_card import draw_weather
from .cards.notes_card import draw_notes
from .cards.todos_card import draw_todos
from .utils.layout import column_layout

def render_frame():
    frame = Image.new("1", (EINK_WIDTH, EINK_HEIGHT), 1)
    draw = ImageDraw.Draw(frame)

    regions = column_layout(EINK_WIDTH, EINK_HEIGHT, [0.22, 0.78], gap=8)
    header, body = regions

    header_l, header_r = column_layout(header[2], header[3], [0.5, 0.5], gap=8, origin=(header[0], header[1]))
    draw_clock(frame, header_l)
    draw_weather(frame, header_r)

    body_l, body_r = column_layout(body[2], body[3], [0.55, 0.45], gap=8, origin=(body[0], body[1]))
    draw_notes(frame, body_l)
    draw_todos(frame, body_r)

    draw.line([(8, EINK_HEIGHT-8), (EINK_WIDTH-8, EINK_HEIGHT-8)], fill=0, width=1)
    return frame

def render_and_push():
    frame = render_frame()
    display_frame(frame)
