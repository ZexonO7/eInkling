# eInking

a calm digital paper project built on a raspberry pi and a 5-inch e-ink display.  
it’s meant to sit quietly on your desk and show you the small things — notes, todos, weather, and time.  
no color. no movement. just slow, clean tech that feels like paper but thinks like code.

---

## what it is

eInking runs a flask app on the pi that builds a simple dashboard.  
each refresh, it draws “cards” for weather, notes, todos, and the clock using pillow.  
the image is then pushed to the e-ink display (or saved as a png in simulator mode).  
it updates quietly in the background — no screens to unlock, no distractions.  

inside, it’s made of small focused pieces:
- `renderer.py` — builds the full frame from all cards  
- `eink.py` — handles display output (waveshare or simulator)  
- `app.py` — flask web panel for editing notes and todos  
- `storage.py` — saves everything as json files  
- `cards/` — small scripts that draw each element (clock, weather, notes, todos)

---

## how it feels

the project’s built to be calm.  
every part loads at its own pace, refreshes quietly, and doesn’t need constant input.  
it’s a mix of analog design and modern hardware — a notebook made of pixels.  

the layout and fonts are handmade, spacing tuned so it feels like a printed page.  
each card draws with soft margins and balanced whitespace, no clutter or heavy UI.

---

## how it works

the pi runs a simple refresh loop:
1. fetch weather and notes data  
2. render all cards into one monochrome image  
3. send image to the display  
4. sleep until the next refresh  

the web interface runs locally on the same pi.  
it lets you add or edit notes, mark todos done, and trigger manual refreshes.  
everything stays local — no cloud, no database, no tracking.

---

## what it’s built with

- **python 3.11+**  
- **flask** for the local web interface  
- **pillow** for image rendering  
- **requests** for pulling weather data  
- **dotenv** for configuration  
- **waveshare python driver** for e-ink panels (or simulator mode)

---

## current goal

finish the 3d-printed pi mount and internal frame  
get the first prototype running fully on hardware  
and keep the design warm — more craft than code  

---

**eInking** is a small experiment in slow tech.  
something that doesn’t buzz or blink — it just exists quietly on your desk 🩶
