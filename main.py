from ball import *
import random
balls,nb,r = [],5,30

def remove_overlap(b1,b2,angle):
    dx = b2.pos.x - b1.pos.x
    dy = b2.pos.y - b1.pos.y
    true_dist = b1.r + b2.r

    mx = py5.cos(angle)*true_dist - dx
    my = py5.sin(angle)*true_dist - dy

    b1.pos.x = b1.pos.x - mx
    b1.pos.y = b1.pos.y - my

    b2.pos.x = b2.pos.x + mx
    b2.pos.y = b2.pos.y + my

def collide(b1,b2):
    dx = b2.pos.x - b1.pos.x
    dy = b2.pos.y - b1.pos.y
    d = py5.sqrt(dx*dx + dy*dy)

    min_dist = b1.r+b2.r
    return d<min_dist

def collision_angle(b1,b2):
    dx = b2.pos.x - b1.pos.x
    dy = b2.pos.y - b1.pos.y

    return py5.atan2(dy,dx)

def update_vel(b1,b2,angle):

    #store velocities to make calculations easy
    v1x, v1y = b1.vel.x, b1.vel.y
    v2x, v2y = b2.vel.x, b2.vel.y

    #rotate velocities so we can only handle one component of velocities
    v1xr = v1x*py5.cos(angle) - v1y*py5.sin(angle)
    v1yr = v1x*py5.sin(angle) + v1y*py5.cos(angle)

    v2xr = v2x*py5.cos(angle) - v2y*py5.sin(angle)
    v2yr = v2x*py5.sin(angle) + v2y*py5.cos(angle)

    #find new velocities
    #apllying two conservations
    #Conservation of movement quantity
    #Conservation of kinetic energy
    v1xn, v1yn = v2xr, v1yr
    v2xn, v2yn = v1xr, v2yr

    #rotate them back to have final velocities 
    v1xf = v1xn*py5.cos(angle) + v1yn*py5.sin(angle)
    v1yf = v1yn*py5.cos(angle) - v1xn*py5.sin(angle)

    v2xf = (v2xn*py5.cos(angle) + v2yn*py5.sin(angle))*0.5
    v2yf = (v2yn*py5.cos(angle) - v2xn*py5.sin(angle))*0.5

    b1.vel = py5.Py5Vector(v1xf,v1yf)
    b2.vel = py5.Py5Vector(v2xf,v2yf)

def handle_collisions():
    global balls, nb
    for i in range(nb):
        for j in range(nb):
            if i!=j:
                if collide(balls[i],balls[j]):
                    angle = collision_angle(balls[i],balls[j])
                    remove_overlap(balls[i],balls[j],angle)
                    update_vel(balls[i],balls[j],angle)

def create_balls():
    global balls,nb,r
    balls = []
    for i in range(nb):
        x = random.randint(1,1+(py5.width-r)//r)*r
        y = random.randint(1,1+(py5.height-r)//r)*r
        c = (py5.random(255),py5.random(255),py5.random(255))
        balls.append(Ball(x,y,r))
        balls[i].col = c

    balls[0].pos = py5.Py5Vector(r,r)
    balls[0].col = (255,255,255)
    balls[0].vel = py5.Py5Vector(50,50)

def draw_balls():
    global balls,nb
    for ball in balls:
        ball.show()
        ball.move()
    handle_collisions()

def setup():
    global balls,nb,r
    py5.size(800,600)
    create_balls()

def mouse_pressed():
    create_balls()

def draw():
    global balls,nb
    py5.background(10,10,20)

    draw_balls()

py5.run_sketch()


