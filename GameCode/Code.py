import raylib as rl
from pyray import *
import random

damage = 2
score = 0
class Pumpkin:
    def __init__(self,pos_x,pos_y,texture,size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = random.randrange(1,20)
        self.points = random.randrange(50,1000)
        self.texture = texture
        self.size = size
        self.alive = True
        self.box = Rectangle(self.pos_x, self.pos_y,self.size,self.size)
        self.lose_points = False
        self.gain_points = False
        self.health = random.randrange(10,20)
        self.max_health = self.health
        self.alpha = 255
        self.status = True
    def Spawn(self):
        global damage
        if self.alive == True:
            draw_rectangle_rec(self.box,Color(100,50,100,self.alpha))
            self.box = Rectangle(self.pos_x, self.pos_y,self.size,self.size) # main problem is the way it scales down is not centered
            self.pos_y +=self.speed
        if self.pos_y >= 1080:
            self.lose_points = True
            self.alive = False
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            if check_collision_recs(player1.collisionbox,self.box):
                self.health -=damage
                self.alpha -=int(255/self.max_health)
                self.size -=5
                if self.health <= 0 or self.alpha <=30:
                    self.alive = False
                    self.gain_points = True
    def award_points(self):
        global score
        if self.status == True:
            if self.alive == False:
                if self.gain_points == True:
                    score +=10 #use the floating thingy to make the score float up &&& add the particles
                else:
                    score -=10 # use the floating and shake thingy
                
                self.status = False

class Player:
    def __init__(self,size):
        self.position = get_mouse_position()
        self.size = size
        self.size_box = size/5
        self.rotation = 0
        self.collisionbox = Rectangle(self.position.x,self.position.y,self.size,self.size)
        self.decrease = False
        self.increase = False
        self.originalsize = size
        self.rotationfactor = 2
        self.orioginalrotation = 0
    def draw(self):
        self.position = get_mouse_position()
        self.collisionbox = Rectangle(self.position.x-self.size_box/2,self.position.y-self.size_box/2,self.size_box,self.size_box)
        draw_rectangle_pro(Rectangle(self.position.x,self.position.y,self.size,self.size),Vector2(self.size/2,self.size/2),self.rotation,RED)
        draw_rectangle_rec(self.collisionbox,BLUE)
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

class Cooldown:
    def __init__(self,time):
        self.time = time
        self.frame = 0
        self.frames_to_go = self.time*60
        self.started = False
        self.ended = False
    def Start_timer(self):
        self.started = True
        self.frame +=1
        if self.frame >= self.frames_to_go:
            self.ended = True
            return True
    def End_timer(self):
        self.ended = True
    def Reset_timer(self):
        self.started = True
        self.frame = 0
        self.ended = False


pumpkin_cooldown = Cooldown(1)
player1 = Player(50)
pumpkin = Pumpkin(500,0,"textureNone",50)
pumpkins = []
init_window(1280,720,"BOB")
set_target_fps(60)
hide_cursor()
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    for pumpk in pumpkins:
        pumpk.Spawn()
        pumpk.award_points()
    player1.draw()
    player1.shoot()
    pumpkin.Spawn()
    pumpkin.award_points()
    draw_text(f"{int(score)}",400,0,40,GREEN)
    if pumpkin_cooldown.Start_timer():
        pumpkins.append(Pumpkin(random.randrange(0,1000,50),0,"textureNone",100))
        pumpkin_cooldown = Cooldown(random.uniform(0,1))
    end_drawing()
close_window()
                    


