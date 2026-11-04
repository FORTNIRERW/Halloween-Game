import raylib as rl
from pyray import*

player = get_mouse_position()
size = 2
class Button:
    def __init__(self,posx,posy,width,height,r,g,b,opacity,text):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.maxheight = height +100
        self.maxwidth = width +100
        self.positionmax = posx -self.width/8
        self.positionmay = posy -self.height/2
        self.r = r
        self.g = g
        self.b = b
        self.opacity = opacity
        self.hover = False
        self.collider = Rectangle(self.posx,self.posy,self.width,self.height)
        self.text = text
    def Draw(self):
        if self.hover == True:
            self.collider.height = self.maxheight
            self.collider.width = self.maxwidth
            self.collider.x = self.positionmax
            self.collider.y = self.positionmay
            draw_rectangle_rec(self.collider,Color(self.r,self.g,200,self.opacity))
        else:
            self.collider = Rectangle(self.posx,self.posy,self.width,self.height)
            draw_rectangle_rec(self.collider,Color(self.r,self.g,self.b,self.opacity))
        draw_text(f"{self.text}",self.posx,self.posy,self.height,WHITE)
    def check_hover(self,playerx,playery,size):
        self.playerx = playerx
        self.playery = playery
        self.size = size
        self.player_collision_box = Rectangle(self.playerx,self.playery,self.size,self.size)
        if check_collision_recs(self.collider,self.player_collision_box):
            self.hover = True
        else:
            self.hover = False
    def check_click(self):
        if check_collision_recs(self.collider,self.player_collision_box) and is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
            return True # replace with what you want to be here

skibidi_button = Button(400,300,300,100,240,210,50,255,"skibidi")
play_button = Button(400,100,300,100,240,210,50,255,"play")
leave_button = Button(400,500,300,100,240,210,50,255,"leave")
init_window(1280,720,"BUTTON TEST")
while not window_should_close():
    player = get_mouse_position()
    begin_drawing()
    clear_background(BLACK)
    play_button.Draw()
    play_button.check_hover(player.x,player.y,2)
    if play_button.check_click():
        print("Play")
    skibidi_button.Draw()
    skibidi_button.check_hover(player.x,player.y,2)
    if skibidi_button.check_click():
        print("Skibidi")
    leave_button.Draw()
    leave_button.check_hover(player.x,player.y,2)
    if leave_button.check_click():
        print("leave")

    end_drawing()
close_window()
