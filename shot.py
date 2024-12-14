import circleshape
from circleshape import *
import constants
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
   def __init__(self,x,y):
      print("Making New Shot")
      self.radius = SHOT_RADIUS
      super().__init__(x,y,self.radius) # pass player radius
      self.rotation = 0

      self.velocity = pygame.Vector2(0, 1)# PLAYER_SHOOT_SPEED
      # self.velocity = self.velocity.rotate(random.randint(-30, 30))
      pass
   def draw(self, screen):
      # print("Drawing")
      pygame.draw.circle(
         screen,
         "white",
         self.position,
         self.radius,
         2
      )
      pass

   def rotate(self, inputRotation):
      self.rotation = inputRotation
      self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
      print("Rotating Shot", self.rotation)
      pass
   def update(self, dt):
      self.move(dt)
      pass
   def move(self, dt):
      # forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += self.velocity * dt
      pass