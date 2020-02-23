import pygame
import os
import random

#инициалтизация
pygame.mixer.init()
pygame.init()

#скачивание музыки
pygame.mixer.music.load('data/c245b81d72ab0bb.wav')
pygame.mixer.music.play(-1)

#скачивание изображения
def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    image.set_colorkey((0, 255, 0))
    return(image)

#переменные
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  150, random.randrange(150, 255, 15), 105)
RED =   (255,   0,   0)
fGreen = GREEN
weapons1 = ['zombie hand:4', 'small sword:5', 'daggers:6']
armor1 = ['wooden armor:2', 'plastic armor:3', 'chain armor:4']
weapons2 = ['magic book:7', 'hook:8', 'knuckle:9']
armor2 = ['iron armor:5', 'magic water armor:6', 'ninja clothes:7']
lvl = 0
damage = 2
armor = 1
life = 100
next_l = 0
money = 0
hpx, hpy = 400, 400
attack = None
x, u = None, None
running_sprite = True
size = width, height = [800, 800]
transportC = None
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    #скачиваем изображения
    image1_down = load_image('war1_down.png')
    image2_down = load_image('war2_down.png')
    image3_down = load_image('war3_down.png')
    image1_up = load_image('war1_up.png')
    image2_up = load_image('war2_up.png')
    image3_up = load_image('war3_up.png')
    image1_right = load_image('war1_right.png')
    image2_right = load_image('war2_right.png')
    image3_right = load_image('war3_right.png')
    image1_left = load_image('war1_left.png')
    image2_left = load_image('war2_left.png')
    image3_left = load_image('war3_left.png')

    def __init__(self, group):
        super().__init__(group)
        #ещё немножко переменных
        self.image = Player.image1_down
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.tik = 0
        self.lvl = 0
        self.damage = damage
        self.armor = armor
        self.life = life

    def update(self, args):
        #глобализация
        global lvl
        global damage
        global armor
        global life
        global transportC
        global fGreen
        global next_l
        global hpx, hpy
        global running_sprite
        global attack
        #и ещё переменных
        self.lvl = lvl
        self.damage = damage
        self.armor = armor
        self.life = life
        self.money = money
        #если игра продолжается
        if running_sprite == True:
            #изменение положения
            hpx, hpy = self.rect.x, self.rect.y
            self.tik += 1
            if self.tik == 41:
                self.tik = 0
            #если игрок идет наверх
            if go_up == 1:
                #на каждый 10-ый счёт изменяем картинку героя
                if self.tik == 10:
                    self.image = Player.image2_up
                if self.tik == 20:
                    self.image = Player.image1_up
                if self.tik == 30:
                    self.image = Player.image3_up
                if self.tik == 40:
                    self.image = Player.image1_up
                if go_fast == 1:
                    self.rect.y -= 3
                elif go_fast == 0:
                    self.rect.y -= 1
            #если игрок идёт вниз
            elif go_down == 1:
                #на каждый 10-ый счёт изменяем картинку героя
                if self.tik == 10:
                    self.image = Player.image2_down
                if self.tik == 20:
                    self.image = Player.image1_down
                if self.tik == 30:
                    self.image = Player.image3_down
                if self.tik == 40:
                    self.image = Player.image1_down
                if go_fast == 1:
                    self.rect.y += 3
                elif go_fast == 0:
                    self.rect.y += 1
            #если игрок идёт налево
            elif go_left == 1:
                #на каждый 10-ый счёт изменяем картинку героя
                if self.tik == 10:
                    self.image = Player.image2_left
                if self.tik == 20:
                    self.image = Player.image1_left
                if self.tik == 30:
                    self.image = Player.image3_left
                if self.tik == 40:
                    self.image = Player.image1_left
                if go_fast == 1:
                    self.rect.x -= 3
                elif go_fast == 0:
                    self.rect.x -= 1
            #если игрок идет направо
            elif go_right == 1:
                #на каждый 10-ый счёт изменяем картинку героя
                if self.tik == 10:
                    self.image = Player.image2_right
                if self.tik == 20:
                    self.image = Player.image1_right
                if self.tik == 30:
                    self.image = Player.image3_right
                if self.tik == 40:
                    self.image = Player.image1_right
                if go_fast == 1:
                    self.rect.x += 3
                elif go_fast == 0:
                    self.rect.x += 1
            #если игрок ушёл за поле влево
            if self.rect.x < -32:
                #то переместить на левое поле
                transportC = 'l'
                self.rect.x = width - 1
                #увеличиваем уровень
                lvl += 1
                #новый цвет поля
                fGreen = (105, random.randrange(150, 255, 15), 105)
            #если игрок ушёл за поле вправо
            elif self.rect.x > width:
                #то переместить его на правое поле
                transportC = 'r'
                self.rect.x = -31
                #увеличиваем уровень
                lvl += 1
                #новый цвет поля
                fGreen = (105, random.randrange(150, 255, 15), 105)
            #если игрок ушёл за поле наверх
            elif self.rect.y < -46:
                #то переместить его на верхнее поле
                transportC = 'u'
                self.rect.y = height - 1
                #увеличиваем уровень
                lvl += 1
                #новый цвет поля
                fGreen = (105, random.randrange(150, 255, 15), 105)
            #если игрок ушёл за поле вниз
            elif self.rect.y > height:
                #то переместить его на нижнее поле
                transportC = 'd'
                self.rect.y = -45
                #увеличиваем уровень
                lvl += 1
                #новый цвет поля
                fGreen = (105, random.randrange(150, 255, 15), 105)
            
            #вывод информации:
            #об уровне
            a1 = pygame.font.Font(None, 25)
            b1 = a1.render(f'Level: {self.lvl}', 1, RED)
            xt1 = 700
            yt1 = 10
            screen.blit(b1, (xt1, yt1))
            
            #об уроне, который наносит игрок
            a2 = pygame.font.Font(None, 25)
            b2 = a2.render(f'Damage: {self.damage}', 1, RED)
            xt2 = 550
            yt2 = 10
            screen.blit(b2, (xt2, yt2))
            
            #о броне
            a3 = pygame.font.Font(None, 25)
            b3 = a3.render(f'Armor: {self.armor}', 1, RED)
            xt3 = 400
            yt3 = 10
            screen.blit(b3, (xt3, yt3))
            
            #о кол-ве оставшихся жизней
            a4 = pygame.font.Font(None, 25)
            b4 = a4.render(f'Life: {self.life}', 1, RED)
            xt4 = 250
            yt4 = 10
            screen.blit(b4, (xt4, yt4))
            
            #о кол-ве денег
            a5 = pygame.font.Font(None, 25)
            b5 = a5.render(f'Money: {self.money}$', 1, RED)
            xt5 = 100
            yt5 = 10
            screen.blit(b5, (xt5, yt5))
            
            if next_l == 2:
                transportC = None
                next_l = 0
        
        #если игрок умер
        if life <= 0:
            attack = None
            running_sprite = False
            a0 = pygame.font.Font(None, 50)
            #выводим текст об окончании игры
            b0 = a0.render(f'Game over', 1, RED)
            xt0 = 500
            yt0 = 510
            screen.blit(b0, (xt0, yt0))
        
        #если игрок достиг конца игры
            #и набрал достаточное кол-во денег
        if lvl == 21 and money >= 40:
            #заканчиваем игру
            running_sprite = False
            ag = pygame.font.Font(None, 50)
            #пишем сообщение о победе
            bg = ag.render(f'You win', 1, RED)
            xtg = 500
            ytg = 510
            screen.blit(bg, (xtg, ytg))
        #и не набрал достаточное кол-во денег
        elif lvl == 21 and money < 40:
            #заканчиваем игру
            running_sprite = False
            aq = pygame.font.Font(None, 50)
            #пишем сообщение о проигрыше
            bq = aq.render(f'You lose', 1, RED)
            xtq = 500
            ytq = 510
            screen.blit(bq, (xtq, ytq))

