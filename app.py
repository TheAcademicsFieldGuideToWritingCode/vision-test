import sys
import time
import pygame
import argparse
from typing import Tuple


def main(interval: float, duration: float, color: Tuple[int, int, int], radius: int) -> None:
    """
    Main function to run the graphical application.

    :param interval: Time in seconds between each appearance of the colored dot.
    :param duration: Duration in seconds of each appearance of the colored dot.
    :param color: Color of the dot (red, green, or blue).
    :param radius: Radius of the dot in pixels.
    """
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    screen_width, screen_height = screen.get_size()
    dot_position = (screen_width // 2, screen_height // 2)

    running = True
    dot_start_time = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        current_time = time.time()

        if dot_start_time is None or current_time - dot_start_time >= interval:
            dot_start_time = current_time
            dot_end_time = dot_start_time + duration

        screen.fill((0, 0, 0))

        if dot_start_time <= current_time <= dot_end_time:
            pygame.draw.circle(screen, color, dot_position, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graphical application to display a colored dot")
    parser.add_argument("interval", type=float, help="Time in seconds between each appearance of the colored dot")
    parser.add_argument("duration", type=float, help="Duration in seconds of each appearance of the colored dot")
    parser.add_argument("color", type=str, choices=["red", "green", "blue"], help="Color of the dot (red, green, or blue)")
    parser.add_argument("radius", type=int, help="Radius of the dot in pixels")

    args = parser.parse_args()

    color_map = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}

    main(args.interval, args.duration, color_map[args.color], args.radius)