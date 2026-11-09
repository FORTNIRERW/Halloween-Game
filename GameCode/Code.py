import raylib as rl
from enum import Enum,auto
from pyray import *
from os.path import join
import random
particless =-1
damage = 2
score = 50
tokens = 0
ammo = 150
max_ammo = 150
gunsize = 50
pumpkin_damage=1
max_money_gained =5
enemydamage = 10
mult =1
reload_time = 2
pumpkin_spawn_rate = 1
special_spawn_rate =20
max_tokens_gained = 1
level = 1
combo_cooldown = 1
max_health = 20
max_health_special = 100
pumpkinspeed = 5
maxspeed = 10
combo = False
dead = False
class screen(Enum): # this is so cool
    PLAY = auto()
    LOSE = auto()
    MENU = auto()
    STATS = auto()
    UPGRADE = auto()
currentScreen = screen.MENU
def reset():
    global particless
    global damage
    global score
    global ammo
    global max_ammo
    global gunsize
    global max_money_gained
    global mult
    global reload_time
    global pumpkin_spawn_rate
    global level
    global combo_cooldown
    global max_health
    global pumpkinspeed
    global maxspeed
    global combo
    global dead
    global pumpkins
    global textattack_list
    global particles_hit_list
    global particles_shoot_list
    global particles_destroy_list
    global levelup
    global tokens
    global max_tokens_gained
    global special_spawn_rate
    global max_health_special
    global special
    global current_frame
    global enemydamage
    global currentScreen
    global reloading
    enemydamage = 10
    particless =-1
    damage = 2
    score = 50
    tokens = 0
    special_spawn_rate = 20
    max_health_special =100
    max_tokens_gained = 1
    ammo = 150
    max_ammo = 150
    gunsize = 50 
    max_money_gained =5
    mult =1
    reload_time = 2
    pumpkin_spawn_rate = 1
    level = 1
    combo_cooldown = 1
    max_health = 20
    pumpkinspeed = 5
    maxspeed = 10
    combo = False
    dead = False
    reloading = False
    pumpkins = []
    special = []
    textattack_list = []
    particles_hit_list = []
    particles_shoot_list = []
    particles_destroy_list = []
    levelup = False
    game_time.Reset_timer()
    current_frame = 0
class Pumpkin:
    def __init__(self,pos_x,pos_y,texture,size):
        global mult
        global max_money_gained
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = random.randrange(1,maxspeed)
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
            # draw_rectangle_rec(self.box,Color(0,0,0,self.alpha))
            draw_texture_pro(self.texture[current_frame],Rectangle(0,0,self.texture[current_frame].width,self.texture[current_frame].height),self.box,Vector2(0,0),0,Color(0,0,0,self.alpha))
            self.box = Rectangle(self.pos_x, self.pos_y,self.size,self.size) # main problem is the way it scales down is not centered
            self.pos_y +=self.speed
        if self.pos_y >= 1080:
            self.lose_points = True
            self.alive = False
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT) and ammo >0:
            if check_collision_recs(player1.collisionbox,self.box) and self.alive ==True:
                textattack_list.append(Text(f"-{damage}",40,int(player1.position.x)+random.randrange(-20,20),int(player1.position.y),0, 0, 0,MatchWorld,10,120,1))
                self.health -=damage
                self.alpha -=int(255/self.max_health)
                if self.health <= 0 or self.alpha <=30:
                    textattack_list.append(Text(f"+{self.points*mult}",50,int(player1.position.x)+random.randrange(-20,20),int(player1.position.y),0,255,0,MatchWorld,10,120,1))
                    self.alive = False
                    self.gain_points = True
    def award_points(self):
        global textattack_list
        global score
        global mult
        global combo
        global particless
        if self.status == True:
            if self.alive == False:
                if self.gain_points == True:
                    combo_timer.Reset_timer()
                    if mult>=2:
                        score +=self.points*(mult-1)
                        combo = True
                        textattack_list.append(Text(f"X{mult} Combo",150,0,900,random.randrange(100,256),random.randrange(100,256),random.randrange(100,256),MatchWorld,10,120,3))
                    else:
                        score+=self.points
                    mult +=1
                     #use the floating thingy to make the score float up &&& add the particles
                else:
                    score -=enemydamage # use the floating and shake thingy
                    textattack_list.append(Text(f"-{enemydamage}",50,random.randrange(0,1620),random.randrange(0,680),255, 0, 0,MatchWorld,10,120,1))
                self.status = False
