import pygame
import constants
from constants import *
import circleshape
from circleshape import *
from player import Player

def main():
	print ("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# init?
	clock = pygame.time.Clock()
	dt = 0
	# player
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	plr = Player(x,y)
	# start gameloop
	while 1==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(color="black")
		plr.draw(screen)
		dt = clock.tick(60)/1000
		print (dt)
		# last
		pygame.display.flip() 


if __name__ == "__main__":
	main()
