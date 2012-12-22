import fisica
import pygame
import math
import random

import algebra

import actores

class Nave(fisica.ObjetoFisico):
    def __init__(self):
        fisica.ObjetoFisico.__init__(self,
                                     posicionX=50,
                                     posicionY=50,
                                     masa=5)

        self.__direccion = fisica.vector.VectorPolar(norma = 4)


    def getAnguloDefault(self):
        return math.pi/40

    def girarSentidoHorario(self):
        self.__direccion.rotar( -self.getAnguloDefault() )

    def girarSentidoAntiHorario(self):
        self.__direccion.rotar( self.getAnguloDefault() )

    def acelerar(self):
        self.aplicarFuerza( self.__direccion )

    def disparar(self, listaDeDisparos):
        listaDeDisparos.append( actores.Proyectil(self.posicion,self.__direccion))

    def dibujar(self):
         direccionOrtogonal = fisica.vector.VectorCartesiano( -self.__direccion.y, self.__direccion.x)

         base = [ (self.posicion - direccionOrtogonal).asTuple(),
                 (self.posicion + direccionOrtogonal).asTuple()]

         punta = (self.__direccion.asVectorCartesiano()*3 + self.posicion).asTuple()

         #dibuja la base de la nave
         pygame.draw.line( pygame.display.get_surface(),
                           pygame.Color("red"),
                           base[0],
                           base[1],
                           1)

         #dibuja los laterales de la nave
         pygame.draw.line( pygame.display.get_surface(),
                           pygame.Color("white"),
                           punta,
                           base[0],
                           1)
         pygame.draw.line( pygame.display.get_surface(),
                           pygame.Color("white"),
                           punta,
                           base[1],
                           1)

class Proyectil(fisica.ObjetoFisico):
    def __init__(self, unaPosicion, unVectorDireccion):
        fisica.ObjetoFisico.__init__(self,
                                     posicionX=unaPosicion.x,
                                     posicionY=unaPosicion.y,
                                     normaVelocidad = 16,
                                     anguloVelocidad = unVectorDireccion.angulo,
                                     masa=1)

        self.tiempoDeVida = 20

    def moverAhora(self):
        self.mover()
        self.tiempoDeVida -= 1

    def dibujar(self):
        pygame.draw.line( pygame.display.get_surface(),
                          pygame.Color("green"),
                          self.posicion.asTuple(),
                          ((self.posicion + self.velocidad*(0.25)).asVectorCartesiano()).asTuple(),
                          1)

class Asteroide(fisica.ObjetoFisico):
    def __init__(self, unaPosicion, moduloVelocidad, masa):
        fisica.ObjetoFisico.__init__(self,
                                     posicionX = unaPosicion.x,
                                     posicionY = unaPosicion.y,
                                     normaVelocidad = moduloVelocidad,
                                     anguloVelocidad = random.uniform(0, 2*math.pi),
                                     masa = masa)


    def dibujar(self):
        pygame.draw.circle(pygame.display.get_surface(),
                           pygame.Color("white"),
                           self.posicion.asTuple(),
                           self.masa,
                           1)

    def girarAleatoriamente(self):
        self.velocidad.angulo =  random.uniform(0, 2*math.pi)

class Escenario:
    def __init__(self, ancho, alto):
        self.fondo = pygame.Surface( (ancho,alto) )
        self.fondo = self.fondo.convert()
        self.fondo.fill( (0,0,0) )

    def dibujar(self):
        pygame.display.get_surface().blit( self.fondo, (0,0) )

