from ursina import *

app = Ursina()

window.color = color.white

table = Entity(
    model = 'cube',
    color = color.green,
    texture = 'grass',
    scale = (2,1,3),
    rotation = (90,0,0)
)

label_player1 = Text(
    text = f'Score: {0}',
    color = color.black,
    position = (0.3, -0.1, -1)
)

label_player2 = duplicate(label_player1, y = 0.1)

ball = Entity(
    model = 'sphere',
    color = color.cyan,
    scale = 0.1,
    z = -1,
    collider = 'sphere'
    )

player1 = Entity(
    model = 'cube',
    color = color.cyan,
    collider = 'box',
    scale = (0.6, 0.1, 1),
    position = (0, -1.4, -1)
)

player2 = duplicate(player1, y=1.4)

speed_x = speed_y = 1
score_player1 = score_player2 = 0
def input(key):
    if key == 'escape':
        quit()

def update():
    global speed_y,speed_x,score_player1,score_player2
    ball.x += speed_x * time.dt 
    ball.y += speed_y * time.dt 

    if abs(ball.x) > 0.9:
        speed_x = -speed_x
    if ball.y > 1.4:
        ball.x = ball.y = 0
        speed_x = 1
        speed_y = 1
        score_player1 += 1
        label_player1.text = f'Score: {score_player1}'
    if ball.y < -1.4:
        ball.x = ball.y = 0
        speed_x = -1
        speed_y = -1
        score_player2 += 1
        label_player2.text = f'Score: {score_player2}'

    
    player1.x += held_keys['d'] * time.dt
    player1.x -= held_keys['a'] * time.dt
    player2.x += held_keys['right arrow'] * time.dt
    player2.x -= held_keys['left arrow'] * time.dt

    if ball.intersects().hit:
        speed_y = -speed_y
        speed_x *= 1.1 
        speed_y *= 1.1 

camera.orthographic = True
camera.fov = 4
app.run()