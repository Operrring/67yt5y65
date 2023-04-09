# from pygame import*

#дисплей

window = display.set_mode((700,500))
display.set_caption('Игра в печеньку')
background = transform.scale(image.load('lab1.png'), (700, 500))
final = transform.scale(image.load('final.jpg'), (700, 500))

#Классы
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):   
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed

    def update(self):
        if self.rect.x <= 270:
            self.direction = "right"
        if self.rect.x >= 320:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed




#Рассположение обектов
tochcka = Player('tochka.png', 25, 17, 627, 445, 0, 0)
beliy = GameSprite('beliy_1.jpg', 267, 368, 0, 0)
beliy_1 = GameSprite('beliy_1.jpg', 400, 300, 535, 0)
beliy_2 = GameSprite('beliy_1.jpg', 295, 216, 115, 0)
beliy_3 = GameSprite('beliy_1.jpg', 430, 35, 220, 333)
beliy_4 = GameSprite('beliy_1.jpg', 700, 34, 85, 402)
beliy_5 = GameSprite('beliy_1.jpg', 990, 34, 0, 470)
beliy_6 = GameSprite('beliy_1.jpg', 35, 400, 0, 360)
beliy_7 = GameSprite('beliy_1.jpg', 35, 400, 676, 260)
beliy_8 = GameSprite('beliy_1.jpg', 450, 52, 338, 249)
beliy_9 = GameSprite('beliy_1.jpg', 97, 130, 413, 0)
beliy_10 = GameSprite('beliy_1.jpg', 97, 130, 447, 147)
kras = GameSprite("kras.jpg", 35, 35, 500, 30)
monster = Enemy('echpoch.jpeg', 15, 15, 320, 280, 6)


#барьеры
barriers = sprite.Group()
barriers.add(beliy)
barriers.add(beliy_1)
barriers.add(beliy_2)
barriers.add(beliy_3)
barriers.add(beliy_4)
barriers.add(beliy_5)
barriers.add(beliy_6)
barriers.add(beliy_7)
barriers.add(beliy_8)
barriers.add(beliy_9)
barriers.add(beliy_10)
barriers.add(monster)

win = False
run = True


#движение
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                tochcka.x_speed = -10
            
        elif e.type == KEYUP:
            if e.key == K_a:
                tochcka.x_speed = 0
                
        if e.type == KEYDOWN:
            if e.key == K_d:
                tochcka.x_speed = 10
            
        if e.type == KEYUP:
            if e.key == K_d:
                tochcka.x_speed = 0
        
        if e.type == KEYDOWN:
            if e.key == K_s:
                tochcka.y_speed = 10
            
        if e.type == KEYUP:
            if e.key == K_s:
                tochcka.y_speed = 0

        if e.type == KEYDOWN:
            if e.key == K_w:
                tochcka.y_speed = -10
            
        if e.type == KEYUP:
            if e.key == K_w:
                tochcka.y_speed = 0


    
#Вывод спрайтов
    if win != True:
        window.blit(background, (0, 0))
        tochcka.reset()
        tochcka.update()
        beliy_1.reset()
        beliy.reset()
        beliy_2.reset()
        beliy_3.reset()
        beliy_4.reset()
        beliy_5.reset()
        beliy_6.reset()
        beliy_7.reset()
        beliy_8.reset()
        beliy_9.reset()
        beliy_10.reset()
        monster.update()
        monster.reset()
        kras.reset()


        if sprite.collide_rect(tochcka, kras):
            win = True
            window.blit(final,(0, 0))
        
    display.update()

    
