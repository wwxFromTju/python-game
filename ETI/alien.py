#!/usr/bin/env python
# encoding=utf-8

import pygame
from pygame.sprite import  Sprite

# 外星人class, 继承了pygame的精灵
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings =ai_settings

        self.image = pygame.image.load('images/liu.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    # 修改对应rect的位置, rect就是真正的块
    def update(self):
        # 左右移动, 根据direction来切换左右
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    # 绘图
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # 判断是否碰到边界
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
