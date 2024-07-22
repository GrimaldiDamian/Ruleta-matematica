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
        self.reloj = pygame.time.Clock()

    def manejo_evento(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def dibujar(self):
        if self.etapa == "menu":
            self.screen.blit(self.fondo,(0,0))
        
        pygame.display.flip()

    def bucle_principal(self):
        while self.running:
            
            self.manejo_evento()
            
            self.reloj.tick(60)
            
            self.dibujar()