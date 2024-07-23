import pygame
import random
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
        self.resultado = 0
        self.numero = 0
        self.input = ""

    def manejo_evento(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.TEXTINPUT:
                if self.etapa == "respuestas":
                    if event.text in ["0","1","2","3","4","5","6","7","8","9"]:
                        self.input +=event.text
            if event.type == pygame.KEYDOWN:
                if self.etapa != "menu":
                    if event.key == pygame.K_ESCAPE:
                        self.etapa = "menu"
                    if self.etapa == "respuestas":
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            self.respuesta()
                        if event.key == pygame.K_BACKSPACE:
                            self.input = self.input[:-1]
                else:
                    if event.key == pygame.K_RIGHT:
                        self.inicio +=1
                        if self. inicio == 3:
                            self.inicio = 0
                    elif event.key == pygame.K_LEFT:
                        self.inicio -= 1
                        if self.inicio ==-1:
                            self.inicio = 2
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.etapa = "juego"

    def dibujo_Texto(self,texto,posicion_x,posicion_y):
        ancho_texto,_ = self.myFond.size(texto)
        texto = self.myFond.render(texto,True,(0,0,0))
        self.screen.blit(texto,(posicion_x - (ancho_texto//2),posicion_y))

    def _animacion(self,posicion1,posicion2,posicion3,posicion4,posicion5,posicion6,i):
        self.screen.blit(self.fondo, (0, 0))
        pygame.draw.polygon(self.screen,"grey",[posicion1[i],posicion2[i],posicion3[i]])
        pygame.draw.polygon(self.screen,"grey",[posicion4[i],posicion5[i],posicion6[i]])
        self.dibujar_elementos_menu()
        pygame.display.flip()
        pygame.time.wait(35)

    def animacion(self,posicion1,posicion2,posicion3,posicion4,posicion5,posicion6):
        for i in range(len(posicion1)):
            self._animacion(posicion1,posicion2,posicion3,posicion4,posicion5,posicion6,i)

        for i in range(len(posicion1)-1,0,-1):
            self._animacion(posicion1,posicion2,posicion3,posicion4,posicion5,posicion6,i)

    def dibujar_menu(self):
        self.screen.blit(self.fondo,(0,0))
        punto_1 = (centro_ancho - (ancho_Rect//2) - ancho_Tri,centro_alto)
        punto_2 = (centro_ancho - (ancho_Rect//2) - 20,centro_alto-(alto_Rect//2))
        punto_3 = (centro_ancho - (ancho_Rect//2) - 20,centro_alto+(alto_Rect//2))
        punto_4 = (centro_ancho + (ancho_Rect//2) + ancho_Tri,centro_alto)
        punto_5 = (centro_ancho + (ancho_Rect//2) + 20,centro_alto-(alto_Rect//2))
        punto_6 = (centro_ancho + (ancho_Rect//2) + 20,centro_alto+(alto_Rect//2))
        
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

    def _dibujar(self,texto):
        pygame.draw.circle(self.screen,"grey",(centro_ancho,centro_alto),radio)
        self.dibujo_Texto(texto,centro_ancho,centro_alto - tamaño_letra//2)

    def animacion_juego(self,texto,color):
        for i in range(20):
            self.screen.fill("purple")
            pygame.draw.circle(self.screen,color,(centro_ancho,centro_alto),radio+i)
            self._dibujar(texto)
            pygame.display.flip()
            pygame.time.wait(tiempo[self.inicio])

    def juego(self):
        self.resultado = 0
        for i in range(cantidad_numeros[self.inicio]):
            self.numero = random.randint(-50,50)
            self.resultado += self.numero
            self.animacion_juego(str(self.numero),colores[self.inicio])
        self.animacion_juego("=",colores[self.inicio])
        self.etapa = "respuestas"

    def respuesta(self):
        self.screen.fill("purple")
        respuesta = int(self.input) if self.input != "" else 0
        self._dibujar(self.input)
        if self.resultado == respuesta:
            self.animacion_juego(str(respuesta),"green")
            self.etapa = "menu"
        else:
            self.animacion_juego(self.input,"red")

    def dibujar(self):
        if self.etapa == "menu":
            self.dibujar_menu()
        
        if self.etapa == "juego":
            self.juego()
        
        if self.etapa == "respuestas":
            self.screen.fill("purple")
            self._dibujar(self.input)
        
        pygame.display.flip()

    def bucle_principal(self):

        pygame.key.start_text_input()

        while self.running:
            
            self.manejo_evento()
            
            self.reloj.tick(60)
            
            self.dibujar()

        pygame.key.stop_text_input()