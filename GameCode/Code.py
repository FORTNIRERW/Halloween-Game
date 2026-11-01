import raylib as rl
from pyray import *
import random
class Pumpkin:
    def __init__(self,pos_x,pos_y,texture,size,):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = random.randrange(1,20)
        self.points = random.randrange(50,1000)
        self.texture = texture
        self.size = size
        self.alive = True
        self.box = Rectangle(self.pos_x, self.pos_y,100,100)
        self.lose_points = False
        self.gain_points = False
    def Spawn(self):
        if self.alive == True:
            draw_rectangle_rec(self.box,ORANGE)
            self.box = Rectangle(self.pos_x, self.pos_y,100,100)
            self.pos_y +=self.speed
        if self.pos_y <= 750:
            self.lose_points = True
            return -(self.lose_points)
        if is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
            if check_collision_recs(player1.collisionbox,self.box):
                self.alive = False
                return self.gain_points

class Player:
    def __init__(self,size):
        self.position = get_mouse_position()
        self.size = size
        self.rotation = 0
        self.collisionbox = Rectangle(self.position.x,self.position.y,self.size,self.size)
        self.decrease = False
        self.increase = False
        self.originalsize = size
        self.rotationfactor = 2
        self.orioginalrotation = 0
    def draw(self):
        self.position = get_mouse_position()
        self.collisionbox = Rectangle(self.position.x-self.size/2,self.position.y-self.size/2,self.size,self.size)
        draw_rectangle_pro(Rectangle(self.position.x+(self.size/10),self.position.y+(self.size/10),self.size,self.size),Vector2(self.size/2,self.size/2),self.rotation,RED)
        self.rotation+=2
    def shoot(self):
        self.collisionbox = Rectangle(self.position.x,self.position.y,self.size,self.size)
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            self.rotation+=self.rotationfactor
            if self.size >= 30:
                self.rotationfactor+=0.2
                self.size -= 3
        elif self.size <= self.originalsize:
            self.rotationfactor = self.orioginalrotation
            self.size += 4



player1 = Player(100)
pumpkin = Pumpkin(500,0,"textureNone",50)
pumpkins = []
init_window(1280,720,"BOB")
set_target_fps(60)
hide_cursor()
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    player1.draw()
    player1.shoot()
    pumpkin.Spawn()
    end_drawing()
close_window()
                    


