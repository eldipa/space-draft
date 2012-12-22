import math

class Vector(object):
    def getX(self):
        raise NotImplementedError()

    def getY(self):
        raise NotImplementedError()

    def setX(self, x):
        raise NotImplementedError()

    def setY(self, y):
        raise NotImplementedError()

    x = property(getX, setX)
    y = property(getY, setY)

    def rotar(self, angulo):
        raise NotImplementedError()

    def getAngulo(self):
        raise NotImplementedError()

    def setAngulo(self, angulo):
        raise NotImplementedError()

    def getNorma(self):
        raise NotImplementedError()

    def setNorma(self, norma):
        raise NotImplementedError()

    norma = property(getNorma, setNorma)
    angulo = property(getAngulo, setAngulo)

    def getCopia(self):
        raise NotImplementedError()

    def asList(self):
        raise NotImplementedError()

    def asTuple(self):
        raise NotImplementedError()

    def asVectorPolar(self):
        raise NotImplementedError()

    def asVectorCartesiano(self):
        raise NotImplementedError()

    def __str__(self):
        return "x:"+str(self.x)+" y:"+str(self.y)+" norma:"+str(self.norma)+" angulo:"+str(self.angulo)

    def __add__(self, otroVector):
        resultado = self.getCopia()
        resultado += otroVector
        return resultado

    def __sub__(self, otroVector):
        resultado = self.getCopia()
        resultado -= otroVector
        return resultado

    def __mul__(self, escalar):
        resultado = self.getCopia()
        resultado *= escalar
        return resultado

    def __rmul__(self, escalar):
        return self*escalar

    def __iadd__(self, otroVector):
        self.x += otroVector.x
        self.y += otroVector.y

        return self

    def __isub__(self, otroVector):
        self.x -= otroVector.x
        self.y -= otroVector.y

        return self

    def __imul__(self, escalar):
        self.norma *= escalar
        return self

class VectorPolar(Vector):
    def __init__(self, norma=0, angulo=0):
        self._norma = norma
        self._angulo = angulo

    def getX(self):
        return round(self.norma * math.cos(self.angulo))

    def getY(self):
        return round(self.norma * math.sin(self.angulo))

    def setX(self, x):
        y = self.y
        self.norma = (x**2 + y**2) ** 0.5
        self.angulo = math.atan2(y, x)

    def setY(self, y):
        x = self.x
        self.norma = (x**2 + y**2) ** 0.5
        self.angulo = math.atan2(y, x)

    x = property(getX, setX)
    y = property(getY, setY)

    def rotar(self, angulo):
        self.angulo += angulo

    def getAngulo(self):
        if self.norma == 0:
            return 0
        else:
            return self._angulo

    def setAngulo(self, angulo):
        anguloReal = angulo - math.pi*2*int(angulo/(math.pi*2))
        self._angulo = anguloReal

    def getNorma(self):
        return self._norma

    def setNorma(self, norma):
        self._norma = norma

    norma = property(getNorma, setNorma)
    angulo = property(getAngulo, setAngulo)

    def getCopia(self):
        return VectorPolar( self.norma, self.angulo )

    def asList(self):
        return [self.norma, self.angulo]

    def asTuple(self):
        return (self.norma, self.angulo)

    def asVectorCartesiano(self):
        return VectorCartesiano( x = self.x, y = self.y)

    def asVectorPolar(self):
        return self.getCopia()

    def a__add__(self, otroVector):
        resultado = self.getCopia()
        resultado += otroVector

        return resultado

    def a__sub__(self, otroVector):
        resultado = self.getCopia()
        resultado -= otroVector

        return resultado

    def a__mul__(self, escalar):
        resultado = self.getCopia()
        resultado *= escalar

        return resultado

    def a__rmul__(self, escalar):
        return self*escalar

    def a__iadd__(self, otroVector):
        self.x+=otroVector.x
        self.y+=otroVector.y

        return self

    def a__isub__(self, otroVector):
        self.x-=otroVector.x
        self.y-=otroVector.y

        return self

    def a__imul__(self, escalar):
        self.norma *= escalar
        return self

class VectorCartesiano(Vector):
    def __init__(self, x=0, y=0):
        self.vector = [x,y]

    def getX(self):
        return self.vector[0]

    def getY(self):
        return self.vector[1]

    def setX(self, x):
        self.vector[0] = int(round(x))

    def setY(self, y):
        self.vector[1] = int(round(y))

    x = property(getX, setX)
    y = property(getY, setY)

    def rotar(self, angulo):
        seno = math.sin(angulo)
        coseno = math.cos(angulo)

        x = self.x
        self.x = (self.x*coseno) - (self.y*seno)
        self.y = (x*seno) + (self.y*coseno)

    def getNorma(self):
        return ( self.x**2 + self.y**2)**0.5

    def getAngulo(self):
        return math.atan2(self.y, self.x)

    def setAngulo(self, angulo):
        anguloDiferencial = self.angulo - angulo
        self.rotar(anguloDiferencial)

    def setNorma(self, norma):
        angulo = self.angulo
        self.x = norma * math.cos( angulo )
        self.y = norma * math.sin( angulo )

    norma = property(getNorma, setNorma)
    angulo = property(getAngulo, setAngulo)

    def getCopia(self):
        return VectorCartesiano( self.x, self.y )

    def asList(self):
        return [self.x, self.y]

    def asTuple(self):
        return (self.x, self.y)

    def asVectorPolar(self):
        return VectorPolar( norma = self.norma, angulo = self.angulo)

    def asVectorCartesiano(self):
        return self.getCopia()

    def a__add__(self, otroVector):
        resultado = self.getCopia()
        resultado += otroVector

        return resultado

    def a__sub__(self, otroVector):
        resultado = self.getCopia()
        resultado -= otroVector

        return resultado

    def a__mul__(self, escalar):
        resultado = self.getCopia()
        resultado *= escalar

        return resultado

    def a__rmul__(self, escalar):
        return self*escalar

    def a__iadd__(self, otroVector):
        self.x+=otroVector.x
        self.y+=otroVector.y

        return self

    def a__isub__(self, otroVector):
        self.x-=otroVector.x
        self.y-=otroVector.y

        return self

    def a__imul__(self, escalar):
        self.x= self.x * escalar
        self.y= self.y * escalar

        return self

