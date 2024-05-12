from pygame import *
from random import randint
import time as timer
pygame.init()
game=True 
life = 3
font.init()
font2 = font.Font(None,52)
finish=False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x>=5:
            self.rect.x = self.rect.x - self.speed
        if keys_pressed[K_d] and self.rect.x<=650:
            self.rect.x = self.rect.x + self.speed
        if keys_pressed[K_w] and self.rect.y>=5:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_s] and self.rect.y<650:
            self.rect.y = self.rect.y + self.speed

lost = 0
win = 0 

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(0, win_width - 80)
            self.rect.y = 0
            lost += 1
            self.speed = randint(1,6)




win_width = 700
win_height = 500

window = display.set_mode((700,500))
display.set_caption('лабиринт')
background = transform.scale(image.load("images.png"),(700, 500))
window.blit(background,(0,0))

sprite1 = Player('гэри.jpg',50,400,5)
monsters = sprite.Group()
for i in range(1,5):
    monster = Enemy('сквидвард.jpg',randint(10,500),100,randint(2,6))
    monsters.add(monster)
    monster = Enemy('krabs.jpg', randint(10,500),100,randint(1,4))
    monsters.add(monster)

mixer.init()
mixer.music.load('jungles.mp3')
mixer.music.play()



clock = time.Clock()
fps = 60
while game == True:
    text_lose = font2.render('Пропущено: ' + str(lost), True,(255,255,255))
    for e in event.get():
          if e.type == QUIT:
               game = False        
    window.blit(background,(0,0))
    sprite1.reset()
    
    window.blit(text_lose,(100,100))
    sprite1.update()
    monsters.draw(window)
    sprites_list = sprite.spritecollide(
    sprite1, monsters, True
)
    if sprites_list:
        #sprite.spritecollide(sprite1,monsters,True)
        life = life-1
    if life == 0:
        font1 = font.Font(None, 70)
        lose = font1.render(
            'YOU LOSE!', True, (255,0,0)
        )
        window.blit(lose,(200,200))
        game = False
    if lost == 20:
        finish = True
        font = font.Font(None, 70)
        win = font.render(
            'YOU WON!', True, (0,255,0)
        )
        window.blit(win,(250,200))
        timer.sleep(1)
        game = False
    if life == 3:
        life_colour = (0,255,0)
    if life == 2:
        life_colour = (0,0,255)
    if life == 1:
        life_colour = (255,0,0)
    font1 = font.Font(None, 70)
    cur_life = font1.render(
        str(life),True,(life_colour)
    )
    window.blit(cur_life,(250,200))

            
    monsters.update()

    display.update()
    if game == False:
        timer.sleep(10)
    clock.tick(fps)









