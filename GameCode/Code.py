import raylib as rl
from pyray import *
import random
particless =-1
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
        if self.pos_y >= 720:
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
class SpawnParticles:
    def __init__(self,min_particles,max_particles,min_speed,max_speed,min_size,max_size,min_resistance,max_resistance,gravity,colors:list,posx,posy,shrink_rate,shrink_factor,cutoff,remove):
        self.max_particles = max_particles
        self.min_particles = min_particles
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.min_size = min_size
        self.max_size = max_size
        self.gravity = gravity
        self.max_resistance = max_resistance
        self.min_resistance = min_resistance
        self.colors = colors
        self.posx = posx
        self.posy = posy
        self.shrink_rate = shrink_rate
        self.shrink_factor = shrink_factor
        self.cutoff = cutoff
        self.remove = remove
        self.position = Vector2(self.posx,self.posy)
        self.particle_num = random.randrange(self.min_particles,self.max_particles)
        self.list_resistance = []
        self.list_speed = []
        self.list_size = []
        self.list_direction_x = []
        self.list_direction_y = []
        self.list_position = []
        self.list_position_x = []
        self.list_position_y = []
        #defined vars
        



    def Randomize(self):
        self.particle_num = random.randrange(self.min_particles,self.max_particles)
        self.list_size = []
        self.list_speed = []
        self.list_resistance = []
        self.list_position = []
        self.list_position_x = []
        self.list_position_y = []
        self.list_colors = []
        for i in range(self.particle_num):
            self.list_size.append(random.randrange(self.min_size,self.max_size))
            self.list_speed.append(random.randrange(self.min_speed,self.max_speed))
            self.list_resistance.append(random.randrange(self.min_resistance,self.max_resistance))
            self.list_direction_x.append(random.randrange(-10,20,1))#firgure out how to make this a float
            self.list_direction_y.append(random.randrange(-10,20,1))# figure out how to make this a float
            self.list_position_x.append(self.position.x)
            self.list_position_y.append(self.position.y)
            self.list_colors.append(random.choice(self.colors))
    def Spawn(self):
        for i in range(self.particle_num):
            draw_rectangle_v(Vector2(self.list_position_x[i-1],self.list_position_y[i-1]),Vector2(self.list_size[i-1],self.list_size[i-1]),self.list_colors[i-1])
            self.list_position_x[i-1] += self.list_direction_x[i-1] * self.list_speed[i-1]- self.list_resistance[i-1]
            self.list_position_y[i-1] += self.list_direction_y[i-1] * self.list_speed[i-1]- self.list_resistance[i-1]
            self.list_size[i-1] -= self.shrink_rate#*(self.list_size[i-1]/self.shrink_factor)
            if self.list_size[i-1] <= self.cutoff:
                self.list_size[i-1] = 0
            if self.list_size[i-1] <= self.remove:
                break
class Text:
    def __init__(self,text,size,posx,posy,color,font,spacing,time,slowness):
        self.text = text
        self.size = size
        self.posx = posx
        self.posy = posy
        self.color = color
        self.font = font
        self.spacing = spacing
        self.frame = 0
        self.time = time
        self.slowness = slowness
        self.opacity = 255
        self.color = Color(0,255,0,self.opacity)
    def reset(self,posx,posy):
        self.frame = 0
        self.posy = posy
        self.posx = posx
    def FloatTextex(self):
        draw_text_ex(self.font,str(self.text),Vector2(self.posx,self.posy),self.size,self.spacing,self.color)
    def FloatText(self):
        if self.frame <= self.time:
            draw_text(str(self.text),self.posx,self.posy,self.size,self.color)
        
        else:
            return
        if self.opacity <=1:
            self.opacity = 0
        self.color = Color(0,255,0,self.opacity)
        self.frame +=1
        if self.frame % self.slowness ==0:
            self.opacity -=5
            self.posy -= int(5)
class Shake:
    def __init__(self,intensity_min,intensity_max,length_min,length_max,times,currentvalue):
        self.intensity_min = intensity_min
        self.intensity_max = intensity_max
        self.length_min = length_min
        self.length_max = length_max
        self.times = times
        self.currentvalue = currentvalue
        self.original_length = 0
        self.original_value = currentvalue
    def Randomize(self):
        self.intensity = random.uniform(self.intensity_min,self.intensity_max)
        self.length = random.uniform(self.length_min,self.length_max)
        self.original_length = 0
        self.shake = True

    def NotRandom(self):
        self.intensity = self.intensity_max
        self.length = self.length_max
        self.original_length = 0
        self.shake = True

    def shake_ya_booty(self):
        if self.shake == True:
            self.currentvalue += self.intensity
            self.original_length += self.intensity
            if abs(self.original_length) >= abs(self.length):
                self.intensity = -self.intensity
                self.times -=1
                if self.times <= 0:
                    self.currentvalue = self.original_value
                    self.shake = False
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
    def shootparticles(self):
        global particless
        global particles_shoot_list
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            particles_shoot_list.append(SpawnParticles(2,10,1,2,4,5,1,10,0,[YELLOW,WHITE],player1.position.x,player1.position.y,0.2,0.2,1,1))
            particless+=1
            particles_shoot_list[particless].Randomize()
            print(particless)
        for particle in particles_shoot_list:
            particle.Spawn()
        if is_mouse_button_released(rl.MOUSE_BUTTON_LEFT):
            particles_shoot_list = []
            particless = -1
            








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

#class lists
pumpkins = []
textgain_list = []
textlose_list = []
shake_kill_list = []
shake_lose_health_list = []
particles_hit_list = []
particles_shoot_list = []
particles_destroy_list = []
#class Structures
lose_health:Shake = Shake(10,11,20,30,5,0)
kill:Shake = Shake(10,11,20,30,5,0)
particle_hit:SpawnParticles = SpawnParticles(5,7,1,2,3,7,1,10,0,[WHITE,ORANGE],player1.position.x,player1.position.y,1,1,1,1)
particle_shoot:SpawnParticles = SpawnParticles(4,5,1,2,3,7,1,10,0,[YELLOW,WHITE],player1.position.x,player1.position.y,1,1,1,1)
particle_destroy:SpawnParticles = SpawnParticles(100,300,10,40,3,7,1,10,0,[ORANGE,WHITE,Color(222, 116, 22,255),Color(255, 178, 0,255)],player1.position.x,player1.position.y,1,1,1,1)
# text_gain:Text = Text()
# text_lost:Text = Text()

init_window(1280,720,"BOB")
set_target_fps(60)
hide_cursor()
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    for pumpk in pumpkins:
        pumpk.Spawn()
        pumpk.award_points()
    player1.shootparticles()
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
                    


