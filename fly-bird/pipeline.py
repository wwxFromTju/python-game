#!/usr/bin/env python
# encoding=utf-8

import pygame
from pygame.sprite import Sprite

class Pipeline(Sprite):
    def __init__(self, settings, screen, direction, change, order):
        super(Pipeline, self).__init__()

        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('image/pipe-green-' + direction + '.jpg')

        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.right + order * 250

        if direction == 'bottom':
            self.rect.bottom = self.screen_rect.bottom + 300 - change
        else:
            self.rect.top = self.screen_rect.top - 300 + change

        self.x = int(self.rect.x)

    def update(self):
        self.x += self.settings.pipeline_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        return self.rect.left <= 0
