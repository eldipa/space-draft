import unittest
import vector
import math

class VectorCartesianoTest(unittest.TestCase):
    def setUp(self):
        self.vectorDePrueba = self.crearVectorDePrueba(0, 0)

    def crearVectorDePrueba(self, x, y):
        return vector.VectorCartesiano(x,y)

    def chequearValores(self, x, y):
        self.assertTrue( self.vectorDePrueba.x == x )
        self.assertTrue( self.vectorDePrueba.y == y )

    def testSumaResta(self):
        self.chequearValores(0, 0)

        self.vectorDePrueba = self.vectorDePrueba + self.crearVectorDePrueba(5, 8)
        self.chequearValores(5, 8)

        self.vectorDePrueba = self.vectorDePrueba - self.crearVectorDePrueba(6, 9)
        self.chequearValores(-1, -1)

        self.vectorDePrueba = self.vectorDePrueba + self.crearVectorDePrueba(-1, 0.08)
        self.chequearValores(-2, -1)

        self.vectorDePrueba = self.vectorDePrueba - self.crearVectorDePrueba(2,-0.02)
        self.chequearValores(-4, -1)

        self.vectorDePrueba = self.vectorDePrueba + self.crearVectorDePrueba(4,0.9)
        self.chequearValores(0, 0)

    def testMultiplicacion(self):
        self.chequearValores(0, 0)

        self.vectorDePrueba = self.vectorDePrueba * 5
        self.chequearValores(0, 0)

        self.vectorDePrueba.x = 1
        self.vectorDePrueba.y = 2

        self.vectorDePrueba = self.vectorDePrueba * 5
        self.chequearValores(5, 10)

        self.vectorDePrueba = self.vectorDePrueba * (-1)
        self.chequearValores(-5, -10)

        self.vectorDePrueba = 2 * self.vectorDePrueba
        self.chequearValores(-10, -20)

        self.vectorDePrueba = self.vectorDePrueba * 1
        self.chequearValores(-10, -20)

        self.vectorDePrueba = self.vectorDePrueba * 1.5
        self.chequearValores(-15, -30)

        print
        print self.vectorDePrueba.x,self.vectorDePrueba.y, self.vectorDePrueba.norma, self.vectorDePrueba.angulo
        self.vectorDePrueba = self.vectorDePrueba * 0.5
        print self.vectorDePrueba.x,self.vectorDePrueba.y, self.vectorDePrueba.norma, self.vectorDePrueba.angulo
        self.chequearValores(-7, -15)

        self.vectorDePrueba = self.vectorDePrueba * 0
        self.chequearValores(0, 0)

    def testSumarmeRestarme(self):
        self.chequearValores(0, 0)

        self.vectorDePrueba += self.crearVectorDePrueba(5,8)
        self.chequearValores(5, 8)

        self.vectorDePrueba -= self.crearVectorDePrueba(6,9)
        self.chequearValores(-1, -1)

        self.vectorDePrueba += self.crearVectorDePrueba(-1, 0.08)
        self.chequearValores(-2, -1)

        self.vectorDePrueba -= self.crearVectorDePrueba(2,-1.02)
        self.chequearValores(-4, 0)

        self.vectorDePrueba += self.crearVectorDePrueba(4,1.9)
        self.chequearValores(0, 2)

    def testMultiplicarme(self):
        self.chequearValores(0, 0)

        self.vectorDePrueba *=  5
        self.chequearValores(0, 0)

        self.vectorDePrueba.x = 1
        self.vectorDePrueba.y = 2

        self.vectorDePrueba *=  5
        self.chequearValores(5, 10)

        self.vectorDePrueba *= (-1)
        self.chequearValores(-5, -10)

        self.vectorDePrueba *= 2
        self.chequearValores(-10, -20)

        self.vectorDePrueba *=  1
        self.chequearValores(-10, -20)

        self.vectorDePrueba *=  0
        self.chequearValores(0, 0)

    def testNorma(self):
        self.chequearValores(0, 0)

        self.assertTrue( self.vectorDePrueba.norma == 0)

        self.vectorDePrueba.x = 1
        self.vectorDePrueba.y = 0
        self.assertTrue( self.vectorDePrueba.norma == 1)

        self.vectorDePrueba.x = 0
        self.vectorDePrueba.y = 1
        self.assertTrue( self.vectorDePrueba.norma == 1)

        self.vectorDePrueba.x = -3
        self.vectorDePrueba.y = -4
        self.assertTrue( self.vectorDePrueba.norma == 5)

        self.vectorDePrueba.x = 1
        self.vectorDePrueba.y = 2
        self.assertTrue( self.vectorDePrueba.norma == 5**0.5)

    def testAdaptadores(self):
        self.chequearValores(0, 0)

        self.assertTrue( self.vectorDePrueba.asList() == [0,0])
        self.assertTrue( self.vectorDePrueba.asTuple() == (0,0))

        self.vectorDePrueba.x = 1
        self.vectorDePrueba.y = 2

        self.chequearValores(1, 2)
        self.assertTrue( self.vectorDePrueba.asList() == [1,2])
        self.assertTrue( self.vectorDePrueba.asTuple() == (1,2))

    def testRotaciones(self):
        self.chequearValores(0, 0)

        self.vectorDePrueba.rotar( math.pi*2.0 )
        self.chequearValores(0, 0)
        self.assertTrue( self.vectorDePrueba.angulo == 0)

        self.vectorDePrueba.rotar(55)
        self.chequearValores(0, 0)
        self.assertTrue( self.vectorDePrueba.angulo == 0)

        self.vectorDePrueba.x = 10
        self.vectorDePrueba.y = 0
        self.chequearValores(10, 0)
        self.assertTrue( self.vectorDePrueba.angulo == 0)

        self.vectorDePrueba.rotar( math.pi*2 )
        self.chequearValores(10, 0)
        self.assertTrue( self.vectorDePrueba.angulo == 0)

        self.vectorDePrueba.rotar( math.pi )
        self.chequearValores(-10, 0)
        self.assertTrue( self.vectorDePrueba.angulo == math.pi)

        self.vectorDePrueba.rotar( math.pi )
        self.chequearValores(10, 0)
        self.assertTrue( self.vectorDePrueba.angulo == 0)

        self.vectorDePrueba.rotar( math.pi/2.0 )
        self.chequearValores(0, 10)
        self.assertTrue( self.vectorDePrueba.angulo == math.pi/2.0)

        self.vectorDePrueba.rotar( math.pi/4.0 )
        self.chequearValores(
                             int(round(-10*math.cos(math.pi/4.0))),
                             int(round(10*math.sin(math.pi/4.0))))

        self.assertTrue( self.vectorDePrueba.angulo == (math.pi/4.0) + (math.pi/2.0))

        self.vectorDePrueba.rotar( (math.pi*5)/4.0 )
        self.chequearValores(10, 0)
        self.assertTrue( self.vectorDePrueba.angulo == 0)

