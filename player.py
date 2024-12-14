import circleshape
from circleshape import *
import constants
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
   def __init__(self,x,y):
      super().__init__(x,y,PLAYER_RADIUS) # pass player radius
      self.rotation = 0
      self.cooldown = PLAYER_SHOOT_COOLDOWN
      pass
   def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
   def draw(self, screen):
      pygame.draw.polygon(
         screen,
         "white",
         self.triangle(),
         2
      )
      pass
   def rotate(self, dt, direction):
      if direction == "left":
         self.rotation += PLAYER_TURN_SPEED * dt
      elif direction == "right":
         self.rotation -= PLAYER_TURN_SPEED * dt
      pass
   def update(self, dt):
      self.cooldown -= dt
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
         self.rotate(dt, "left")
      if keys[pygame.K_d]:
         self.rotate(dt, "right")
      if keys[pygame.K_w]:
         self.move(dt)
      if keys[pygame.K_s]:
         self.move(-dt)
      if keys[pygame.K_SPACE]:
         if self.cooldown <= 0:
            self.shoot()
            self.cooldown = PLAYER_SHOOT_COOLDOWN
         else:
            print(self.cooldown)
   def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt
      pass
   def shoot(self):
      # print("trying To Shoot")

      # velocity = edge[0] * speed
      # velocity = velocity.rotate(random.randint(-30, 30))
      # position = edge[1](random.uniform(0, 1))
      #  def spawn(self, radius, position, velocity):
      
      shot = Shot(self.position.x, self.position.y)
      # pygame.Vector2(0, 1).rotate(self.rotation)
      shot.rotate(self.rotation)
      shot.velocity = shot.velocity * PLAYER_SHOOT_SPEED
      pass