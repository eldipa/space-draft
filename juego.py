from pygame import *
import actores

import random
import math
import fisica

class Game:
    def __init__(self):
        self.ancho = 500
        self.alto = 500
        self.nivel = 0

        init()
        display.set_mode((self.ancho, self.alto))

        self.nave = actores.Nave()

        self.asteroides = []
        self.disparos = []

        self.escenario = actores.Escenario(self.ancho,self.alto)
        self.estadoJuego = "continuando"

    def crearAsteroides(self):
        self.asteroides = []
        for n in range(self.nivel * 3):
            x = random.randint(0,self.ancho)
            y = random.randint(0,self.alto)
            m = 10 + (5 * random.randint(1, self.nivel+1))
            self.asteroides.append(actores.Asteroide(fisica.Posicion(x, y),1, m))

    def gameLoop(self):
        clock = time.Clock()
        while self.estadoJuego == "continuando":
            self.nivel += 1
            print "Nivel", self.nivel
            self.crearAsteroides()

            while self.estadoJuego == "continuando":
                clock.tick(30)

                self.nave.mover()
                self.logicaDeAsteoirdes()
                self.logicaDeDisparos()

                self.procesar()
                self.dibujar()

                if not self.asteroides:
                    print "Pasas al siguiente nivel"
                    break

            if self.estadoJuego == "reiniciar":
                self.estadoJuego = "continuando"
                self.nivel = 0
                self.nave = actores.Nave()

    def dibujar(self):
        self.escenario.dibujar()
        self.nave.dibujar()

        for asteroide in self.asteroides:
            asteroide.dibujar()

        for disparo in self.disparos:
            disparo.dibujar()

        display.flip()

    def logicaDeDisparos(self):
        disparosARemover = []

        for disparo in self.disparos:
            disparo.moverAhora()

            if disparo.tiempoDeVida <= 0:
                disparosARemover.append(disparo)

            if disparo.posicion.x <= 0:
                disparo.posicion.x = self.ancho
            elif disparo.posicion.x >= self.ancho:
                disparo.posicion.x = 0

            if disparo.posicion.y <= 0:
               disparo.posicion.y = self.alto
            elif disparo.posicion.y >= self.alto:
                disparo.posicion.y = 0

        for disparoAgotado in disparosARemover:
            self.disparos.remove(disparoAgotado)

    def logicaDeAsteoirdes(self):
        for asteroide in self.asteroides[:]:
            if (self.nave.posicion - asteroide.posicion).norma < (asteroide.masa - 2):
                print "Boom! Has perdido!"
                self.estadoJuego = "reiniciar"

            for disparo in self.disparos:
                if (disparo.posicion - asteroide.posicion).norma < asteroide.masa:

                    self.asteroides.remove(asteroide)
                    if asteroide.masa > 8:
                        self.asteroides.append(actores.Asteroide(asteroide.posicion,
                                                                 asteroide.velocidad.norma + 1,
                                                int(round(asteroide.masa / 2))))
                        self.asteroides.append(actores.Asteroide(asteroide.posicion,
                                                                 asteroide.velocidad.norma + 1,
                                                int(round(asteroide.masa / 2))))
                    break

            if asteroide.posicion.x <= 0:
                asteroide.posicion.x = self.ancho
            elif asteroide.posicion.x >= self.ancho:
                asteroide.posicion.x = 0

            if asteroide.posicion.y <= 0:
                asteroide.posicion.y = self.alto
            elif asteroide.posicion.y >= self.alto:
                asteroide.posicion.y = 0

            asteroide.mover()


    def procesar(self):
        for evento in event.get():
            if evento.type == QUIT:
                self.estadoJuego = "finalizado"
            elif evento.type == KEYDOWN:
                if evento.key == K_LCTRL:
                     self.nave.disparar(self.disparos)
                if evento.key == K_z:
                    self.nave.posicion.x = random.randint(0,self.ancho)
                    self.nave.posicion.y = random.randint(0, self.alto )

                elif evento.key == K_DOWN:
                    pass

            elif evento.type == KEYUP:
                if (evento.key == K_UP) or (evento.key == K_DOWN):

                    pass

        if (key.get_pressed()[K_UP] == 1):
            self.nave.acelerar()
            if self.nave.velocidad.norma > 12:
                self.nave.velocidad.norma = 12
        elif (key.get_pressed()[K_DOWN] == 1) and (self.nave.velocidad.norma > -4):
           pass

        if key.get_pressed()[K_LEFT] == 1:
            self.nave.girarSentidoHorario()
        elif key.get_pressed()[K_RIGHT] == 1:
            self.nave.girarSentidoAntiHorario()

        if self.nave.posicion.x <= 0:
                self.nave.posicion.x = self.ancho
        elif self.nave.posicion.x >= self.ancho:
                self.nave.posicion.x = 0

        if self.nave.posicion.y <= 0:
               self.nave.posicion.y = self.alto
        elif self.nave.posicion.y >= self.alto:
                self.nave.posicion.y = 0

print "Space-Draft!"
print
print "Shoot: Left Ctrl"
print "Teleport: Z"
print
juego = Game()
juego.gameLoop()
