# eInking

a calm digital paper project built on a raspberry pi and a 5-inch e-ink display.  
it’s meant to sit quietly on your desk and show you the small things — notes, todos, weather, and time.  
no color. no movement. just slow, clean tech that feels like paper but thinks like code.

<img width="1536" height="1024" alt="4a976584-c3ac-41a3-883a-c59129e36dc1" src="https://github.com/user-attachments/assets/a954a3a1-119a-42c3-98cc-45f2fb28af9e" />

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

<img width="293" height="290" alt="image" src="https://github.com/user-attachments/assets/60b1fff2-0bd5-48ae-ab8d-7747c0477f0c" />

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

finish the 3d-printed mount and internal frame  
get the first prototype running fully on hardware  
and keep the design warm — more craft than code 

<img width="1757" height="953" alt="Screenshot 2025-11-05 005258" src="https://github.com/user-attachments/assets/372f77f5-2ae7-45b7-ad55-f6fb4f7946df" />


---

**eInkling** is a experiment in slow tech.  
something that doesn’t buzz or blink — it just exists quietly on your desk 🩶

<img width="1704" height="923" alt="Screenshot 2025-11-05 042806" src="https://github.com/user-attachments/assets/e698bf03-64a4-4de7-bc95-aa071088c1ba" />

