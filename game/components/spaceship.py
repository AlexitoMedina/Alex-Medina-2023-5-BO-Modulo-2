import pygame
from game.components.bullets.bullet import Bullet
from pygame.sprite import Sprite

from game.utils.constants import DEFAULT_TYPE, SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, HEAVY_MACHINE_GUN_TYPE

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH//2) - SPACESHIP_WIDTH//2
    Y_POS = 500
    SPEED = 10
    SCREEN_ERROR = 10
    SPEED_BULLET = 8

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP,(self.SPACESHIP_WIDTH,self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.explosion = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.power_up_shoot = HEAVY_MACHINE_GUN_TYPE
        self.has_power_up = False
        self.has_power_up_shoot = False
        self.power_time_up = 0
        


    def update(self, user_input,game):
        #movimiento en diagonal hacia abajo izquierda
        if user_input[pygame.K_DOWN] and user_input[pygame.K_LEFT]:
            if self.rect.x == 0 and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
                self.rect.y += 5
            if self.rect.left > 0 and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x -= 5
                self.rect.y += 5
            if user_input[pygame.K_m]:
                self.shoot(game)

        #movimiento diagonal hacia arriba izquierda
        elif user_input[pygame.K_UP] and user_input[pygame.K_LEFT]:
            if self.rect.x == 0 and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
                self.rect.y -= 5
            if self.rect.left > 0 and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x -= 5
                self.rect.y -= 5
            if user_input[pygame.K_m]:
                self.shoot(game)    
        #movimiento diagonal hacia arriba derecha
        elif user_input[pygame.K_UP] and user_input[pygame.K_RIGHT]:
            if self.rect.x > SCREEN_WIDTH-self.SPACESHIP_WIDTH and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x = self.SPEED
                self.rect.y -= 5
            if self.rect.right < SCREEN_WIDTH and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x += 5
                self.rect.y -= 5
            if user_input[pygame.K_m]:
                self.shoot(game)
        #movimiento diagonal hacia abajo derecha
        elif user_input[pygame.K_DOWN] and user_input[pygame.K_RIGHT]:
            if self.rect.x > SCREEN_WIDTH-self.SPACESHIP_WIDTH and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x = self.SPEED
                self.rect.y += 5
            if self.rect.right < SCREEN_WIDTH and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x += 5
                self.rect.y += 5
            if user_input[pygame.K_m]:
                self.shoot(game)

        #va a la izquierda 
        elif user_input[pygame.K_LEFT]:
            if self.rect.x == 0:
                self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
            if self.rect.left > 0:
                self.rect.x -= self.SPEED
            if user_input[pygame.K_m]:
                self.shoot(game)
        #va a la derecha
        elif user_input[pygame.K_RIGHT]:
            if self.rect.x > SCREEN_WIDTH - self.SPACESHIP_WIDTH - self.SCREEN_ERROR:
                self.rect.x = self.SPEED
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.SPEED
            if user_input[pygame.K_m]:
                self.shoot(game)
        #va arriba
        elif user_input[pygame.K_UP]:
            if self.rect.top > SCREEN_HEIGHT//2:
                self.rect.y -= self.SPEED
            if user_input[pygame.K_m]:
                self.shoot(game)
        #va abajo
        elif user_input[pygame.K_DOWN]:
            if self.rect.bottom < SCREEN_HEIGHT : 
                self.rect.y += self.SPEED
            if user_input[pygame.K_m]:
                self.shoot(game)
        #disparo
        elif user_input[pygame.K_m]:
            self.shoot(game)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot (self,game):
        bullet= Bullet(self)
        game.bullet_manager.add_bullet(bullet)

    def set_image(self, size=(SPACESHIP_WIDTH, SPACESHIP_HEIGHT), image = SPACESHIP):
        self.image = image 
        self.image = pygame.transform.scale(self.image, size )

 
