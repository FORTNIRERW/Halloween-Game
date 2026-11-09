import raylib as rl
from pyray import *
import random
from os.path import join

class Card:
    def __init__(self,texture,posx,posy,size,max_size,pixal_width,pixal_height):
        self.texture = texture
        self.posx = posx
        self.posy = posy
        self.size = size
        self.max_size = max_size
        self.pixal_width = pixal_width
        self.sentence = "not gun"
        self.pixal_height = pixal_height

        self.xbefore = int((self.size*(self.size*self.pixal_width))/2) # 300
        self.ybefore = int((self.size*(self.size*self.pixal_height))/2)# 450
        self.xpost = int((self.max_size*(self.size*self.pixal_width))/2) # 300
        self.ypost = int((self.max_size*(self.size*self.pixal_height))/2)# 450
        self.collision_box = Rectangle(self.posx-self.xbefore,self.posy-self.ybefore,int(200*self.size),int(300*self.size))
    def draw(self):
        self.xbefore = int((self.size*(self.size*self.pixal_width))/2) # 300
        self.ybefore = int((self.size*(self.size*self.pixal_height))/2)# 450
        draw_texture_ex(self.texture,Vector2(self.posx-self.xbefore,self.posy-self.ybefore),0,self.size,WHITE)
    def hover(self):
        self.xpost = int((self.max_size*(self.size*self.pixal_width))/2) # 300
        self.ypost = int((self.max_size*(self.size*self.pixal_height))/2)# 450

        if check_collision_recs(mouse_box,self.collision_box):
            draw_texture_ex(self.texture,Vector2(int((self.posx-self.xpost)),int((self.posy-self.ypost))),0,self.max_size,WHITE)
    def check_click(self):
        if check_collision_recs(mouse_box,self.collision_box) and is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
            print(self.sentence)
            return True
    def applyeffect(self):
        if self.texture == card_gunsize_texture:
            self.sentence = "your gun is now 2x as large"
        if self.texture == card_ammo_texture:
            self.sentence = "your ammo is now 500"
        if self.texture == card_damage_texture:
            self.sentence = "you deal +5 damage"
    def randomize(self):
        self.texture = random.choice(cards)
rerollcost = 5
rerollmult = 5
init_window(1280,720,"Cards")
card_damage_texture = load_texture((join("Halloween-Game","Assets","Images","damagedelete.png")))
card_ammo_texture = load_texture((join("Halloween-Game","Assets","Images","CrateUpgrade1.png")))
card_gunsize_texture = load_texture((join("Halloween-Game","Assets","Images","GunsizeDelete.png")))
cards = [card_ammo_texture,card_damage_texture,card_gunsize_texture]
card_gunsize = Card(card_gunsize_texture,100,250,1,1.5,200,300)
card_ammo= Card(card_damage_texture,300,250,1,1.5,200,300)
card_damage= Card(card_ammo_texture,500,250,1,1.5,200,300)
cards_list = []
card_gunsize.randomize()
while not window_should_close():
    mousep = get_mouse_position()
    mouse_box = Rectangle(mousep.x,mousep.y,2,2)
    begin_drawing()
    clear_background(WHITE)
    if is_key_pressed(rl.KEY_R):
        cards_list = []
        cards_list.append(Card(card_ammo_texture,500,250,1,1.2,200,300))
        cards_list.append(Card(card_damage_texture,300,250,1,1.2,200,300))
        cards_list.append(Card(card_gunsize_texture,100,250,1,1.2,200,300))
        print(rerollcost)
        rerollcost +=int(rerollmult/2)+rerollcost
        for card in cards_list:
            card.randomize()
    if len(cards_list)>0:
        for card in cards_list:
            card.draw()
            card.applyeffect()
            if card.check_click():
                cards_list.remove(card)
            card.hover()
    if len(cards_list)>0:
        for card in cards_list:
            card.hover()
    end_drawing()
close_window()


#cards need to be random
# the cards need to have different chances of spawning
#the cards need to affect player stats
# they need to cost a certain amount of tokens
# they should not be too OP
# they should give positive and negative effects mostly positive
#there should be super rare cards



# we need a draw cards randomizes from a cards list based on chance and draws them in order