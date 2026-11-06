import raylib as rl
from pyray import *
from os.path import join
from enum import Enum, auto

class screen(Enum): # this is so cool
    PLAY = auto()
    LOSE = auto()
    MENU = auto()
    STAT = auto()
    UPGRADE = auto()
currentScreen = screen.MENU



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
        if check_collision_recs(self.collision,mouse_rectangle):
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
        if check_collision_recs(self.collision,mouse_rectangle) and is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
            return True




init_window(1280,720,"HopeFully these stupid buttons work")

buttonoutline = load_texture((join("Halloween-Game","Assets","Images","BackgroundElements","Buttons1.png")))
button_play = Button(buttonoutline,400,400,0.17,BLACK,"play")
button_leave = Button(buttonoutline,400,100,0.17,BLACK,"leave")
button_Menu = Button(buttonoutline,400,100,0.17,BLACK,"Back")
while not window_should_close():
    p = get_mouse_position()
    mouse_rectangle = Rectangle(p.x,p.y,20,20)
    begin_drawing()
    clear_background(WHITE)
    if currentScreen == screen.MENU:
        draw_rectangle_rec(mouse_rectangle,BLUE)
        button_play.Draw()
        button_play.Draw_text()
        button_play.Hover()

        if button_play.Check_click():
            currentScreen = screen.PLAY
        button_leave.Draw()
        button_leave.Draw_text()
        button_leave.Hover()
        if button_leave.Check_click():
            currentScreen = screen.LOSE
    elif currentScreen ==screen.LOSE:
        draw_text("You Lose",400,400,100,BLACK)
        button_Menu.Draw()
        button_Menu.Draw_text()
        button_Menu.Hover()
        if button_Menu.Check_click():
            currentScreen = screen.MENU
    elif currentScreen == screen.PLAY:
        draw_text("Your Playing",400,400,100,BLACK)
        button_Menu.Draw()
        button_Menu.Draw_text()
        button_Menu.Hover()
        if button_Menu.Check_click():
            currentScreen = screen.MENU
    print(currentScreen)
    end_drawing()
close_window()