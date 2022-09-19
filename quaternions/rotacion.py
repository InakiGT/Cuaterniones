from cmath import cos, sin, sqrt

from graphics.graphics import Square

class RotacionQuad:
    def __init__(self):
        self.s = 0.0 # Parte escalar
        self.v = [0.0, 0.0, 0.0] # Parte Vectorial

    def __Normalizar(self, vector):
        op = vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]
        r = sqrt(op)
        if r != 0.0:
            vector[0] /= r
            vector[1] /= r
            vector[2] /= r
        else:
            print("Vector invalido para operar")
            quit()
        
    def RotarPunto(self, punto, vector, angulo):
        rr = [0.0, 0.0, 0.0]

        w = sin(angulo / 2) # Parte real
        self.__Normalizar(vector)
        self.s = cos(angulo / 2)

        self.v[0] = vector[0] * w
        self.v[1] = vector[1] * w
        self.v[2] = vector[2] * w

        a = self.s * self.s - self.v[0] * self.v[0] - self.v[1] * self.v[1] - self.v[2] * self.v[2]
        b = 2 * (self.v[0] * punto[0] + self.v[1] * punto[1] +self.v[2] * punto[2])
        rr[0] = a * punto[0] + b * self.v[0] + 2 * self.s * (self.v[1] * punto[2] - self.v[2] * punto[1])
        rr[1] = a * punto[1] + b * self.v[1] + 2 * self.s * (self.v[2] * punto[0] - self.v[0] * punto[2])
        rr[2] = a * punto[2] + b * self.v[2] + 2 * self.s * (self.v[0] * punto[1] - self.v[1] * punto[0])
        punto[0] = rr[0]
        punto[1] = rr[1]
        punto[2] = rr[2]

    def RotarCuadrado2D(self, cuadrado: Square, vector, angulo):
        self.RotarPunto(cuadrado.coords, vector, angulo)
        self.RotarPunto(cuadrado.first_point_coords, vector, angulo)
        self.RotarPunto(cuadrado.second_point_coords, vector, angulo)
        self.RotarPunto(cuadrado.third_point_coords, vector, angulo)
        self.RotarPunto(cuadrado.fourth_point_coords, vector, angulo)