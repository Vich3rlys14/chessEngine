#!/usr/bin/python3
#-*-coding : utf-8-*-
#author : vicherlys

# Getting utility modules

try :
	import math
	from UserInterface.Display import *
	from Board.Board import *

except ImportError as err :
  print("ImportationError occured at main.py: %s "%(err))


UI = Interface()
lock = False #Locking the screen position of a dragged piece
draggedPiece = None
tablePos = lambda pos : (math.floor(pos[1]/case_size), math.floor(pos[0]/case_size))

""" Drag and Drop implementation"""
def dropPiece(position):
	global draggedPiece,lock
	lock = False
	setTablePosContent( tablePos(position), draggedPiece)
	print ("A {} was dropped at case :{} ...".format(draggedPiece,tablePos(position)))


def dragPiece(mousePos) :
	global lock,draggedPiece
	if lock == True:
		UI.DrawPieceDrag(draggedPiece,mousePos)

	else:
		mpos = tablePos(mousePos)
		draggedPiece = getTablePosContent(mpos)
		if (-1 != getTablePosContent(mpos) != ""):
			setTablePosContent(mpos, -1)
			lock = True
	return True

UI.DrawChessBoard()
pygame.display.init()

gameover= False

while not gameover:
	UI.DrawChessBoard()
	UI.DrawPieces(chessBoard)

	for event in pygame.event.get():
		if event.type == QUIT:
			gameover=True
		elif event.type == MOUSEMOTION:
			mouse = pygame.mouse.get_pos()
			if pygame.mouse.get_pressed()[0] :
				dragPiece(mouse)

	if pygame.mouse.get_pressed()[0] !=1 and lock == True :
		dropPiece(mouse)

	elif pygame.mouse.get_pressed()[0] and lock==True:
		dragPiece(pygame.mouse.get_pos())

	pygame.display.update()
