from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
Entity.default_shader = lit_with_shadows_shader

player = FirstPersonController()
Sky(color = color.light_gray)

class Cubo(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            scale = (1,1),
            origin_y = -.5,
            collider = 'box',
            color = color.lime,
            texture = 'grass',
        )
    
    def input(self, key):
         if self.hovered:
            if key == 'left mouse down':
                cubo = Cubo(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)


player.position = Vec3(0,10,0)

def input(key):
    if key == 'escape':
        quit()

chunksize = 32

for z in range(chunksize):
    for x in range (chunksize):
        ground = Cubo(position=(x,0,z))


def update():
    pass

app.run()