class Chest(pygame.sprite.Sprite):
    #скачиваем изображения
    image1 = load_image('chest1.png')

    def __init__(self, group):
        super().__init__(group)
        #задаем значения переменных
        self.image = Chest.image1
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000

    def update(self, args):
        #глобализация
        global transportC
        global next_l
        global lvl
        global weapons1
        global damage
        global money
        global armor
        global x, u
        #если игра продолжается
        if running_sprite == True:
            #список соприкосающихся спрайтов
            blocks_hit_list = pygame.sprite.spritecollide(self, all_sprites, False)
            #если такие есть
            if len(blocks_hit_list) > 1:
                #если игрок соприкосается с сундуком
                if '[<Player sprite(in 1 groups)>, <Chest sprite(in 1 groups)>]' == str(blocks_hit_list):
                    #сундук исчезает
                    self.rect.x = -1000
                    self.rect.y = -1000
                    #если уровень меньше 10
                    if lvl // 10 == 0:
                        j = random.random()
                        if j >= 0.5:                           
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                #выпало оружие 1
                                x = weapons1[0].split(':')
                            elif 60 < rnd < 90:
                                #выпало оружие 2
                                x = weapons1[1].split(':')
                            elif 90 < rnd < 100:
                                #выпало оружие 3
                                x = weapons1[2].split(':')

                            #если наш урон меньше урона от оружия
                            if damage < int(x[1]):
                                #то мы получаем оружие
                                damage = int(x[1])
                                #выводим сообщение о получении оружия
                                print('-------------------------')
                                print(f'you picked {x[0]} with damage {x[1]}')
                                print('-------------------------')
                            #если наш урон больше или равен урону от оружия
                            elif damage >= int(x[1]):
                                #то мы получаем деньги равные половине урона от оружия
                                m = (int(x[1]) // 2)
                                money += m
                                #сообщение о получение денег
                                print('-------------------------')
                                print(f'you find {m}$')
                                print('-------------------------')
                                
                        elif j < 0.5:
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                #выпала защита 1
                                u = armor1[0].split(':')
                            elif 60 < rnd < 90:
                                #выпала защита 2
                                u = armor1[1].split(':')
                            elif 90 < rnd < 100:
                                #выпала защита 3
                                u = armor1[2].split(':')

                            #если наша зашита меньше чем новая
                            if armor < int(u[1]):
                                #то мы получаем защиту
                                armor = int(u[1])
                                #выводится сообщение о получении защиты
                                print('-------------------------')
                                print(f'you picked {u[0]} with protection {u[1]}')
                                print('-------------------------')
                            #если наша защита лучше полученной 
                            elif armor >= int(u[1]):
                                #то мы получаем деньги равные половине зищиты
                                lm = (int(u[1]) // 2)
                                money += lm
                                #сообщение о получении защиты
                                print('-------------------------')
                                print(f'you find {lm}$')
                                print('-------------------------')
                    
                    #если уровень больше 9
                    if lvl // 10 == 1 or lvl == 20:
                        j = random.random()
                        if j >= 0.5:
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                #получаем оружие 4
                                x = weapons2[0].split(':')
                            elif 60 < rnd < 90:
                                #получаем оружие 5
                                x = weapons2[1].split(':')
                            elif 90 < rnd < 100:
                                #получаем оружие 6
                                x = weapons2[2].split(':')

                            #если наш урон меньше урона от оружия
                            if damage < int(x[1]):
                                #то мы получаем оружие
                                damage = int(x[1])
                                #выводим сообщение о получении оружия
                                print('-------------------------')
                                print(f'you picked {x[0]} with damage {x[1]}')
                                print('-------------------------')
                            #если наш урон больше или равен урону от оружия
                            elif damage >= int(x[1]):
                                #то мы получаем деньги равные половине урона от оружия
                                m = (int(x[1]) // 3)
                                money += m
                                #сообщение о получение денег
                                print('-------------------------')
                                print(f'you find {m}$')
                                print('-------------------------')

                        elif j < 0.5:
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                #получаем защиту 4
                                u = armor2[0].split(':')
                            elif 60 < rnd < 90:
                                #получаем защиту 5
                                u = armor2[1].split(':')
                            elif 90 < rnd < 100:
                                #получаем защиту 6
                                u = armor2[2].split(':')

                            #если наша зашита меньше чем новая
                            if armor < int(u[1]):
                                #то мы получаем защиту
                                armor = int(u[1])
                                #выводится сообщение о получении защиты
                                print('-------------------------')
                                print(f'you picked {u[0]} with protection {u[1]}')
                                print('-------------------------')
                            #если наша защита лучше полученной 
                            elif armor >= int(u[1]):
                                #то мы получаем деньги равные половине зищиты
                                lm = (int(u[1]) // 3)
                                money += lm
                                #сообщение о получении защиты
                                print('-------------------------')
                                print(f'you find {lm}$')
                                print('-------------------------')
                    
                            
                           
            if transportC != None:
                #рандомное появление сундука
                self.rect.x = random.randrange(40, 730)
                self.rect.y = random.randrange(40, 730)
                next_l += 1
            
        
class Skeletron(pygame.sprite.Sprite):
    #скачивание изображений
    image1_down = load_image('skel1_down.png')
    image2_down = load_image('skel2_down.png')
    image3_down = load_image('skel3_down.png')
    image1_up = load_image('skel1_up.png')
    image2_up = load_image('skel2_up.png')
    image3_up = load_image('skel3_up.png')
    image1_right = load_image('skel1_right.png')
    image2_right = load_image('skel2_right.png')
    image3_right = load_image('skel3_right.png')
    image1_left = load_image('skel1_left.png')
    image2_left = load_image('skel2_left.png')
    image3_left = load_image('skel3_left.png')

    def __init__(self, group):
        #задаются переменные
        super().__init__(group)
        self.image = Skeletron.image1_down
        self.rect = self.image.get_rect()
        self.rect.x = -400
        self.rect.y = -400
        self.tik = 0
        self.damage = 1
        self.armor = 1
        self.life = 5
        self.k = 0
        self.at = 0
        self.bat = 1
        self.no = 0

    def update(self, args):
        #глобализация
        global transportC
        global next_l
        global attack
        global life
        global money
        
        #если игра продолжается
        if running_sprite == True:
            #список соприкосающихся спрайтов
            blocks_hit_list = pygame.sprite.spritecollide(self, all_sprites, False)
            #если такие есть
            if len(blocks_hit_list) > 1:
                #если скелет и игрок соприкасаются
                if '[<Player sprite(in 1 groups)>, <Skeletron sprite(in 1 groups)>]' == str(blocks_hit_list):
                    self.k = 1
            else:
                self.k = 0
            
            if transportC != None:
                #рандомное появление скелета
                self.rect.x = random.randrange(40, 710)
                self.rect.y = random.randrange(40, 710)
                #данные скелета
                self.damage = (lvl // 5) + 1
                self.armor = (lvl // 10) + 1
                self.life = (lvl // 2) + 5
                next_l += 1
            
            self.tik += 1
            if self.tik == 41:
                self.tik = 0
            #если игрок близко к скелету
            if (self.rect.x - 250 < hpx < self.rect.x + 250 and self.rect.y - 250 < hpy < self.rect.y + 250) and self.k == 0:
                #скелет приближается к игроку и каждый 20-ый счёт меняется картинка героя
                if hpx > self.rect.x:
                    self.rect.x += 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_right
                    if self.tik == 40:
                        self.image = Skeletron.image3_right
                elif hpx < self.rect.x:
                    self.rect.x -= 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_left
                    if self.tik == 40:
                        self.image = Skeletron.image3_left
                elif hpy > self.rect.y:
                    self.rect.y += 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_down
                    if self.tik == 40:
                        self.image = Skeletron.image3_down
                elif hpy < self.rect.y:
                    self.rect.y -= 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_up
                    if self.tik == 40:
                        self.image = Skeletron.image3_up
            elif self.k == 1:
                attack = 'skel'
                #если скелет атакует
                if attack == 'skel':
                    #если скелет умирает
                    if self.life <= 0:
                        #то он исчезает
                        self.rect.x = 3000
                        self.rect.y = 3000
                        attack = None
                    #если игрок пытается убить скелета
                    if args.type == pygame.MOUSEBUTTONDOWN and self.bat == 1:
                        self.bat = 0
                        #уменьшаем жизни скелета
                        self.life -= damage
                        #сообщение о нанесении урона
                        print('-------------------------')
                        print(f'you caused damage {damage}')
                        #если скелет еще жив
                        if self.life > 0:
                            #выводится сообщение об оставшихся жизнях скелета
                            print(f'enemy lives {self.life}')
                        #если скелет умер
                        else:
                            #выводится сообщение о смерти 
                            print(f'enemy dies')
                            print('you find 2$')
                            #добавление денег
                            money += 2
                        print('-------------------------')
                    self.at += 1
                    if self.at == 200:
                        iii = random.randint(0, 100)
                        if armor > iii > 0:
                            #получаем урон в 2 раза меньше чем у скелета
                            life -= self.damage // 2
                            #вывод сообщения о получении урона
                            print('-------------------------')
                            print(f'you get damage {self.damage // 2}')
                            print('-------------------------')
                        else:
                            #получаем урон равный урону скелета
                            life -= self.damage
                            #вывод сообщения о получении урона
                            print('-------------------------')
                            print(f'you get damage {self.damage}')
                            print('-------------------------')
                        self.at = 0
                        self.bat = 1
            elif self.k == 0:
                attack = None
        else:
            self.image = Skeletron.image1_down
                


#заводим группы спрайтов
Player(all_sprites)
Chest(all_sprites)
Skeletron(all_sprites)
pygame.display.set_caption("PythonRPG")
#делаем иконку игры
img = pygame.image.load('data\icon.png')
pygame.display.set_icon(img)



#задаем переменные
go_up = 0
go_down = 0
go_left = 0
go_right = 0
go_fast = 0
fps = 120
running = True
clock = pygame.time.Clock()


while running:
    clock.tick(fps)
    #заливаем поле и рисуем квадрат
    screen.fill(fGreen)
    pygame.draw.polygon(screen, BLACK, [[40, 40], [760, 40], [760, 760], [40, 760]], 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #если клавиша движения зажата
        if event.type == pygame.KEYDOWN:
            #то идем в нужном направлении
            if event.key == pygame.K_w:
                go_up = 1
            if event.key == pygame.K_s:
                go_down = 1
            if event.key == pygame.K_a:
                go_left = 1
            if event.key == pygame.K_d:
                go_right = 1
            if event.key == pygame.K_LSHIFT:
                go_fast = 1
        #если не зажата
        if event.type == pygame.KEYUP:
            #то не движемся
            if event.key == pygame.K_w:
                go_up = 0
            if event.key == pygame.K_s:
                go_down = 0
            if event.key == pygame.K_a:
                go_left = 0
            if event.key == pygame.K_d:
                go_right = 0
            if event.key == pygame.K_LSHIFT:
                go_fast = 0
    
    all_sprites.draw(screen)
    all_sprites.update(event)
    
    pygame.display.flip()

pygame.quit()