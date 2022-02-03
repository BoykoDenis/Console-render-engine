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

        matrix_premade = [[pointX - self.global_vector[0]], [pointY - self.global_vector[1]], [pointZ - self.global_vector[2]]]
        relative_vector = Matrix(dims = [3, 1], matrix = matrix_premade)
        relative_vector = self.convertion(relative_vector)
        relative_vector = relative_vector.get_matrix()
        return max(abs(relative_vector[0][0]) - self.width//2,
                   abs(relative_vector[1][0]) - self.lenght//2,
                   abs(relative_vector[2][0]) - self.hight//2)


    #def convert_from_global_2_local_cords():
    def calc_convert_matrix_kan_2_base(self):
        self.convertion_kan_2_base = Matrix.multiply_without_saving(self.base_vectors.calculate_inverse(), self.kanon)


    def convertion(self, relative_vector):
        self.calc_convert_matrix_kan_2_base()
        return Matrix.multiply_without_saving(self.convertion_kan_2_base, relative_vector)

    def rotate(self, axis, angle):
        self.base_vectors.rotate(axis, angle)


    






