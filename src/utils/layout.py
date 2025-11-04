def column_layout(W, H, fractions, gap=0, origin=(0, 0)):
    """Split a rectangle into horizontal columns based on fractions.
    Returns list of rects (x, y, w, h). Origin moves the top-left.
    """
    ox, oy = origin
    widths = [int(W * f) for f in fractions]
    rem = W - sum(widths)
    widths[-1] += rem

    rects = []
    x = ox
    for w in widths:
        rects.append((x, oy, w, H))
        x += w + gap
    return rects
