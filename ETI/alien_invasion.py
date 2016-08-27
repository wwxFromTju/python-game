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

    # 设置点击的按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 保存游戏状态, 将状态保存在同一个地方
    stats = GameStats(ai_settings)

    # 对应角色的初始化
    # 下面的
    ship = Ship(ai_settings, screen)
    # 子弹
    bullets = Group()
    # 上面的
    aliens = Group()
    # 记分板
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建上面的一群飘着的东西
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 不停地监听键盘输入和刷新界面
    while True:
        # 监听键盘, 做出对应的反应
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        # 判断时候在游戏中
        if stats.game_active:
            # 更新下面的位置
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新上面的
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 刷新界面
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

if __name__ == '__main__':
    run_game()