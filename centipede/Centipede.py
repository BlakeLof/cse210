import pygame, random
from Centipede_part import *
from Tick import *
from Highscore import *
from Spider import *

game_map = []
pygame.init()
pygame.display.set_caption('Centipede')
mushroom_image = pygame.image.load('mushroom.gif')
mushroom_image2 = pygame.image.load('mushroom2.gif')
mushroom_image3 = pygame.image.load('mushroom3.gif')
mushroom_image4 = pygame.image.load('mushroom4.gif')
player_image = pygame.image.load('player.png')

screen = pygame.display.set_mode([625,700])
level = 0
mode = 'menu'
pygame.key.set_repeat(20, 20)
mushrooms = []
centipede_parts = []
shoot_x = 0
titlefont = pygame.font.SysFont("Baskerville", 100)
myfont = pygame.font.SysFont("Arial", 20)
shoot_y = 0
time = 0
score = 0
spawning_centipedes = 0
can_shoot = True
player_x = 312
player_y = 650
pygame.mouse.set_visible(False)
running = True
pygame.draw.rect(screen, pygame.color.THECOLORS['black'], (0,0,750,840))
tick = 0
spider = Spider()

def setup_game_map():
    global game_map
    game_map = []
    for x in range(0,28):
        arrayOfZeros = [0]*25
        game_map.append(arrayOfZeros)
    for x in range (0,30):
        mushroomx = random.randint(0, 24)
        mushroomy = random.randint(0, 24)
        mushrooms.append("mushroom")
        game_map[mushroomy][mushroomx] = 1


        


        

def draw_game_map():
        for column in range(25):
            for row in range(28):
                spot = game_map[row][column]
                if spot == 1:
                    screen.blit(mushroom_image, [column*25, row*25])
                if spot == 2:
                    screen.blit(mushroom_image2, [column*25, row*25])
                if spot == 3:
                    screen.blit(mushroom_image3, [column*25, row*25])
                if spot == 4:
                    screen.blit(mushroom_image4, [column*25, row*25])

                    
def move():
    global player_x, player_y, shoot_x, shoot_y, can_shoot
    pos = pygame.mouse.get_pos()
 
    if game_map[pos[1]/25][pos[0]/25] == 0:
        player_x = pos[0]-6
        player_y = pos[1]-15
        if player_x > 599:
            player_x = 600
        if player_y > 649:
            player_y = 650
        if player_y < 551:
            player_y = 550

    shoot_y -= 25
    if shoot_y < 1:
        can_shoot = True
        
def shoot(x,y):
    global shoot_x, shoot_y, can_shoot
    shoot_x = x +9
    shoot_y = y
    can_shoot = False
    
def is_shot():
    global shoot_x, shoot_y, can_shoot, score, tick
    shot_tilex = shoot_x/25
    shot_tiley = shoot_y/25
    #check if hit mushroom
    if game_map[shot_tiley][shot_tilex] > 0:
        game_map[shot_tiley][shot_tilex] +=1
        if game_map[shot_tiley][shot_tilex]==5:
            game_map[shot_tiley][shot_tilex]=0
        can_shoot = True
        shoot_x = 1000
        shoot_y = 800
        score+=1
     

    #check if hit centipede
    for cp in centipede_parts:
        if shot_tilex == cp.x and shot_tiley == cp.y:
            centipede_parts.remove(cp)
            score += 10
            game_map[shot_tiley][shot_tilex] = 1
            can_shoot = True
            shoot_x = 1000
            shoot_y = 800
    if shot_tilex == tick.x and shot_tiley == tick.y:
            score += 50
            can_shoot = True
            shoot_x = 1000
            shoot_y = 800
            tick.dead()
    if spider.rect.colliderect((shoot_x,shoot_y,2,17)):
            score += 20
            can_shoot = True
            shoot_x =1000
            shoot_y = 800
            spider.x = 10000
def is_dead():
    global running, mode, topthreescores
    player_rect = pygame.Rect(player_x, player_y, 18, 25)
    for cp in centipede_parts:
        if player_rect.colliderect(cp.rect):
            mode='menu'
            Highscore.write_score(score)
            topthreescores = Highscore.get_top_scores(3)
    if player_rect.colliderect(tick.rect):
            mode='menu'
            Highscore.write_score(score)
            topthreescores = Highscore.get_top_scores(3)
    if player_rect.colliderect(spider.rect):
            mode= 'menu'
            Highscore.write_score(score)
            topthreescores = Highscore.get_top_scores(3)
def make_centipede():
    global spawning_centipedes
    spawning_centipedes = 12
def draw_everything():
    pygame.draw.rect(screen, pygame.color.THECOLORS['black'], (0,0,750,840))
    message = myfont.render(str(score) , 1, pygame.color.THECOLORS['red'])
    screen.blit(message, (20, 675))
    draw_game_map()
    pygame.draw.rect(screen, pygame.color.THECOLORS['red'], (shoot_x,shoot_y,2,17))
    screen.blit(tick.image, tick.rect)
    screen.blit(spider.image, spider.rect)
    for cp in centipede_parts:
            screen.blit(cp.image, cp.rect)
    screen.blit(player_image, (player_x, player_y))
    pygame.display.update()
def all_dead():
    global level
    if centipede_parts == []:
      make_centipede()
      level+=1
      print level

tick = Tick()
tick.dead()
topthreescores = Highscore.get_top_scores(3)

while running:

    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONUP and mode == 'menu':
            mode = 'play'
            time = 0
            centipede_parts = []
            score=0
            tick.dead()
            setup_game_map()
        keys = pygame.key.get_pressed()
        pressed=pygame.mouse.get_pressed()
        if (keys[pygame.K_SPACE] or pressed[0] ==True) and can_shoot == True :
               shoot(player_x, player_y+1)
    if mode == 'menu':
        spider.x = 10000
        pygame.draw.rect(screen, pygame.color.THECOLORS['black'], (0,0,750,840))
        level = 1
        Highscore.show_high_scores(pygame, screen, topthreescores, 300, 500)
        message = myfont.render("Click to Start the Game" , 1, pygame.color.THECOLORS['white'])
        screen.blit(message, (220, 240))
        title = titlefont.render("CENTIPEDE" , 1, pygame.color.THECOLORS['white'])
        screen.blit(title, (130, 100))
        pygame.display.update()
    if mode == 'play':
 
        move()
        is_dead()

            
        if random.randint(0,2000/level) == 0:
            if tick.offscreen() == True:
                tick = Tick()
        if random.randint(0,1000/level) == 0:
            if spider.offscreen() == True:
                spider = Spider()
        if time%3 == 0:
            all_dead()
            if spawning_centipedes>0:
                spawning_centipedes-=1
                centipede_part = Centipede_part(12,0)
                centipede_parts.append(centipede_part)
            for cp in centipede_parts:
                cp.move(game_map)   
            tick.move(game_map)
            spider.move()
            
        if can_shoot == False:
            is_shot()
                       
 
        time+=1
        draw_everything()
 
 
pygame.quit()
