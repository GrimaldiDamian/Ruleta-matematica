import pygame
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

    def animacion(self,posicion1,posicion2,posicion3,posicion4,posicion5,posicion6):
        for i in range(len(posicion1)):
            self.screen.blit(self.fondo, (0, 0))
            pygame.draw.polygon(self.screen,"grey",[posicion1[i],posicion2[i],posicion3[i]])
            pygame.draw.polygon(self.screen,"grey",[posicion4[i],posicion5[i],posicion6[i]])
            self.dibujar_elementos_menu()
            pygame.display.flip()
            pygame.time.wait(35)

        for i in range(len(posicion1)-1,0,-1):
            self.screen.blit(self.fondo, (0, 0))
            pygame.draw.polygon(self.screen,"grey",[posicion1[i],posicion2[i],posicion3[i]])
            pygame.draw.polygon(self.screen,"grey",[posicion4[i],posicion5[i],posicion6[i]])
            self.dibujar_elementos_menu()
            pygame.display.flip()
            pygame.time.wait(35)

    def dibujar_menu(self):
        self.screen.blit(self.fondo,(0,0))
        punto_1 = (centro_ancho - (ancho_Rect//2) - ancho_Tri,centro_alto)
        punto_2 = (centro_ancho - (ancho_Rect//2) - 10,centro_alto-(alto_Rect//2))
        punto_3 = (centro_ancho - (ancho_Rect//2) - 10,centro_alto+(alto_Rect//2))
        punto_4 = (centro_ancho + (ancho_Rect//2) + ancho_Tri,centro_alto)
        punto_5 = (centro_ancho + (ancho_Rect//2) + 10,centro_alto-(alto_Rect//2))
        punto_6 = (centro_ancho + (ancho_Rect//2) + 10,centro_alto+(alto_Rect//2))
        
        lista_punto_1 = []
        lista_punto_2 = []
        lista_punto_3 = []
        lista_punto_4 = []
        lista_punto_5 = []
        lista_punto_6 = []
        
        for i in range(10):
            punto_1 = punto_1[0] - i, punto_1[1]
            lista_punto_1.append(punto_1)
            punto_2 = punto_2[0] - i, punto_2[1]
            lista_punto_2.append(punto_2)
            punto_3 = punto_3[0] - i, punto_3[1]
            lista_punto_3.append(punto_3)
            punto_4 = punto_4[0] + i, punto_4[1]
            lista_punto_4.append(punto_4)
            punto_5 = punto_5[0] + i, punto_5[1]
            lista_punto_5.append(punto_5)
            punto_6 = punto_6[0] + i, punto_6[1]
            lista_punto_6.append(punto_6)
        
        self.animacion(lista_punto_1,lista_punto_2,lista_punto_3,lista_punto_4,lista_punto_5,lista_punto_6)

    def dibujar_elementos_menu(self):
        pygame.draw.rect(self.screen,colores[self.inicio],(centro_ancho-(ancho_Rect//2),centro_alto-(alto_Rect//2),ancho_Rect,alto_Rect))
        self.dibujo_Texto(self.dificultad[self.inicio],centro_ancho,centro_alto - (tamaño_letra//2))

    def dibujar(self):
        if self.etapa == "menu":
            self.dibujar_menu()
        
        pygame.display.flip()

    def bucle_principal(self):
        while self.running:
            
            self.manejo_evento()
            
            self.reloj.tick(60)
            
            self.dibujar()