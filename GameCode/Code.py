import raylib as rl
from pyray import *
import random
particless =-1
damage = 100
score = 0
ammo = 200
max_ammo = 200
gunsize = 50
pumpkin_damage=1
max_money_gained =10
mult =1
reload_time = 2
pumpkin_spawn_rate = 3
level = 1
combo_cooldown = 5
max_health = 20
combo = False

class Pumpkin:
    def __init__(self,pos_x,pos_y,texture,size):
        global mult
        global max_money_gained
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = random.randrange(1,20)
        self.points = max_money_gained
        self.texture = texture
        self.size = size
        self.alive = True
        self.box = Rectangle(self.pos_x, self.pos_y,self.size,self.size)
        self.lose_points = False
        self.gain_points = False
        self.health = max_health
        self.max_health = self.health
        self.alpha = 255
        self.status = True
    def Spawn(self):
        global damage
        global textattack_list
        global ammo
        global mult
        if self.alive == True:
            draw_rectangle_rec(self.box,Color(100,50,100,self.alpha))
            self.box = Rectangle(self.pos_x, self.pos_y,self.size,self.size) # main problem is the way it scales down is not centered
            self.pos_y +=self.speed
        if self.pos_y >= 1080:
            self.lose_points = True
            self.alive = False
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT) and ammo >0:
            if check_collision_recs(player1.collisionbox,self.box) and self.alive ==True:
                textattack_list.append(Text(f"-{damage}",40,int(player1.position.x)+random.randrange(-20,20),int(player1.position.y),253, 249, 0,None,10,120,1))
                self.health -=damage
                self.alpha -=int(255/self.max_health)
                if self.health <= 0 or self.alpha <=30:
                    textattack_list.append(Text(f"+${self.points*mult}",100,int(player1.position.x)+random.randrange(-20,20),int(player1.position.y),0,255,0,None,10,120,1))
                    self.alive = False
                    self.gain_points = True
    def award_points(self):
        global textattack_list
        global score
        global mult
        global combo
        if self.status == True:
            if self.alive == False:
                if self.gain_points == True:
                    if mult>=2:
                        score +=self.points*(mult-1)
                        combo = True
                        textattack_list.append(Text(f"X{mult} Combo",300,400,300,random.randrange(0,256),random.randrange(0,256),random.randrange(0,256),None,10,120,1))
                    else:
                        score+=self.points
                    mult +=1
                     #use the floating thingy to make the score float up &&& add the particles
                else:
                    score -=10 # use the floating and shake thingy
                    textattack_list.append(Text(f"-$10",250,random.randrange(0,1620),random.randrange(0,680),255, 0, 0,None,10,120,1))
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
    def __init__(self,text,size,posx,posy,r,g,b,font,spacing,time,slowness):
        self.text = text
        self.size = size
        self.posx = posx
        self.posy = posy
        self.r = r        
        self.g = g
        self.b = b
        self.font = font
        self.spacing = spacing
        self.frame = 0
        self.time = time
        self.slowness = slowness
        self.opacity = 255
        self.color = Color(self.r,self.g,self.b,self.opacity)
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
        self.color = Color(self.r,self.g,self.b,self.opacity)
        self.frame +=1
        if self.frame % self.slowness ==0:
            self.opacity -=5
            self.posy -= int(5)
class Shake:
    def __init__(self,intensity_min,intensity_max,length_min,length_max,times,currentvalue,original_length):
        self.intensity_min = intensity_min
        self.intensity_max = intensity_max
        self.length_min = length_min
        self.length_max = length_max
        self.times = times
        self.currentvalue = currentvalue
        self.original_length = original_length
        self.original_value = currentvalue
        self.shake = False
    def Randomize(self):
        self.intensity = random.uniform(self.intensity_min,self.intensity_max)
        self.length = random.uniform(self.length_min,self.length_max)
        self.original_length = 0
        self.shake = True

    def NotRandom(self):
        self.intensity = self.intensity_max
        self.length = self.length_max
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
    def __init__(self,size,gunsize):
        self.gunsize = gunsize
        self.position = get_mouse_position()
        self.size = size
        self.size_box = self.gunsize/5
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
        self.collisionbox = Rectangle(self.position.x,self.position.y,self.size_box,self.size_box)
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            self.rotation+=self.rotationfactor
            if self.size >= 30:
                self.rotationfactor+=0.2
                self.size -= 3
        elif self.size <= self.originalsize:
            self.rotationfactor = self.orioginalrotation
            self.size += 4
    def shootparticles(self):
        global ammo
        global particless
        global particles_shoot_list
        global reloading
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT) and ammo >0:
            ammo -=1
            particles_shoot_list.append(SpawnParticles(2,10,1,2,4,5,1,10,0,[YELLOW,WHITE],player1.position.x,player1.position.y,0.2,0.2,1,1))
            particless+=1
            particles_shoot_list[particless].Randomize()
        for particle in particles_shoot_list:
            particle.Spawn()
        if is_mouse_button_released(rl.MOUSE_BUTTON_LEFT):
            particles_shoot_list = []
            particless = -1
        if ammo == 0 and is_key_pressed(rl.KEY_R):
            reloading = True
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
        self.started = False
        self.frame = 0
        self.ended = False
