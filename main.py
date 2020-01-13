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
draglock = False #Locking the screen position of a dragged piece
draggedPiece = None
startdrag=None
tablePos = lambda pos : (math.floor(pos[1]/case_size), math.floor(pos[0]/case_size))


""" Drag and Drop implementation"""
def dropPiece(position):
	global draggedPiece,draglock,startdrag
	draglock = False
	for row in chessBoard:
		print (row)
	if (isLegalMove( startdrag,tablePos(position))):
		makemove( startdrag , tablePos(position) , draggedPiece)

	print ("A {} was dropped at case :{} ,it is illegal".format(draggedPiece,tablePos(position)))


def dragPiece(mousePos) :
	global draglock,draggedPiece,startdrag
	if draglock == True:
			
		UI.DrawPieceDrag(draggedPiece ,startdrag ,mousePos)
	else:
		mpos = tablePos(mousePos)
		print(mpos)
		draggedPiece = getTablePosContent(mpos)
		if ( getTablePosContent(mpos) != ""):
			startdrag = mpos
			draglock = True
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

	if pygame.mouse.get_pressed()[0] !=1 and draglock == True :
		print("drop position ",mouse)
		dropPiece(mouse)

	elif pygame.mouse.get_pressed()[0] and draglock==True:
		dragPiece(pygame.mouse.get_pos())

	pygame.display.update()
