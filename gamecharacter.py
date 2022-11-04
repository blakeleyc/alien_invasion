import pygame


class Cow:
    """A class to manage the cow."""

    def __init__(self, bb_game):
        """Initialize the bird and set its starting position."""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        # Load the bird image and get its rect.
        #   Bird image from: https://opengameart.org/content/game-character-blue-flappy-bird-sprite-sheets
        self.image = pygame.image.load('images/cutecow.bmp')
        self.rect = self.image.get_rect()

        # Start each new bird at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the cow at its current location."""
        self.screen.blit(self.image, self.rect)