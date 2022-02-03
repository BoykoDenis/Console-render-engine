from re import X
from camera import Camera
from Box import Box
x = 8
#object1 = Box(6, 0, 0, x, x, x)
#object2 = Box(0, 6, 0, x, x, x)
object3 = Box(0, 0, 6, x, x, x)
#object3.rotate('x', 10)
#object4 = Box(-6, 0, 0, x, x, x)
#object5 = Box(0, -6, 0, x, x, x)
#object6 = Box(0, 0, -6, x, x, x)
scene = [object3]
cam = Camera([0, 0, 0], scene)
#cam.next_frame()
while True:
    cam.ray_marching(0.3)
    cam.next_frame()
    #object3.rotate('x', 10)
    object3.rotate('z', 10)

