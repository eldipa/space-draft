import test_vector_cartesiano
import vector

class VectorPolarTest( test_vector_cartesiano.VectorCartesianoTest):
    def crearVectorDePrueba(self, x, y):
         unVector = vector.VectorPolar()

         unVector.x = x
         unVector.y = y

         return unVector

    def testAdaptadores(self):
        self.chequearValores(0, 0)

        self.assertTrue( self.vectorDePrueba.asList() == [0,0])
        self.assertTrue( self.vectorDePrueba.asTuple() == (0,0))

        self.vectorDePrueba.x = 1
        self.vectorDePrueba.y = 2

        self.chequearValores(1, 2)
        self.assertTrue( self.vectorDePrueba.asList() == [self.vectorDePrueba.norma,
                                                          self.vectorDePrueba.angulo])
        self.assertTrue( self.vectorDePrueba.asTuple() == (self.vectorDePrueba.norma,
                                                          self.vectorDePrueba.angulo))

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

        self.vectorDePrueba = self.vectorDePrueba * 0.5
        self.chequearValores(-8, -15)

        self.vectorDePrueba = self.vectorDePrueba * 0
        self.chequearValores(0, 0)

