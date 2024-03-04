import pygame
import os

pygame.init()

screen_width = 1280
screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

image_path = os.path.join(os.path.dirname(__file__), "image2.png")
image = pygame.image.load(image_path)

image_width = 200  
image_height = 300 
image = pygame.transform.scale(image, (image_width, image_height))

imagePosition = [[150,450], [500,100], [800,450]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 
    
    for idx, (x, y) in enumerate(imagePosition):
        if idx == 0:
            rotated_image = pygame.transform.rotate(image, -90)
        elif idx == 2:  
            rotated_image = pygame.transform.rotate(image, 90)
        else:  
            rotated_image = pygame.transform.rotate(image, 180)
        
        screen.blit(rotated_image, (x, y))

    pygame.display.flip()

# Quitter Pygame
pygame.quit()