#!/usr/bin/python3
#-*-coding : utf-8 -*-
#author : vicherlys

# Getting utility modules
try :
  from  UserInterface.Display import *
except ImportError as err :
  print("ImportationError occured at main.py: %s "%(err))


UI = Interface()

done = False 
UI.DrawChessBoard()
pygame.display.init()
while not done:
  UI.DrawChessBoard()
  pygame.display.update()



