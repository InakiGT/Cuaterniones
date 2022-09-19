
# Genera un punto en las 3 dimensiones del plano
class Object3D:
    def __init__(self, center_x_coord: float, center_y_coord: float, center_z_coord: float):
        self.coords = [ center_x_coord, center_y_coord, center_z_coord ]

    def mostrar_coordenadas(self):
        print("Punto:", self.coords)

# Genera un punto en las 3 dimensiones del plano, pero sin profundidad
class Object2D(Object3D):
    def __init__(self, center_x_coord: float, center_y_coord: float):
        Object3D.__init__(self, center_x_coord, center_y_coord, 0.0)

# Genera las 5 coordenadas de un cuadrado en el plano, según el tamaño indicado en Unidades
class Square(Object2D):
    def __init__(self, center_x_coord: float, center_y_coord: float, size: float):
        Object2D.__init__(self, center_x_coord, center_y_coord)
        self.size = size
    
        if not(1 / 2 * size > self.coords[0] or 1 / 2 * size > self.coords[1]):
            self.first_point_coords   = [ self.coords[0] - 1/2 * self.size, self.coords[1] - 1/2 * self.size, 0.0 ]
            self.second_point_coords  = [ self.coords[0] + 1/2 * self.size, self.coords[1] + 1/2 * self.size, 0.0 ]
            self.third_point_coords   = [ self.coords[0] + 1/2 * self.size, self.coords[1] - 1/2 * self.size, 0.0 ]
            self.fourth_point_coords  = [ self.coords[0] - 1/2 * self.size, self.coords[1] + 1/2 * self.size, 0.0 ]
        else:
            print("No se puede crear un cuadrado con esas dimensiones")
            quit()
    
    def mostrar_coordenadas(self):
        print("Centro:", self.coords, "Vertice 1:", self.first_point_coords, "Vertice 2:", self.second_point_coords,"Vertice 3", self.third_point_coords, "Vertice 4:", self.fourth_point_coords)