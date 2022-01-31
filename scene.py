from camera import Camera
from Box import Box

object1 = Box(10, 0, 0, 3, 3, 3)
scene = [object1]
cam = Camera([0, 0, 0], scene)
cam.next_frame()
cam.ray_marching(0.1)
cam.next_frame()