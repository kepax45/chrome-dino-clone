import pygame
import random
from utils import *
from classes import *

running = True
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dino clone')
velY = 0
frames = 0
speed = 12
grounded = False
obstacle1 = get_random_obstacle()
obstacle2 = get_random_obstacle()
obstacle2.x += 600
clock = pygame.time.Clock()
score = 0
highscore = 0
pricked = False
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            break
    if((pricked==True and restart_button.collides_point(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) or (pricked==True and pygame.key.get_pressed()[pygame.K_SPACE])):
        obstacle1.x = -obstacle1.endpointX()
        obstacle2.x = -obstacle2.endpointX()
        score = 0
        speed = 12
        dino.y = ground1.y - 65
        pricked = False
    if(pricked==True):
        continue
    window.fill((255, 255, 255))
    if(dino.collides(ground1) or dino.collides(ground2)):
        dino.y = ground1.y - 65
        velY = 0
        grounded = True
    if(frames%5==0):
        score+=1
    if(frames%5==0 and grounded==True):
        dino.animate('walking')
    score_display.force_image(make_score(score))
    score_display.draw(window)
    ground1.draw(window)
    ground2.draw(window)
    obstacle1.draw(window)
    obstacle2.draw(window)
    if(dino.collides(obstacle1) or dino.collides(obstacle2)):
        dino.force_image(pricked_sprite)
        highscore = max(score, get_highscore())
        write_highscore(highscore)
        highscore_display.force_image(make_highscore())
        highscore_display.x = score_display.x-highscore_display.main_img.get_width()*1.5
        highscore_display.draw(window)
        game_over_sign.draw(window)
        restart_button.draw(window)
        pricked = True
    dino.draw(window)
    if(pygame.key.get_pressed()[pygame.K_SPACE] and grounded==True):
        velY = -30
        dino.force_image(standing)
        grounded = False
    if(grounded==False):
        velY += 1.5
        dino.y += velY
    if(obstacle1.endpointX() <= 0):
        obstacle1 = get_random_obstacle()
        if(obstacle1.x-obstacle2.endpointX()<=400):
            obstacle1.x += 400
    if(obstacle2.endpointX() <= 0):
        obstacle2 = get_random_obstacle()
        if(obstacle2.x-obstacle1.endpointX()<=400):
            obstacle2.x += 400
    pygame.display.update()
    ground1.x -= speed
    ground2.x -= speed
    obstacle1.x -= speed
    obstacle2.x -= speed
    if(ground1.x <= -2401):
        ground1.x = ground2.x+ground2.width
    if(ground2.x <= -2401):
        ground2.x = ground1.x+ground1.width
    speed += 0.001
    frames = (frames + 1)
pygame.quit()
