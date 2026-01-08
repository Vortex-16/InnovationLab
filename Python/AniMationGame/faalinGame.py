from asciimatics.screen import Screen
from random import randint
import time

def game(screen):
    width = screen.width
    height = screen.height
    player_x = width // 2
    player_y = height - 2

    enemies = []

    while True:
        screen.clear()

        # Add a new enemy randomly
        if randint(0, 5) == 0:
            enemies.append([randint(0, width - 1), 0])

        # Move enemies down
        for enemy in enemies:
            enemy[1] += 1
            if enemy[1] < height:
                screen.print_at('X', enemy[0], enemy[1], colour=Screen.COLOUR_RED)

        # Remove enemies that went off-screen
        enemies = [e for e in enemies if e[1] < height]

        # Draw player
        screen.print_at('A', player_x, player_y, colour=Screen.COLOUR_GREEN)

        screen.refresh()
        time.sleep(0.05)

        # Check collision
        for e in enemies:
            if e[0] == player_x and e[1] == player_y:
                screen.clear()
                screen.print_at("GAME OVER!", width//2 - 5, height//2, colour=Screen.COLOUR_YELLOW)
                screen.refresh()
                time.sleep(2)
                return

        # Player input
        ev = screen.get_key()
        if ev in (ord('q'), ord('Q')):
            break
        elif ev in (Screen.KEY_LEFT, ord('a'), ord('A')):
            player_x = max(0, player_x - 1)
        elif ev in (Screen.KEY_RIGHT, ord('d'), ord('D')):
            player_x = min(width - 1, player_x + 1)

Screen.wrapper(game)