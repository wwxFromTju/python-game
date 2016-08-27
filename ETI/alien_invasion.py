#!/usr/bin/env python
# encoding=utf-8

import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf
from game_stats import GameStats


def run_game():
    # pygame初始化
    pygame.init()

    # 将配置都放在一个文件
    ai_settings = Settings()
    # 设置窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置标题
    pygame.display.set_caption('Liu and Li')

    play_button = Button(ai_settings, screen, 'Play')

    # 保存游戏状态
    stats = GameStats(ai_settings)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()