class Special:
    def __init__(self,pos_x,pos_y,texture,size):
        global mult
        global max_tokens_gained
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 3
        self.Tokens = max_tokens_gained
        self.texture = texture
        self.size = size
        self.alive = True
        self.box = Rectangle(self.pos_x, self.pos_y,self.size,self.size)
        self.gain_Tokens = False
        self.health = max_health_special
        self.max_health = self.health
        self.alpha = 255
        self.status = True
    def Spawn(self):
        global damage
        global textattack_list
        global ammo
        global mult
        if self.alive == True:
            draw_texture_pro(Enemy2Animation[current_frame],Rectangle(0,0,Enemy1.width,Enemy1.height),self.box,Vector2(0,0),0,Color(0,0,0,self.alpha))
            self.box = Rectangle(self.pos_x, self.pos_y,self.size,self.size) # main problem is the way it scales down is not centered
            self.pos_y +=self.speed
        if self.pos_y >= 1080:
            self.alive = False
        if is_mouse_button_down(rl.MOUSE_BUTTON_LEFT) and ammo >0:
            if check_collision_recs(player1.collisionbox,self.box) and self.alive ==True:
                textattack_list.append(Text(f"-{damage}",40,int(player1.position.x)+random.randrange(-20,20),int(player1.position.y),0, 0, 0,MatchWorld,10,120,1))
                self.health -=damage
                self.alpha -=int(255/self.max_health)
                if self.health <= 0 or self.alpha <=30:
                    textattack_list.append(Text(f"+{self.Tokens*mult}",500,350,600,0,255,40,MatchWorld,10,250,1))
                    self.alive = False
                    self.gain_Tokens = True
    def award_Tokens(self):
        global textattack_list
        global tokens
        global mult
        global combo
        global score
        if self.status == True:
            if self.alive == False:
                if self.gain_Tokens == True:
                    combo_timer.Reset_timer()
                    if mult>=2:
                        tokens +=self.Tokens*(mult-1)
                        combo = True
                        textattack_list.append(Text(f"X{mult} Combo",150,0,900,random.randrange(100,256),random.randrange(100,256),random.randrange(100,256),MatchWorld,10,120,3))
                    else:
                        tokens+=self.Tokens
                    mult +=1
                else:
                    score -=enemydamage # use the floating and shake thingy
                    textattack_list.append(Text(f"-{enemydamage}",50,random.randrange(0,1620),random.randrange(0,680),255, 0, 0,MatchWorld,10,120,1))
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
        if self.frame <= self.time:
            draw_text_ex(self.font,str(self.text),Vector2(self.posx,self.posy),self.size,self.spacing,self.color)
        
        else:
            return
        if self.opacity <=1:
            self.opacity = 0
        self.color = Color(self.r,self.g,self.b,self.opacity)
        self.frame +=1
        if self.frame % self.slowness ==0:
            self.opacity -=5
            self.posy -= int(5)
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
    def __init__(self,size,gunsize,texture):
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
        self.texture = texture
    def draw(self):
        self.position = get_mouse_position()
        self.collisionbox = Rectangle(self.position.x-self.size_box/2,self.position.y-self.size_box/2,self.size_box,self.size_box)
        draw_texture_pro(crosshairAnimation[current_frame],Rectangle(0,0,crosshairAnimation[1].width,crosshairAnimation[1].height),Rectangle((self.position.x-self.size_box/2)+5,(self.position.y-self.size_box/2)+5,self.size,self.size),Vector2(self.size/2,self.size/2),self.rotation,BLACK)
        # draw_rectangle_rec(self.collisionbox,BLUE) #this is the hitbox
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
            particles_shoot_list.append(SpawnParticles(2,10,1,2,4,5,1,10,0,[BLACK,BLACK,BLACK,WHITE],player1.position.x,player1.position.y,0.2,0.2,1,1))
            particless+=1
            particles_shoot_list[particless].Randomize()
        for particle in particles_shoot_list:
            particle.Spawn()
        if is_mouse_button_released(rl.MOUSE_BUTTON_LEFT):
            particles_shoot_list = []
            particless = -1
        if is_key_pressed(rl.KEY_R):
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
class Button:
    def __init__(self,texture,posx,posy,size,tint,text):
        self.texture = texture
        self.posx = posx
        self.posy = posy
        self.originalx = posx
        self.originaly = posy
        self.size = size
        self.max_size = self.size*2
        self.max_posy = self.posx-int((buttonoutline.height/2)*self.size)
        self.max_posx = self.posy - int((buttonoutline.width/2)*self.size)
        self.tint = tint
        self.text = text
        self.collision = Rectangle(self.posx,self.posy,buttonoutline.width*self.size,buttonoutline.height*self.size)
    def Draw(self):
        draw_texture_ex(self.texture,Vector2(self.posx,self.posy),0,self.size,self.tint)
        # draw_rectangle_rec(self.collision,RED)
    def Draw_text(self):
        draw_text(self.text,self.posx+25,self.posy+20,int(self.size*300),self.tint)
    def Hover(self):
        if check_collision_recs(self.collision,mouse_box):
            self.tint = GRAY
            self.size = self.max_size
            self.posx = self.originalx-int(self.size*buttonoutline.width/4)
            self.posy = self.originaly-int(self.size*buttonoutline.height/4)
            self.collision = Rectangle(self.posx,self.posy,buttonoutline.width*self.size,buttonoutline.height*self.size)
        else:
            self.size = self.max_size/2
            self.tint = BLACK
            self.posy = self.originaly
            self.posx = self.originalx
            self.collision = Rectangle(self.posx,self.posy,buttonoutline.width*self.size,buttonoutline.height*self.size)
    def Check_click(self):
        if check_collision_recs(self.collision,mouse_box) and is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
            return True

