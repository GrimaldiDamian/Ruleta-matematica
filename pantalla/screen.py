import pygame
from PIL import Image
from constantes.constantes import *

class screen():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ancho,alto),pygame.FULLSCREEN)
        self.fondo = pygame.image.load("RECURSOS/fondo.jpg")
        self.etapa = "menu"
        self.running = True
        self.myFond = pygame.font.SysFont('Times New Roman', tamaño_letra)
        self.reloj = pygame.time.Clock()
        self.dificultad = ["FACIL","MEDIO","DIFICIL"]
        self.inicio = 0

    def manejo_evento(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if self.etapa != "menu":
                    if event.key == pygame.K_ESCAPE:
                        self.etapa = "menu"
                else:
                    if event.key == pygame.K_RIGHT:
                        self.inicio +=1
                        if self. inicio == 3:
                            self.inicio = 0
                    elif event.key == pygame.K_LEFT:
                        self.inicio -= 1
                        if self.inicio ==-1:
                            self.inicio = 2

    def dibujo_Texto(self,texto,posicion_x,posicion_y):
        ancho_texto,_ = self.myFond.size(texto)
        texto = self.myFond.render(texto,True,(0,0,0))
        self.screen.blit(texto,(posicion_x - (ancho_texto//2),posicion_y))

    def dibujar_menu(self):
        pygame.draw.rect(self.screen,colores[self.inicio],(centro_ancho-(ancho_Rect//2),centro_alto-(alto_Rect//2),ancho_Rect,alto_Rect))
        self.dibujo_Texto(self.dificultad[self.inicio],centro_ancho,centro_alto - (tamaño_letra//2))

    def dibujar(self):
        if self.etapa == "menu":
            self.screen.blit(self.fondo,(0,0))
            self.dibujar_menu()
        
        pygame.display.flip()

    def bucle_principal(self):
        while self.running:
            
            self.manejo_evento()
            
            self.reloj.tick(60)
            
            self.dibujar()