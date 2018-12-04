#-*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Aline Invasion")
    # 创建一艘飞船,一个外星人编组和一个子弹编组
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    # 创建外星人群
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            game_functions.update_aliens(ai_settings, stats, screen, ship,
                                        aliens, bullets)
            game_functions.update_bullets(ai_settings, screen, ship,
                                        aliens, bullets)
        game_functions.update_screen(ai_settings, screen, ship, aliens,
                                        bullets)

run_game()
