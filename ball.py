import py5
friction = -0.005

class Ball:
    def __init__(self, x, y, r):
        self.pos = py5.Py5Vector(x,y)
        self.vel = py5.Py5Vector(0,0)
        self.acc = py5.Py5Vector(0,0)

        self.r = r
        self.col = (py5.random(255),py5.random(255),py5.random(255))

    def handle_boundary_collision(self):
        if self.pos.x<self.r:
            self.pos.x = self.r
            self.vel.x = -self.vel.x
        elif self.pos.x>py5.width-self.r:
            self.pos.x = py5.width-self.r
            self.vel.x = -self.vel.x
        if self.pos.y<self.r:
            self.pos.y = self.r
            self.vel.y = -self.vel.y
        elif self.pos.y>py5.height-self.r:
            self.pos.y = py5.height-self.r
            self.vel.y = -self.vel.y
                
    def move(self):
        self.vel.x = self.vel.x + self.acc.x
        self.vel.y = self.vel.y + self.acc.y

        self.vel.x = self.vel.x + self.vel.x*friction
        self.vel.y = self.vel.y + self.vel.y*friction

        self.pos.x = self.pos.x + self.vel.x
        self.pos.y = self.pos.y + self.vel.y


        self.handle_boundary_collision()
    
    def show(self):
        py5.fill(*self.col)
        py5.ellipse(self.pos.x,self.pos.y,self.r*2,self.r*2)

