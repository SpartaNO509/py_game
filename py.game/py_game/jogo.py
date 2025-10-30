import pygame

pygame.init()
pygame.display.set_caption("Jogo em Python")

tela_largura = 1000
tela_altura = 800
x = 200
y = 500
scale = 1
gravidade = 0.5
altura = y*2
velocidade = 5
class Mapa:
    def __init__(self,mapa):
        self.mapa = mapa
        
        



class Jogador:
    def __init__(self,vida,x,y,vel):
        self.vel = vel
        self.vida = vida
        self.x = x
        self.y = y
        
        
jogador1 = Jogador(100,1,1,5)






tela = pygame.display.set_mode((tela_largura, tela_altura))

img = pygame.image.load('img/parado1.png').convert_alpha()
largura_img = img.get_width()
altura_img = img.get_height()
img = pygame.transform.scale(img, (largura_img * scale, altura_img * scale))

jogador = img.get_rect()
jogador.center = (x, y)

clock = pygame.time.Clock()
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        teclas = pygame.key.get_pressed()    
        if  teclas[pygame.K_ESCAPE]:
            rodando = False
        if teclas[pygame.K_LEFT]:
            jogador.x -= velocidade
        if teclas[pygame.K_RIGHT]:
            jogador.x += velocidade
        if teclas[pygame.K_SPACE]:
            jogador.y -= velocidade
        if teclas[pygame.K_LSHIFT]:
            jogador.y += velocidade               
        

    tela.fill((30, 30, 30))
    tela.blit(img, jogador)
    pygame.display.update()

pygame.quit()
