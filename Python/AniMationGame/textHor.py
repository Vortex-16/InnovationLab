from blessed import Terminal
import time

term = Terminal()
msg = "🚀 MOVING TERMINAL EFFECTS!"

with term.fullscreen():
    while True:
        for x in range(term.width - len(msg)):
            print(term.home + " " * x + msg)
            time.sleep(0.05)