init_window(1800,1000,"BOB")
combo_textures = []
MomFont = load_font((join("Halloween-Game","Assets","Fonts","Momfont.ttf")))
MatchWorld = load_font((join("Halloween-Game","Assets","Fonts","Matcha World.ttf")))
Crosshair1 = load_texture((join("Halloween-Game","Assets","Images","Crosshair","Crosshair1.png")))
Crosshair2 = load_texture((join("Halloween-Game","Assets","Images","Crosshair","Crosshair2.png")))
Enemy1 = load_texture((join("Halloween-Game","Assets","Images","Enemy1","Enemy1.png")))
Enemy2 = load_texture((join("Halloween-Game","Assets","Images","Enemy1","Enemy2.png")))
AnotherEnemy1 = load_texture((join("Halloween-Game","Assets","Images","enemy2","AnotherEnemy1.png")))
AnotherEnemy2 = load_texture((join("Halloween-Game","Assets","Images","enemy2","AnotherEnemy2.png")))
buttonoutline = load_texture((join("Halloween-Game","Assets","Images","BackgroundElements","Buttons1.png")))
backgroundMain = load_texture((join("Halloween-Game","Assets","Images","BackgroundElements","Background1.png")))
for i in range(1,6):
    combo_textures.append(load_texture((join("Halloween-Game","Assets","Images","BackgroundElements",f"ComboOutlineBetter{i}.png"))))
