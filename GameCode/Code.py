import raylib as rl
from pyray import *
from os.path import join
import random
particless =-1
damage = 2
score = 100
tokens = 0
ammo = 200
max_ammo = 200
gunsize = 50
pumpkin_damage=1
max_money_gained =10
enemydamage = 10
mult =1
reload_time = 2
pumpkin_spawn_rate = 1
special_spawn_rate =20
max_tokens_gained = 1
level = 1
combo_cooldown = 10
max_health = 20
max_health_special = 100
pumpkinspeed = 5
maxspeed = 10
combo = False
dead = False
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
    global upgrade_screen
    global game_screen
    global tokens
    global max_tokens_gained
    global special_spawn_rate
    global max_health_special
    global special
    global current_frame
    global enemydamage
    enemydamage = 10
    particless =-1
    damage = 2
    score = 100
    tokens = 0
    special_spawn_rate = 20
    max_health_special =100
    max_tokens_gained = 1
    ammo = 200
    max_ammo = 200
    gunsize = 50 
    max_money_gained =10
    mult =1
    reload_time = 2
    pumpkin_spawn_rate = 1
    level = 1
    combo_cooldown = 2
    max_health = 20
    pumpkinspeed = 5
    maxspeed = 10
    combo = False
    dead = False
    pumpkins = []
    special = []
    textattack_list = []
    particles_hit_list = []
    particles_shoot_list = []
    particles_destroy_list = []
    levelup = False
    upgrade_screen = False
    game_screen = True
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


init_window(1280,720,"BOB")
MomFont = load_font((join("Halloween-Game","Assets","Fonts","Momfont.ttf")))
MatchWorld = load_font((join("Halloween-Game","Assets","Fonts","Matcha World.ttf")))
Crosshair1 = load_texture((join("Halloween-Game","Assets","Images","Crosshair","Crosshair1.png")))
Crosshair2 = load_texture((join("Halloween-Game","Assets","Images","Crosshair","Crosshair2.png")))
Enemy1 = load_texture((join("Halloween-Game","Assets","Images","Enemy1","Enemy1.png")))
Enemy2 = load_texture((join("Halloween-Game","Assets","Images","Enemy1","Enemy2.png")))
AnotherEnemy1 = load_texture((join("Halloween-Game","Assets","Images","enemy2","AnotherEnemy1.png")))
AnotherEnemy2 = load_texture((join("Halloween-Game","Assets","Images","enemy2","AnotherEnemy2.png")))

animation_cooldown = Cooldown(40)
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
level1cam = Camera2D()
level1cam.offset=(Vector2(0,0))
level1cam.zoom=1
level1cam.rotation=0
level1cam.target = Vector2(0,0)
levelup = False
upgrade_screen = False
game_screen = True
game_time = Cooldown(30)
current_frame = 0
toggle_fullscreen()
set_target_fps(60)
hide_cursor()
while not window_should_close():


    

    begin_drawing()
    begin_mode_2d(level1cam)
    clear_background(RAYWHITE)
    if game_screen == True and dead == False:
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
            negative_effect = random.randrange(0,1)
            game_screen = False
            if negative_effect == 1:
                max_health += int(max_health/2)
                max_health_special +=int(max_health_special/2)
                print("more health")
            elif negative_effect == 0:
                enemydamage +=int(enemydamage/2)
                print(enemydamage)
                print("more damage")
            upgrade_screen = True
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
        draw_text(f"${int(score)} Money",400,0,40,BLACK)
        draw_text(f"{int(ammo)} Ammo",400,40,40,BLACK)
        if pumpkin_cooldown.Start_timer():
            pumpkins.append(Pumpkin(random.randrange(0,1870,50),0,Enemy2Animation,100))# CHANGED THIS
            pumpkin_cooldown = Cooldown(random.uniform(0,pumpkin_spawn_rate))
        if special_cooldown.Start_timer():
            special.append(Special(random.randrange(0,1870,50),0,Enemy2Animation,150)) # CHANGED THIS
            special_cooldown = Cooldown(random.uniform(0,special_spawn_rate))
        if ammo ==0 and reloading == False:
            draw_text(f"Press R to Reload",0,400,200,BLACK)
        if reloading == True:
            draw_text(f"Reloading........",0,400,200,BLACK)
            reload_cooldown.Start_timer()
            ammo = 0
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
        if score <= 0:
            dead = True
        draw_text_ex(MatchWorld,f"Level {level}",Vector2(400,80),50,10,BLACK)
        draw_text_ex(MatchWorld,f"spawn_rate {pumpkin_spawn_rate}",Vector2(400,120),50,10,BLACK)
        draw_text(f"Time {game_time.frame}/{game_time.frames_to_go}",400,160,50,BLACK)
        draw_text(f"Zoom {level1cam.zoom}",400,200,50,BLACK)
        draw_text(f"ComboTimer {combo_timer.frame}/{combo_timer.frames_to_go}",400,240,50,BLACK)
        draw_text(f"current_frame = {current_frame} timer = {animation_cooldown.frame}",400,280,50,BLACK)
    if dead == True and game_screen == True:
        draw_text("R to Restart",20,300,250,BLACK)
        if is_key_pressed(rl.KEY_R):
            reset()
    if upgrade_screen == True:
        draw_text("upgrade 1",100,100,300,BLACK)
        draw_text("upgrade 2",100,300,300,BLACK)
        draw_text("upgrade 3",100,500,300,BLACK)
        if is_key_pressed(rl.KEY_V):
            upgrade_screen = False
            game_screen = True
            game_time.Reset_timer()
            pumpkins = []
            special = []
            textattack_list = []
            mult = 1
    end_mode_2d()
    end_drawing()
close_window()
                    

