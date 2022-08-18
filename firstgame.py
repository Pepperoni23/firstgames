import pygame

pygame.init()

display_height = 800
display_wight = 1100

display = pygame.display.set_mode((display_wight,display_height))
pygame.display.set_caption('SuperAdmin - box')

icon = pygame.image.load('image/boxing-icon.png')
pygame.display.set_icon(icon)





speed = 5
usr_x  = 100
usr_y = 600
clock = pygame.time.Clock()
huk = False


class objecthero:
    def __init__(self,imag,x,y):
        self.x = x
        self.y = y
        self.hero = imag
    def dis(self):
        display.blit(self.hero,(self.x,self.y))

user = pygame.image.load("image/usr-red.png")
bg = pygame.image.load("image/ring.jpeg")
jump = False
jumpCount = 10

def jumpCounterUP():
    global usr_y
    global usr_x
    global jump
    for i in range(9):
        usr_y -= 5
        usr_x += 3



def jumpCounterDOWN():
    global usr_y
    global usr_x
    global jump
    for i in range(9):
        usr_y += 5
        usr_x += 3
    jump = False





def rus_game():
    global huk
    global usr_x
    global usr_y
    global jump
    global jumpCount
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if not jump:
            if key[pygame.K_LEFT] and usr_x > 5:
                usr_x -= speed
            if key[pygame.K_RIGHT] and usr_x <800:
                usr_x += speed
            if key[pygame.K_UP] and usr_y >410:
                 usr_y -= speed
            if key[pygame.K_DOWN] and usr_y < 650:
                usr_y += speed
            if key[pygame.K_SPACE]:
                jump = True
                jumpCounterUP()
                jumpCounterDOWN()

        hero1 = objecthero(user,usr_x,usr_y).dis()
        display.blit(bg,(0,0))
        display.blit(user,(usr_x,usr_y))
        pygame.display.update()
        clock.tick(80)


rus_game()



