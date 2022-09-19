
from cmath import pi
from graphics.graphics import Object3D, Square
from quaternions.rotacion import RotacionQuad


def main():
    punto = Object3D(5.0, 5.0, 0.0)
    vector = Object3D(2.0, 0.0, 0.0)
    angulo = 90
    angulo = angulo * (pi / 180)

    q = RotacionQuad()
    q.RotarPunto(punto.coords, vector.coords, angulo)
    print("Punto Rotado:")
    punto.mostrar_coordenadas()

    cuadrado = Square(5.0, 5.0, 2.0)
    q.RotarCuadrado2D(cuadrado, vector.coords, angulo)
    print("Cuadrado Rotado: ")
    cuadrado.mostrar_coordenadas()

if __name__ == "__main__":
    main()

     