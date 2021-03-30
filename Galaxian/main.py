import pygame
from pygame.locals import *
from pygame import mixer
import random
import math

control_frame = 0


"""
Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
"""

def gameOverText():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (50, 250))

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def isCollision(x, y, x0, y0):
    distance = math.sqrt((math.pow(x-x0, 2))+ (math.pow(y-y0, 2)))
    if distance < 32:
        return True
    else:
        return False


def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_State
    bullet_State = "fire"
    screen.blit(bulletImg, (x+18, y+10))

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Galaxian")

    icon = pygame.image.load("Galaxian Resources\\alien.png")
    pygame.display.set_icon(icon)


    # player
    playerImg = pygame.image.load("Galaxian Resources\\Player\\player.png")
    player_X, player_Y = (425, 450)
    player_XCHANGE = 0

    enemyImg = list()
    enemy_X = list()
    enemy_Y = list()
    enemy_XCHANGE = list()
    enemy_YCHANGE = list()
    num_of_enemies = 9

    # enemy
    for i in range(num_of_enemies):
        if i >= 0 and i < 3:
            enemyImg.append(pygame.image.load("Galaxian Resources\\Enemy\\enemy1.png"))
            enemy_X.append(random.randint(50, 850))
            enemy_Y.append(random.randint(50, 150))
            enemy_XCHANGE.append(3)
            enemy_YCHANGE.append(20)

        if i >= 3 and i < 6:
            enemyImg.append(pygame.image.load("Galaxian Resources\\Enemy\\enemy4.png"))
            enemy_X.append(random.randint(50, 850))
            enemy_Y.append(random.randint(50, 150))
            enemy_XCHANGE.append(3)
            enemy_YCHANGE.append(20)

        if i >= 6 and i < 9:
            enemyImg.append(pygame.image.load("Galaxian Resources\\Enemy\\enemy3.png"))
            enemy_X.append(random.randint(50, 850))
            enemy_Y.append(random.randint(50, 150))
            enemy_XCHANGE.append(3)
            enemy_YCHANGE.append(20)




    # bullet
    bulletImg = pygame.image.load("Galaxian Resources\\Assets\\bala.png")
    bullet_X = 0
    bullet_Y = 430
    buleetXchange = 0
    bulletYchange = 8
    bullet_State = "ready"



    # background
    background = pygame.image.load("Galaxian Resources\\Background\\background1.png")

    backgrounds = list()

    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background1.png"))

    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background2.png"))

    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background3.png"))

    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background4.png"))

    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background5.png"))

    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background6.png"))

    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))
    backgrounds.append(pygame.image.load("Galaxian Resources\\Background\\background7.png"))

    # background sound
    mixer.music.load("Galaxian Resources\\Sounds\\background.wav")
    mixer.music.play(-1)

    # score
    score_value = 0;
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    # game over text
    over_font = pygame.font.Font('freesansbold.ttf', 128)


    running = True
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_XCHANGE = -3
                if event.key == pygame.K_RIGHT:
                    player_XCHANGE = 3
                if event.key == pygame.K_SPACE:
                    if bullet_State is "ready":
                        laser_Sound = mixer.Sound("Galaxian Resources\\Sounds\\laser.wav")
                        laser_Sound.play()
                        bullet_X = player_X
                        fire_bullet(bullet_X, bullet_Y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_XCHANGE = 0




        screen.fill((0, 0, 0))

        if(control_frame >= 98):
            control_frame = 0

        screen.blit(backgrounds[control_frame], (0, 0))


        # player movement
        player_X += player_XCHANGE
        if player_X <= 0:
            player_X = 0
        elif player_X >= 836:
            player_X = 836

        # enemy movement
        for i in range(num_of_enemies):
            #Game Over
            if enemy_Y[i] > 400:
                for j in range(num_of_enemies):
                    enemy_Y[j] = 2000
                gameOverText()
                break
            enemy_X[i] += enemy_XCHANGE[i]
            if enemy_X[i] <= 0:
                enemy_XCHANGE[i] = 3
                enemy_Y[i] += enemy_YCHANGE[i]
            elif enemy_X[i] >= 836:
                enemy_XCHANGE[i] = -3
                enemy_Y[i] += enemy_YCHANGE[i]


            collision = isCollision(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
            if collision:
                explosion_Sound = mixer.Sound("Galaxian Resources\\Sounds\\explosion.wav")
                explosion_Sound.play()
                score_value += 1
                bullet_Y = 430
                bullet_State = "ready"
                enemy_X[i], enemy_Y[i] = (random.randint(50, 850), random.randint(50, 150))
            enemy(enemy_X[i], enemy_Y[i], i)

        # bullet movement
        if bullet_Y <= 0:
            bullet_Y = 430
            bullet_State = "ready"

        if bullet_State is "fire":
            fire_bullet(bullet_X, bullet_Y)
            bullet_Y -= bulletYchange

        control_frame += 1
        player(player_X, player_Y)
        show_score(textX, textY)
        pygame.display.flip()



