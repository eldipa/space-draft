import vector
import math

class Matriz3x3:
    def __init__(self, a11, a12, a13,
                        a21, a22, a23,
                        a31, a32, a33):
        self.matriz = (
                       (a11,a12,a13),
                       (a21,a22,a23),
                       (a31,a32,a33)
                       )

    def __str__(self):
        return str(self.matriz)

    def evaluar(self, dato):
        parametros = []
        for i in range(3):
            for j in range(3):
                parametros.append( self.__procesar(i, j, dato))

        return Matriz3x3( parametros[0], parametros[1], parametros[2],
                          parametros[3], parametros[4], parametros[5],
                          parametros[6], parametros[7], parametros[8])

    def __procesar(self, fila, columna, parametro):
        if callable(self.matriz[fila][columna]):
            return self.matriz[fila][columna](parametro)
        else:
            return self.matriz[fila][columna]

    def multiplicarVector(self, x_y):
        a1, a2 = x_y
        a3 = 0

        return (
                int(round(self.matriz[0][0]*a1 + self.matriz[0][1]*a2 + self.matriz[0][2]*a3)),
                int(round(self.matriz[1][0]*a1 + self.matriz[1][1]*a2 + self.matriz[1][2]*a3))
                )

def menosSin(rad):
    return math.sin(rad)*(-1)

matrizRotacionZ = Matriz3x3(math.cos, menosSin,0,math.sin,math.cos,0,0,0,1)

matrizRotacionY = Matriz3x3(math.cos, 0, math.sin, 0,1,0, menosSin,0,math.cos)

matrizRotacionX = Matriz3x3(1,0,0, 0, math.cos, menosSin, 0, math.sin, math.cos)

#
#n = matrizRotacionZ.evaluar(0)
#
#print str(matrizRotacionZ), str(n)
#
#print
#
#vec = vector.VectorCartesiano(1,0)
#
#vecRotado = matrizRotacionZ.evaluar(math.pi).multiplicarVector(vec)
#
#print vec, vecRotado
#
