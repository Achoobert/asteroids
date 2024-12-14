import pygame
import constants
from constants import *
import circleshape
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print ("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# Game State
	clock = pygame.time.Clock()
	dt = 0
	# Groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	# player
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	Player.containers = (updatable, drawable)
	plr = Player(x,y)
	# shot
	Shot.containers = (updatable, drawable, shots)
	# asteroids
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	asteroidField = AsteroidField()
	# plr = Player(x,y)
	# start gameloop
	while 1==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(color="black")
		for thing in updatable:
			thing.update(dt)
		for thing in drawable:
			thing.draw(screen)
		for thing in asteroids:
			if thing.collisionDetect(plr):
				print("Game over!")
				return
			for bullet in shots:
				if bullet.collisionDetect(thing):
					bullet.kill()
					thing.split()
		dt = clock.tick(60)/1000
		# print (dt)
		# last
		pygame.display.flip() 


if __name__ == "__main__":
	main()
