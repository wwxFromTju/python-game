#!/usr/bin/env python
# encoding=utf-8

import sys
import pygame
from pygame.sprite import Group
from numpy import random

from settings import Settings
from pipeline import Pipeline
from fly import Fly


def start_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('fake fly bird')

    # pipeline_group = Group()

    pipeline_list = [create_pipeline(game_settings, screen, Group(), random.randint(1, 18), i) for i in range(5)]

    # create_pipeline(game_settings, screen, pipeline_group, random.randint(1, 21))

    fly = Fly(game_settings, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                fly.update_up()
        if not check_over(fly, pipeline_list):
            fly.update_down()
            screen.fill(game_settings.bg_color)
            fly.blitme()
            for pipeline_group in pipeline_list:
                check_edge(game_settings, screen, pipeline_group)
                pipeline_update(pipeline_group)
                pipeline_draw(pipeline_group)
            pygame.display.flip()


def create_pipeline(game_settins, screen, pipeline_group, num, order):

    pipeline_top = Pipeline(game_settins, screen, 'top', num * 10, order)
    pipeline_bottom = Pipeline(game_settins, screen, 'bottom', (18 - num) * 10, order)

    pipeline_group.add(pipeline_bottom)
    pipeline_group.add(pipeline_top)

    return pipeline_group


def pipeline_update(pipeline_group):
    for pipeline in pipeline_group:
        pipeline.update()


def pipeline_draw(pipeline_group):
    for pipeline in pipeline_group:
        pipeline.blitme()


def check_edge(game_settings, screen, pipeline_group):
    for pipeline in pipeline_group:
        if pipeline.check_edges():
            pipeline_group.empty()
            create_pipeline(game_settings, screen, pipeline_group, random.randint(1, 21), 0)


def check_over(fly, pipeline_list):
    for pipeline_group in pipeline_list:
        collisions =pygame.sprite.spritecollide(fly, pipeline_group, False)
        if fly.check_over():
            fly.set_restart()
        if collisions:
            return True


if __name__ == '__main__':
    start_game()
