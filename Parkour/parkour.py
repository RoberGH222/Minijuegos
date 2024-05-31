from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader

app = Ursina(borderless=False)
Entity.default_shader = basic_lighting_shader

player = FirstPersonController()
Sky(texture='background.jpg')
background_music = Audio('kart-mario.mp3', loop=True)

class Cubo(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            scale = (1,1),
            origin_y = -.5,
            color = color.pink,
            collider = 'box',     
        )

player.position = Vec3(0,4,0)
Cubo(position=(0,0,0))
Cubo(position=(10,0,0))
Cubo(position=(20,0,0))
Cubo(position=(30,0,0))


def input(key):
    if key == 'escape':
        quit()

green_cubes = []
for z in range(10):
    x = random.randint(1,2)
    cubo = Cubo(position=(x,0,z))
    if z == 9:
        cubo.color = color.green
        green_cubes.append(cubo)

for z in range(20):
    x = random.randint(10,13)
    cubo = Cubo(position=(x,0,z))
    if z == 19:
        cubo.color = color.green
        green_cubes.append(cubo)

for z in range(30):
    x = random.randint(20,24)
    cubo = Cubo(position=(x,0,z))
    if z == 29:
        cubo.color = color.green
        green_cubes.append(cubo)

for z in range(40):
    x = random.randint(30,35)
    cubo = Cubo(position=(x,0,z))
    if z == 39:
        cubo.color = color.green
        green_cubes.append(cubo)

ground = Entity(model='plane', collider='box', scale=64, color=color.light_gray)
ground.position = Vec3(0,-10,0)

def update():

    for cubo in green_cubes:
        if round(player.position.x) == round(cubo.position.x) and round(player.position.z) == round(cubo.position.z):
            player.position = Vec3(round(cubo.position.z)+1,10,0)
            print(Vec3(round(cubo.position.z)+1,10,0))

    if (player.position.y <= -5):
        player.position = Vec3(0,10,0)

background_music.play()
app.run()