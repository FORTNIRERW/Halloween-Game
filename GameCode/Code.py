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
        self.box = Rectangle(pos_x, pos_y,100,100)
        self.lose_points = False
        self.gain_points = False
    def Spawn(self):
        if self.alive == True:
            draw_rectangle_rec(self.box,ORANGE)
            pos_y -=self.speed
        if pos_y <= 750:
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
        self.frame = 1
        self.interval = 2
        self.increment = -1
        self.rotation = 0
        self.collisionbox = Rectangle(self.position.x,self.position.y,self.size,self.size)
        self.decrease = False
        self.increase = False
        self.originalsize = size
    def draw(self):
        self.position = get_mouse_position()
        self.collisionbox = Rectangle(self.position.x-self.size/2,self.position.y-self.size/2,self.size,self.size)
        draw_rectangle_rec(self.collisionbox,RED)
    def shoot(self):
        self.collisionbox = Rectangle(self.position.x,self.position.y,self.size,self.size)
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            if self.decrease == True:
                if  self.frame % self.interval == 0:
                    self.size += self.increment
                    self.frame = 0
                self.frame +=1
                if self.size <= self.originalsize/2:
                    self.decrease = False
            elif self.increase == False:
                    if  self.frame % self.interval == 0:
                        self.size += self.increment
                        self.frame = 0
                    self.frame +=1
                    if self.size >= self.originalsize:
                        self.size = self.originalsize
player1 = Player(100)
pumpkins = []
init_window(1280,720,"BOB")
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    player1.draw()
    if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
        if player1.size >= 10:
            player1.size -= 0.1
    elif player1.size <= player1.originalsize:
        player1.size += 0.1
    end_drawing()
close_window()
                    


