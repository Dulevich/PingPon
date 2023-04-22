from pygame import *

font.init()
font = font.Font(None, 60)
lose1 = font.render('Игрок 1 проиграл',True,(0, 0, 0))
lose2 = font.render('Игрок 2 проиграл',True,(0, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width,  player_hight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed   

win_width = 750
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PingPon")

background = transform.scale(image.load("wooddd.jpg"), (win_width, win_height))

player1 = Player('rocket1.png', 50, 200, 8, 100, 150)
player2 = Player('rocket1.png', 600, 200, 8, 100, 150)
ball = GameSprite('asteroid.png', 340, 250, 5, 70, 70)

game = True
finish = False
clock = time.Clock()
FPS = 60



speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        window.blit(background,(0, 0))     
        player1.update_l()
        player2.update_r()

        player1.reset()
        player2.reset()
        ball.reset()

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1      

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    
    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (200, 200))

    if ball.rect.x < -50:
        finish = True
        window.blit(lose1, (200, 200))

    display.update()
    clock.tick(FPS)