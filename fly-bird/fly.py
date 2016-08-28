#!/usr/bin/env python
# encoding=utf-8

import pygame
from pygame.sprite import Sprite

class Fly(Sprite):
    def __init__(self, settings, screen):
        super(Fly, self).__init__()

        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('image/li.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.y = self.settings.screen_height / 2
        self.rect.x = self.screen_rect.left

        # 修改对应rect的位置, rect就是真正的块

    def update_up(self):
        # 左右移动, 根据direction来切换左右
        self.rect.y -= 40

    def update_down(self):
        self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_over(self):
        return self.rect.y >= self.settings.screen_height

    def set_restart(self):
        self.rect.y = self.settings.screen_height / 2
