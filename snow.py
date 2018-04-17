import pygame
WHITE = (255, 255, 255)
BLACK =(0,0,0)

class Snow(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
         super().__init__()

         self.image = pygame.Surface([width, height]) 
         self.image.fill(WHITE)
         self.image.set_colorkey(WHITE)

         self.width=width 
         self.height=height
         self.color = color
         self.speed = speed

         pygame.draw.ellipse(self.image, color, [0, 0, self.width, self,height])

         self.rect = self.image.get_rect()

         def moveBackward(self, speed): 
                self.rect.y += self.speed * speed / 20

         def cahngeSpeed(self, speed):
            self.color = color
            
