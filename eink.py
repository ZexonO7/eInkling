import os
from datetime import datetime
from config import OUT_DIR, ROTATION, EINK_DRIVER

def _apply_rotation(img):
    if ROTATION in (90, 180, 270):
        return img.rotate(ROTATION, expand=True)
    return img

def _display_simulator(img):
    img = _apply_rotation(img)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(OUT_DIR, f"frame_{ts}.png")
    img.convert("1").save(path)
    print(f"[SIM] wrote {path}")

def _display_waveshare(img):
    try:
        from lib import epd4in2, epd5in83, epd7in5_V2  # adjust per your panel
    except Exception as e:
        raise RuntimeError("Waveshare libs not found — add their 'lib' folder to PYTHONPATH.") from e

    W, H = img.size
    if W in (400, 300) or H in (400, 300):
        epd = epd4in2.EPD()
    elif max(W, H) in (648, 600, 800, 480):
        epd = epd5in83.EPD()
    else:
        epd = epd7in5_V2.EPD()

    epd.init()
    try:
        img = _apply_rotation(img)
        epd.display(epd.getbuffer(img))
    finally:
        epd.sleep()

def display_frame(img):
    if EINK_DRIVER.upper() == "WAVESHARE":
        _display_waveshare(img)
    else:
        _display_simulator(img)
