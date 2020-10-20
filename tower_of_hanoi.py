import pygame
import game_objects
import settings


def main():
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screen.fill(settings.white)
    game_objects.game.run()


if __name__ == "__main__":
    main()
