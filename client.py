# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:29:16 2020

@author: katherine lamoureux
enceladus - client code
https://www.pygame.org/

https://www.youtube.com/watch?v=McoDjOCb2Zo
bookmark: 13:45

https://techwithtim.net/tutorials/game-development-with-python/

"""

import pygame

width = 500
height = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.val = 3
    
    def draw(self, win):
        py;game.draw.rect(win, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.val
            
        if keys[pygame.K_RIGHT]:
            self.x += self.val
            
        if keys[pygame.K_UP]:
            self.y -= self.val
            
        if keys[pygame.K_DOWN]:
            self.y += self.val


def redrawWindow():
    
    win.fill((255,255,255))
    pygame.display.update()
    
def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        redrawWindow()
        
