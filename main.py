#!/usr/bin/python3
#-*-coding : utf-8 -*-
#author : vicherlys

# Getting utility modules
try :
  
  from UserInterface.Display import *
  from Board.Board import *
except ImportError as err :
  print("ImportationError occured at main.py: %s "%(err))


UI = Interface()

done = False 
UI.DrawChessBoard()
pygame.display.init()
while not done:
  for event in pygame.event.get():
    if event.type == QUIT:
      done = True
  UI.DrawChessBoard()
  UI.DrawPieces(chessTable)
  pygame.display.update()

