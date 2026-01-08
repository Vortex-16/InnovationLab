from asciimatics.screen import Screen
import time

def demo(screen):
    while True:
        screen.clear()
        screen.print_at("🚀 SPACE TERMINAL!", 10, 10)
        screen.refresh()
        time.sleep(0.1)

Screen.wrapper(demo)