reloading = False
reload_cooldown = Cooldown(reload_time)
pumpkin_cooldown = Cooldown(pumpkin_spawn_rate)
combo_timer = Cooldown(combo_cooldown)
player1 = Player(50,gunsize)
pumpkin = Pumpkin(500,0,"textureNone",50)
#class lists
pumpkins = []
textattack_list = []
textlose_list = []
shake_kill_list = []
shake_lose_health_list = []
particles_hit_list = []
particles_shoot_list = []
particles_destroy_list = []
#class Structures
kill:Shake = Shake(10,11,20,30,5,0,1)
particle_hit:SpawnParticles = SpawnParticles(5,7,1,2,3,7,1,10,0,[WHITE,ORANGE],player1.position.x,player1.position.y,1,1,1,1)
particle_shoot:SpawnParticles = SpawnParticles(4,5,1,2,3,7,1,10,0,[YELLOW,WHITE],player1.position.x,player1.position.y,1,1,1,1)
particle_destroy:SpawnParticles = SpawnParticles(100,300,10,40,3,7,1,10,0,[ORANGE,WHITE,Color(222, 116, 22,255),Color(255, 178, 0,255)],player1.position.x,player1.position.y,1,1,1,1)
# text_gain:Text = Text()
# text_lost:Text = Text()
level1cam = Camera2D()
level1cam.offset=(Vector2(0,0))
level1cam.zoom=1
level1cam.rotation=0
level1cam.target = Vector2(0,0)
levelup = False
upgrade_screen = False
game_screen = True
init_window(1280,720,"BOB")
toggle_fullscreen()
set_target_fps(60)
hide_cursor()
while not window_should_close():
    game_time = round(get_time(),1)
    if game_time%10 == 0 and levelup == False:
        levelup = True
        level+=1
        pumpkin_spawn_rate/=1.1
    if not game_time%10==0:
        levelup = False

    


    begin_drawing()
    begin_mode_2d(level1cam)
    clear_background(BLACK)
    for pumpk in pumpkins:
        pumpk.Spawn()
        pumpk.award_points()
    
    player1.shootparticles()
    player1.draw()
    player1.shoot()
    pumpkin.Spawn()
    pumpkin.award_points()
    for i in range(0,len(textattack_list)):
        textattack_list[i].FloatText() #this draws items that are within the list
        if textattack_list[i].opacity <=0:
            textattack_list[i]
    draw_text(f"${int(score)} Money",400,0,40,GREEN)
    draw_text(f"{int(ammo)} Ammo",400,40,40,YELLOW)
    if pumpkin_cooldown.Start_timer():
        pumpkins.append(Pumpkin(random.randrange(0,1870,50),0,"textureNone",100))
        pumpkin_cooldown = Cooldown(random.uniform(0,pumpkin_spawn_rate))
    if ammo ==0 and reloading == False:
        draw_text(f"Press R to Reload",0,400,200,WHITE)
    if reloading == True:
        draw_text(f"Reloading........",0,400,200,WHITE)
        reload_cooldown.Start_timer()
        if reload_cooldown.Start_timer():
            particles_shoot_list = []
            particless = -1
            ammo = max_ammo
            reload_cooldown.Reset_timer()
            reloading = False
    if combo == True:
        combo_timer.Start_timer()
        if combo_timer.Start_timer() == True:
            combo_timer.Reset_timer()
            mult = 1
            combo = False
    draw_text(f"Level {level}",400,80,50,WHITE)
    draw_text(f"spawn_rate {pumpkin_spawn_rate}",400,120,50,WHITE)
    draw_text(f"Time {game_time}",400,160,50,WHITE)
    draw_text(f"Zoom {level1cam.zoom}",400,200,50,WHITE)
    end_mode_2d()
    end_drawing()
close_window()
                    

