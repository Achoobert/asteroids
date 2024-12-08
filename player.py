import circleshape
from circleshape import *
import constants
from constants import PLAYER_RADIUS

class Player(CircleShape):
   def __init__(self,x,y):
      super().__init__(x,y,PLAYER_RADIUS) # pass player radius
      self.rotation = 0
      pass
   # in the player class
   def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
   
   def draw(self, screen):
      # The screen object
      # A color (use "white")
      # A list of points (use self.triangle() that we provided for you)
      # A line width (use 2)
      pygame.draw.polygon(
         screen,
         "white",
         self.triangle(),
         2
      )
      pass
