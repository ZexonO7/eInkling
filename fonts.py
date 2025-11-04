from PIL import ImageFont

def _try(paths, size):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

_DEJAVU = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

def font_regular(size):
    return _try([_DEJAVU[0]], size)

def font_bold(size):
    return _try([_DEJAVU[1]], size)
