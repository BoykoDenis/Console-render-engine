import os
import math
from tkinter import Frame
from matrix import Matrix

class Camera:
    def __init__(self, position, scene):

        self.position_vector = position #global position
        self.camera_base = Matrix(dims = [3, 3], matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) # camera cords system relative to camera location and rotation
        self.camera_vector = [1, 0, 0] # camera view direction
        self.convertion_matrix_base_2_kan = Matrix()
        self.scene = scene
        self.raylimit = 5 #raymarching limit per pixel
        self.resolution = [51, 35]
        self.total_pixels = self.resolution[0]*self.resolution[1]
        self.complited_pixels = 0
        self.centerX = self.resolution[0] // 2
        self.centerY = self.resolution[1] // 2
        self.eyedistance = 10
        self.frame = [['.' for _ in range(self.resolution[0])] for _ in range(self.resolution[1])]
        self.distance_factor = 0.1

    def ray_marching(self, camera_scale):

        for ry in range(0, self.resolution[1]):
            for rx in range(0, self.resolution[0]):
                px = x = rx
                py = y = ry
                x = (self.centerX - px) * camera_scale
                y = (self.centerY - py) * camera_scale
                z = self.eyedistance
                camera_ray_base_cord_vector = Matrix(dims = [3, 1], matrix=[[x], [y], [z]])
                vector = Matrix.multiply_without_saving(self.camera_base, camera_ray_base_cord_vector).get_matrix()
                x, y, z = vector[0][0], vector[1][0], vector[2][0]

                last_size = self.vector_size(x, y, z)
                scale = 1
                for i in range(self.raylimit):
                    distance = self.__min_distance(x, y, z)

                    if distance <= self.distance_factor:
                        self.frame[py][px] = '#'
                        self.complited_pixels += 1
                        break

                    scale = last_size + distance / last_size
                    x, y, z = x*scale, y*scale, z*scale
                    last_size += distance



    def __min_distance(self, x, y, z):
        minimal = float('inf')
        for object in self.scene:
            distance = object.distance(x, y, z)
            if distance < minimal:
                minimal = distance
        return minimal #TODO implement normal vector returnal




    def next_frame(self):
        os.system('cls')
        for row in self.frame:
            for col in row:
                print(col, end = ' ')
            print()
        self.reset_frame()



    def vector_size(self, x, y, z):
        return (x**2 + y**2 + z**2)**0.5


    def calc_convert_matrix_kan_2_base(self):
        self.convertion_matrix = Matrix.multiply_without_saving(self.base_vectors.calculate_inverse(), self.kanon)


    def convertion(self, relative_vector):
        self.calc_convert_matrix_kan_2_base()
        return Matrix.multiply_without_saving(self.convertion_kan_2_base, relative_vector)


    def reset_frame(self):
        for x in range(len(self.frame)):
            for y in range(len(self.frame[0])):
                self.frame[x][y] = '.'