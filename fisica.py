import vector

class ObjetoFisico(object):
    def __init__(self, posicionX=0, posicionY=0, normaVelocidad = 0, anguloVelocidad = 0, masa = 1 ):
        self.vectorPosicion = Posicion(posicionX,posicionY)
        self.vectorVelocidad = Velocidad(normaVelocidad, anguloVelocidad)

        self.masa = masa

    def getPosicion(self):
        return self.vectorPosicion

    def rotarDireccion(self, angulo):
        self.vectorVelocidad.rotar(angulo)

    def aumentarModuloVelocidad(self, aumento):
        self.vectorVelocidad.norma += aumento

    def getVelocidad(self):
        return self.vectorVelocidad

    def aplicarFuerza(self, unVector):
        self.vectorVelocidad += unVector*(1.0/self.masa)

    posicion = property(getPosicion)
    velocidad = property(getVelocidad)

    def mover(self):
        self.vectorPosicion += self.vectorVelocidad #.asVectorCartesiano()

class Posicion(vector.VectorCartesiano):
    def __init__(self, x=0, y=0):
        vector.VectorCartesiano.__init__(self, x, y)

class Velocidad(vector.VectorPolar):
    def __init__(self, norma=0, angulo=0):
        vector.VectorPolar.__init__(self, norma, angulo)

