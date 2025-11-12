# eInking

einking is a calm digital paper built with an esp32 and a 4.2 inch e ink display
it sits quietly on your desk or a wall ig.. and shows what matters most
time, weather, notes and small things that make the day feel softer
no bright light no sounds no rush just still quiet tech

it runs on the esp32
connects to wifi fetches data draws it on the e ink screen and then rests again
it only wakes up when it needs to
every half hour or when you press one of the buttons on the side

<img width="1536" height="1024" alt="4a976584-c3ac-41a3-883a-c59129e36dc1" src="https://github.com/user-attachments/assets/a954a3a1-119a-42c3-98cc-45f2fb28af9e" />

the device has two buttons
one for a manual refresh
and one for cycling through quotes or notes
simple physical control that makes it feel more alive but still calm

it runs on a small 4.2v li ion battery
no cables hanging off just a quiet little screen that breathes information slowly

<img width="1840" height="935" alt="Screenshot 2025-11-09 174221" src="https://github.com/user-attachments/assets/eb9f9204-a420-4837-8c37-40eb1f780a09" />

the case is like 3 piece
modeled in onshape with soft edges and a smooth royal green finish
the display sits flush in the front the esp board behind it the battery in a pocket at the back
everythin fits neatly like it was always meant to be there

inside it uses gxepd2 for the display wifi and httpclient for connection and arduinojson for parsing data
it fetches weather notes and updates them as a simple black and white layout
the whole thing stays efficient with deep sleep cycles keeping it calm even in code

<img width="1844" height="940" alt="Screenshot 2025-11-09 165623" src="https://github.com/user-attachments/assets/d88c1ed2-9e0e-4ea4-b9f8-5dfa1ec01dce" />

the repo holds everythin
the code the 3d files the logs and all the assets
it’s organized and complete ready for anyone who wants to build it

einking started as an idea for quiet tech
now it’s something real that lives on a desk
soft slow and deliberate 

<img width="279" height="941" alt="image" src="https://github.com/user-attachments/assets/0af34e49-6e2e-4bf0-a172-cf6265caac43" />

figuring out the cost for einking took longer than building half the project
the first few versions were too expensive the raspberry pi setup alone pushed it past a hundred dollars and it didn’t feel right
this project was never meant to be a high end gadget it was meant to be quiet affordable and personal
so every part had to earn its place

the esp32 changed everything
switching from the pi to the esp brought the cost down by more than half
after that it was all about small careful choices
a simpler printed case instead of a carved frame
a smaller e ink display that still looked crisp
and using the esp’s internal storage instead of adding an sd card
each change trimmed the cost a little more

right now the full build sits just under fifty dollars
that includes the esp32 the display the battery the buttons and the printed case
it took hours of research comparing parts measuring dimensions and balancing what to keep and what to let go

<img width="1222" height="244" alt="Screenshot 2025-11-12 150700" src="https://github.com/user-attachments/assets/e71692f6-5967-46df-9cc5-abc557f5bdee" />