animation_cooldown = Cooldown(40)
combo_color_speed = 0.6
combo_color_cooldown = Cooldown(combo_color_speed)
combor = random.randrange(100,256)
combob = random.randrange(100,256)
combog = random.randrange(100,256)
comboa = 0
crosshairAnimation = [Crosshair1,Crosshair2]
Enemy1Animation = [Enemy1,Enemy2]
Enemy2Animation = [AnotherEnemy1,AnotherEnemy2]
reloading = False
reload_cooldown = Cooldown(reload_time)
pumpkin_cooldown = Cooldown(pumpkin_spawn_rate)
combo_timer = Cooldown(combo_cooldown)
player1 = Player(50,gunsize,Crosshair1)
pumpkin = Pumpkin(500,0,Enemy1,50)
specialboi = Special(500,0,"texture",80)
special_cooldown = Cooldown(special_spawn_rate)
#class lists
pumpkins = []
special = []
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
particle_shoot:SpawnParticles = SpawnParticles(4,5,1,2,3,7,1,10,0,[BLACK,BLACK,BLACK,WHITE],player1.position.x,player1.position.y,1,1,1,1)
particle_destroy:SpawnParticles = SpawnParticles(100,300,10,40,3,7,1,10,0,[ORANGE,WHITE,Color(222, 116, 22,255),Color(255, 178, 0,255)],player1.position.x,player1.position.y,1,1,1,1)
button_play = Button(buttonoutline,600,100,0.25,BLACK,"play")
button_leave = Button(buttonoutline,600,400,0.25,BLACK,"leave")
button_Menu = Button(buttonoutline,600,400,0.25,BLACK,"Back")
button_stats = Button(buttonoutline,600,700,0.25,BLACK,"Stats")
level1cam = Camera2D()
level1cam.offset=(Vector2(0,0))
level1cam.zoom=1
level1cam.rotation=0
level1cam.target = Vector2(0,0)
levelup = False
game_time = Cooldown(30)
current_frame = 0
set_target_fps(60)
show_cursor()
while not window_should_close():
    mousep = get_mouse_position()
    mouse_box = Rectangle(mousep.x-2,mousep.y-2,5,5)
    

    begin_drawing()
    begin_mode_2d(level1cam)
    clear_background(RAYWHITE)
    draw_texture_ex(backgroundMain,Vector2(0,0),0,1,WHITE)
    if currentScreen == screen.PLAY and dead == False:
        hide_cursor()
        animation_cooldown.Start_timer()
        if animation_cooldown.frame >20:
            current_frame = 1
            if animation_cooldown.frame >= 40:
                animation_cooldown.Reset_timer()
        else:
            current_frame = 0

        if game_time.Start_timer() and levelup == False:
