import pygame
import sys
import shipvar
from tkinter import *

class Option():

    #Variable to store wether text is hovered over or not
    mouseHover = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        
        
        self.set_rect() #call set_rect function
        self.draw()  #call draw function
            
    def draw(self):
        self.set_rend() #call set_rend function
        screen.blit(self.rend, self.rect) #blits text into correct position
        
    def set_rend(self):
        #Renders text with correct colour
        self.rend = menu_font.render(self.text, True, self.colour_choice())
        
    def colour_choice(self):
        if self.mouseHover:
            return (100, 100, 100) #text colour is grey when hovered over
        else:
            return (255, 255, 255) #text colour is white when NOT hovered over
        
    def set_rect(self):
        self.set_rend() #call set_rend function
        self.rect = self.rend.get_rect() #equal to rectangular co-ordinates of text
        self.rect.topleft = self.pos #top left co-ordinate is equal to position of text

#initializes pygame
pygame.init()

#sets screen size to 1200x800
screen = pygame.display.set_mode((1200, 800))

#sets font style and size
menu_font = pygame.font.Font(None, 40)
title_font = pygame.font.Font(None, 80)
ship_font = pygame.font.Font(None, 30)
instruction_font = pygame.font.Font(None,18)

#creates title
title = title_font.render("VRBH GAME", True, (255, 255, 255))


#Spaceship names
ship1Title = Option("PlaneShip", (300, 310))
ship2Title = Option("RockShip", (450, 310))
ship3Title = Option("NukeShip", (600, 310))
ship4Title = Option("OofoShip", (750,310))

#Loads background image
bg = pygame.image.load("background.jpg").convert()

#Ship Images
ship1 = pygame.image.load("ship1.png").convert()
ship2 = pygame.image.load("ship2.png").convert()
ship3 = pygame.image.load("ship3.png").convert()
ship4 = pygame.image.load("ship4.png").convert()

#More Buttons
importShip = Option('IMPORT SHIP', (520,450))
quitButton = Option("QUIT",(580,500))
       

def TKBox():


    root = Tk()

    def getit():
        
        name = entry1.get()
        
        shipvar.shipName = str(name)
        import MainFinal

        root.destroy()
        
    Line1 = Label(root, text ="1) Create/Download an image of a ship (PNG) \n (Make sure theres no background & its not bigger than 150x120)")
    Line2 = Label(root, text = "2) Place the file into the game folder where rest of the ships are")
    Line3 = Label(root, text = "3) Open the program and press on 'New Game' in the main menu")
    Line4 = Label(root,text = "4) Press on Import Ship, a new small window will open \n (Possibly underneath the game window")
    Line5 = Label(root,text = "5) Insert the full file name including the type of file \n and press import - The game will start")

    Line1.grid(row = 0)
    Line2.grid(row = 1)
    Line3.grid(row = 2)
    Line4.grid(row = 3)
    Line5.grid(row = 4)
    
    label1 = Label(root, text = "File Name: ")
    label1.grid(row = 5)
    
    entry1 = Entry(root)
    entry1.grid(row = 5, column = 1)
    
    button1 = Button(root, text = "Import", command = getit )
    button1.grid(row = 5, column = 2)


    
    root.mainloop()

def load_ship():
    loop  = True
    while loop == True:
        pygame.event.pump()
        screen.blit(bg, (0,0)) #blits background
        
        screen.blit(title, (425,15)) #blits title

        #Blits ship images
        screen.blit(ship1, (300, 150))
        screen.blit(ship2, (450, 150))
        screen.blit(ship3, (600, 150))
        screen.blit(ship4, (750, 150))

      

        for buttons in ship1Title, ship2Title, ship3Title, ship4Title, quitButton, importShip:
            if buttons.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.mouseHover = True
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if ship1Title.rect.collidepoint(pygame.mouse.get_pos()) == True:
                            shipvar.shipName = 'ship1.png'
                            import MainFinal
                            loop = False
                        
                        elif ship2Title.rect.collidepoint(pygame.mouse.get_pos()) == True:
                            shipvar.shipName = 'ship2.png'
                            import MainFinal
                            loop = False
                            
                        elif ship3Title.rect.collidepoint(pygame.mouse.get_pos()) == True:
                            shipvar.shipName = 'ship3.png'
                            import MainFinal
                            loop = False
                            
                        elif ship4Title.rect.collidepoint(pygame.mouse.get_pos()) == True:
                            shipvar.shipName = 'ship4.png'
                            import MainFinal
                            loop = False
                            
                        elif quitButton.rect.collidepoint(pygame.mouse.get_pos()) == True:
                            pygame.quit()
                        elif importShip.rect.collidepoint(pygame.mouse.get_pos()) == True:
                            TKBox()
                            loop = False
                                    
                        else:
                            loop = False
            else:
                buttons.mouseHover = False
            buttons.draw()

        pygame.display.update()

        
load_ship()
        
        
