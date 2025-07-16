import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, shots, drawable)
    
    asteroidField = AsteroidField()
    
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x,y)
    
    
    dt = 0
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        for update_v in updatable:
            update_v.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()
        

        screen.fill("black")

        for draw_v in drawable:
            draw_v.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
