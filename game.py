# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

SCREEN_WIDTH = 384
SCREEN_HEIGHT = 640

#初始化游戏
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('')

#绘制背景
background = pygame.image.load('resources/image/background.png')
#绘制飞机
plane_img = pygame.image.load('resources/image/shoot.png')
player_rect = pygame.Rect(0,99,102,106)
player = plane_img.subsurface(player_rect)
player_pos = [150,450]

while True:
	screen.fill(0)
	screen.blit(background, (0,0))
	key_press = pygame.key.get_pressed()
	if key_press[K_UP]:
		player_pos[1] -= 3
	if key_press[K_DOWN]:
		player_pos[1] += 3
	if key_press[K_LEFT]:
		player_pos[0] -= 3
	if key_press[K_RIGHT]:
		player_pos[0] += 3
	screen.blit(player,player_pos)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
