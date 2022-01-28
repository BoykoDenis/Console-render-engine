from matrix import Matrix

class Box:
    def __init__(self, positionX, positionY, positionZ, width, lenght, hight) -> None:
        self.global_vector = [positionX, positionY, positionZ]
        self.width = width
        self.lenght = lenght
        self.hight = hight
        self.base_vectors = Matrix(dims = [3, 3], matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.kanon = Matrix(dims = [3, 3], matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.convertion_kan_2_base = Matrix()
        self.convertion_base_2_kan = Matrix()
        self.rotX = 0
        self.rotY = 0
        self.rotZ = 0
        self.animation = False


    def distance(self, pointX, pointY, pointZ):

        relative_vector = [self.global_vector[0] - pointX, self.global_vector[1] - pointY, self.global_vector[2] - pointZ]

        return max(abs(self.global_vector[0] - pointX) - self.width//2,
                   abs(self.global_vector[1] - pointY) - self.lenght//2,
                   abs(self.global_vector[2] - pointZ) - self.hight//2)


    #def convert_from_global_2_local_cords():
    def calc_convert_matrix_kan_2_base(self):
        self.convertion_matrix = Matrix.multiply_without_saving(self.base_vectors.calculate_inverse(), self.kanon)


    def convertion(self, point_vector_global):




