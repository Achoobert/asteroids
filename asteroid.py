import circleshape
from circleshape import *
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
   def __init__(self,x,y,radius):
      super().__init__(x,y,radius) # pass player radius
      self.rotation = 0
      pass
   def draw(self, screen):
      pygame.draw.circle(
         screen,
         "white",
         self.position,
         self.radius,
         2
      )
      pass
   def rotate(self, dt):
      pass
   def update(self, dt):
      self.move(dt)
      pass
   def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += self.velocity * dt
      pass
   def split(self):
      self.kill()
      newSize = self.radius-ASTEROID_MIN_RADIUS
      if newSize >= ASTEROID_MIN_RADIUS:
         newDirection = random.uniform(20,50)
         self.velocity = self.velocity * 1.2
         newVel1 = self.velocity.rotate(self.rotation+newDirection)
         newVel2 = self.velocity.rotate(self.rotation-newDirection)
         self.spawn(self.position.x, self.position.y, newVel1, newSize)
         self.spawn(self.position.x, self.position.y, newVel2, newSize)
   def spawn(self, positionX,positionY, velocity, radius):
      print("Spawning child asteroid")
      asteroid = Asteroid(positionX, positionY, radius)
      asteroid.velocity = velocity