import pygame
import random

pygame.init()

pygame.display.set_caption("Space invaders")
icono = pygame.image.load('controller.png')
pygame.display.set_icon(icono)

background = pygame.image.load('background.png')

screen = pygame.display.set_mode((800,600))

running = True

playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 200)
enemyX_change = 4
enemyY_change = 30

def player(x, y):
	screen.blit(playerImg, (x,y))

def enemy(x, y):
	screen.blit(enemyImg, (x,y))


while running:
	screen.fill((225,16,16))
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -5
			if event.key == pygame.K_RIGHT:
				playerX_change = 5

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	enemyX += enemyX_change

	if enemyX <= 0:
		enemyX_change = 4
		enemyY += enemyY_change
	if enemyX >= 736:
		enemyX_change = -4
		enemyY += enemyY_change


	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()