# game_time = round(get_time(),1)
            levelup = True
            level+=1
            pumpkin_spawn_rate/=1.1
            negative_effect = random.randrange(0,2)
            if negative_effect == 1:
                max_health += int(max_health/2)
                max_health_special +=int(max_health_special/2)
                print("more health")
            elif negative_effect == 0:
                enemydamage +=int(enemydamage/2)
                print(enemydamage)
                print("more damage")
            currentScreen = screen.UPGRADE
            game_time.Reset_timer()

                
            
        if not game_time.Start_timer():
            levelup = False


        for pumpk in pumpkins:
            pumpk.Spawn()
            pumpk.award_points()
        for specials in special:
            specials.Spawn()
            specials.award_Tokens()

        player1.shootparticles()
        player1.draw()
        player1.shoot()
        for i in range(0,len(textattack_list)):
            textattack_list[i].FloatTextex() #this draws items that are within the list
            if textattack_list[i].opacity <=0:
                textattack_list[i]
        if pumpkin_cooldown.Start_timer():
            pumpkins.append(Pumpkin(random.randrange(300,1800,50),0,Enemy1Animation,100))# CHANGED THIS
            pumpkin_cooldown = Cooldown(random.uniform(0,pumpkin_spawn_rate))
        if special_cooldown.Start_timer():
            special.append(Special(random.randrange(300,1800,50),0,Enemy2Animation,150)) # CHANGED THIS
            special_cooldown = Cooldown(random.uniform(0,special_spawn_rate))
        if ammo ==0 and reloading == False:
            draw_text_ex(MatchWorld,f"R to Reload",Vector2(200,400),200,10,BLACK)
        if reloading == True:
            draw_text_ex(MatchWorld,f"Reloading........",Vector2(150,400),200,10,BLACK)
            reload_cooldown.Start_timer()
            ammo = 0
            if reload_cooldown.Start_timer():
                particles_shoot_list = []
                particless = -1
                ammo = max_ammo
                reload_cooldown.Reset_timer()
                reloading = False
        draw_texture_ex(combo_textures[current_frame],Vector2(-10,-10),0,1.02,Color(combor,combog,combob,comboa))
        if not combo:
            if comboa >1:
                comboa -=15
                combo_color_speed = 0.6
        if combo == True:
            if comboa <255:
                comboa +=15
                combo_color_cooldown = Cooldown(combo_color_speed)
            if combo_color_cooldown.Start_timer():
                combo_color_speed/=1.4
                combor = random.randrange(100,256)
                combob = random.randrange(100,256)
                combog = random.randrange(100,256)
                combo_color_cooldown.Reset_timer()
            combo_timer.Start_timer()
            if combo_timer.Start_timer() == True:
                combo_timer.Reset_timer()
                mult = 1
                combo = False
        if score <= 0:
            dead = True
            currentScreen = screen.LOSE
        draw_text_ex(MatchWorld,f"Level {level}",Vector2(400,80),50,10,BLACK)
        draw_text_ex(MatchWorld,f"spawn_rate {int(pumpkin_spawn_rate)}",Vector2(400,120),50,10,BLACK)
        draw_text_ex(MatchWorld,f"Time {int(game_time.frame/60)}/{int(game_time.frames_to_go/60)}",Vector2(400,160),50,10,BLACK)
        # draw_text_ex(MatchWorld,f"ComboTimer {combo_timer.frame}/{combo_timer.frames_to_go}",Vector2(400,200),50,10,BLACK)
        # draw_text_ex(MatchWorld,f"current_frame = {current_frame} timer = {animation_cooldown.frame}",Vector2(400,240),50,10,BLACK)
        draw_text_ex(MatchWorld,f"${int(score)} Money",Vector2(400,0),50,10,BLACK)
        draw_text_ex(MatchWorld,f"{int(ammo)} Ammo",Vector2(400,40),50,10,BLACK)
        # draw_text_ex(MatchWorld,f"{combo_color_speed} ComboCooldown",Vector2(400,280),50,10,BLACK)
    if currentScreen != screen.PLAY:
        show_cursor()
    if currentScreen == screen.LOSE:
        button_Menu.Draw()
        button_Menu.Draw_text()
        button_Menu.Hover()
        if button_Menu.Check_click():
            currentScreen = screen.MENU
            reset()
    if currentScreen == screen.UPGRADE:
        draw_text("upgrade 1",100,100,300,BLACK)
        draw_text("upgrade 2",100,300,300,BLACK)
        draw_text("upgrade 3",100,500,300,BLACK)
        if is_key_pressed(rl.KEY_V):
            currentScreen = screen.PLAY
            game_time.Reset_timer()
            textattack_list = []
    if currentScreen == screen.MENU:
        show_cursor()
        button_play.Draw()
        button_play.Draw_text()
        button_play.Hover()
        if button_play.Check_click():
            print("sigma")
            currentScreen = screen.PLAY
        button_stats.Draw()
        button_stats.Draw_text()
        button_stats.Hover()
        if button_stats.Check_click():
            currentScreen = screen.STATS
        button_leave.Draw()
        button_leave.Draw_text()
        button_leave.Hover()
    end_mode_2d()
    end_drawing()
close_window()
                    

