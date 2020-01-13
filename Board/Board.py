from Board.Position import Pos


listcopy = lambda x: [ n for n in x]
copyboard = lambda board : [ listcopy(line) for line in board]

def printBoard(board):
	""" Debugging function """
	for line in board:
		print (line)

# Table representation.
"""
chess board representation

whites : uppercase
black  : lowercase

 ----------------
|R N B Q K B N R |0 black side
|P P P P P P P P |1
|                |2
|                |3
|                |4
|                |5
|p p p p p p p p |6
|r n b q k b n r |7 white side
 ----------------

"""

chessBoard = [["" for x in range(8)] for x in range(8)]

pions = ["p","r","b","k","q","n"]
order = ["r","n","b","q","k","b","n","r" ]

# Chess board initialisation.
chessBoard[0] = [ i.capitalize() for i in order ]
chessBoard[7] = listcopy( order )
chessBoard[6] = ["p" for _ in range (8)]
chessBoard[1] = ["P" for _ in range (8)]

turn = -1 # it is the value for white , 1 for black . first turn white 
moves = list()
isEnnemy = lambda a,b: a.isupper() != b.isupper()

"""
Games rules implemenation.
"""

""" coordinate translation to position notation"""
coordToNote = lambda pos:"abcdefgh"[pos[1]-1]+str(8-pos[0])

positions= []
movesList = []

positions.append( copyboard(chessBoard) ) # Append initial position
currentPosIndex = 0

print(positions)

def makemove(startdrag , destination , draggedPiece):
	""" Making move function"""
	global chessBoard , positions, currentPosIndex
	print ("A {} was dropped at case :{} ,it is a legal move".format(draggedPiece,destination))
	setTablePosContent( destination, draggedPiece)
	setTablePosContent( startdrag , "")
	positions.append(copyboard(chessBoard))
	currentPosIndex += 1

""" position notation translation to coordinate"""
def translate_pos(pos):
  if len(pos) == 2:# check with a regex the correct format
    x= "abcdefgh".index(pos[1])
    return [int(pos[0])-1 , x] 
  else : raise Exception

def getTablePosContent(pos, board=chessBoard):
	if (pos != None):
		return board[pos[0]][pos[1]]
	raise IndexError

def setTablePosContent(pos , elt):
  chessBoard[pos[0]][pos[1]] = elt
  return True

def pawnMoves (start):
	""" List all allowed moves for a pawns """
	global  turn , positions,currentPosIndex
	legal_moves = []
	ptype  = False if turn < 0 else True

	if start.y == 1 or start.y==6:
		# Two steps for first move
		for i in range (2):
			position = start+Pos([(i+1)*turn , 0])
			print("position = {}".format(position))
			try:
				if ( getTablePosContent(position) == ""):
					#legal_moves.append(position)
					yield position
			except IndexError:
				continue
	else:
		# normal pawn moves
		movePos = start+Pos([turn,0])
		try:
			if getTablePosContent(movePos) == "":
				#legal_moves.append(movePos)
				yield movePos
		except IndexError:
			pass

	for i in [-1,1]:
		try:
			p = start +Pos([turn,i])				
			target =  getTablePosContent(p , positions[currentPosIndex])

			#allowing to take ennemies
			if  target != "" and ptype != target.isupper():
				#legal_moves.append(p)
				yield p

			#taking by side pass (prise en passant)
			sp = start + Pos([0,i])
			target =  getTablePosContent(sp , positions[currentPosIndex])
			if target.casefold() == "p"and ptype != target.isupper():
				if getTablePosContent( start+ Pos([turn*2 , i]) , positions[currentPosIndex-1]) == target:
					#legal_moves.append(p) 
					yield p
				
		except IndexError :
			continue
	return legal_moves


def kingMoves(start):
	""""""
	global  turn, positions,currentPosIndex
	directions = [-1,0,1]
	king  = getTablePosContent(start.pos())
	moves = list()
	


	for x in directions:
		for y in directions:
			if not x == y == 0 :
				move = ( start+ Pos([y,x]))
				try:
					dest = getTablePosContent(move)
					if isEnnemy(king , dest ) or dest == "" :
						moves.append(move)
				except IndexError:
					continue
	return moves


def rookMoves(start):
	
	global  turn, positions, currentPosIndex
	d = [-1,1]
	for i in range(4):
		x,y =  0,0
		v = d[i%2]

		if i < 2 : x = v
		else :  y = v
		
		direction = Pos([y,x])
		
		dirNextCase = start+ direction
		followDir = True
		while dirNextCase != None and followDir:
			caseContent = getTablePosContent(dirNextCase)
			currentPiece = getTablePosContent([start.y,start.x])
			if caseContent == "":
				yield dirNextCase
			elif caseContent != "" and isEnnemy(currentPiece,caseContent)   :
				followDir = False
				yield dirNextCase
			
			elif caseContent != "" and not (isEnnemy(currentPiece,caseContent)):
				followDir = False

			else:
				followDir = False
			dirNextCase = Pos(dirNextCase)+ direction


def queenMoves(start):
	""""""
	global  turn, positions, currentPosIndex
		
	d = [-1,0,1]
	for x in d:
		for y in d:
			if not x == y == 0:
				direction = Pos([y,x])
		
				dirNextCase = start+ direction
				followDir = True
				while dirNextCase != None and followDir:
					caseContent = getTablePosContent(dirNextCase)
					currentPiece = getTablePosContent([start.y,start.x])
					if caseContent == "":
						yield dirNextCase
					elif caseContent != "" and isEnnemy(currentPiece,caseContent)   :
						followDir = False
						yield dirNextCase
			
					elif caseContent != "" and not (isEnnemy(currentPiece,caseContent)):
						followDir = False

					else:
						followDir = False
					dirNextCase = Pos(dirNextCase)+ direction


def bishopMoves(start):
	""""""
	global  turn, positions, currentPosIndex
	
	d = [-1,1]
	for x in d:
		for y in d:
			direction = Pos([y,x])
			dirNextCase = start+direction
			
			followDir = True
			while dirNextCase != None and followDir:
				caseContent = getTablePosContent(dirNextCase)
				currentPiece = getTablePosContent([start.y,start.x])
				if caseContent == "":
					yield dirNextCase
				elif caseContent != "" and isEnnemy(currentPiece,caseContent)   :
					followDir = False
					yield dirNextCase
			
				elif caseContent != "" and not (isEnnemy(currentPiece,caseContent)):
					followDir = False

				else:
					followDir = False
				dirNextCase = Pos(dirNextCase)+ direction

	

def knightMoves(start):
	""""""
	global  turn, positions, currentPosIndex
	d = [-1,1]

	def checkPosition(pos):
		if pos == None:
			return False
		p = getTablePosContent(pos)
		if p != "":
			if isEnnemy(getTablePosContent([start.y,start.x]) , p) :
				return True
			else:
				return False
		else :
			return True
		
	for i in range(4):
		x,y =  0,0
		v = d[i%2]*2

		if i < 2 :
			x = v
			for n in d:
				y = n
				movePos = start + Pos([y,x])
				if checkPosition(movePos):
					yield movePos

		else :
			y = v
			for n in d:
				x = n
				movePos = start + Pos([y,x])
				if checkPosition(movePos):
					yield movePos


def isLegalMove( start,dest ):
	global chessBoard, turn , positions,currentPosIndex
	isLegal = False

	ptype = getTablePosContent(start , positions[currentPosIndex] )

	legal_moves = []
	start = Pos(start)

	if not (turn > 0) == ptype.isupper():
		print(isLegal)
		return isLegal

	if start == dest: return False

	# implementation of pawns deplacement
	if ptype.casefold() == "p": # if is a pawn
		if dest in pawnMoves(start): legal_moves.append(dest)
	
	elif ptype.casefold() == "k":
		legal_moves = kingMoves(start)

	elif ptype.casefold() == "b":
		if dest in bishopMoves(start): legal_moves.append(dest)

	elif ptype.casefold() == "n":
		if dest in knightMoves(start): legal_moves.append(dest)

	elif ptype.casefold() == "q":
		if dest in queenMoves(start): legal_moves.append(dest)

	elif ptype.casefold() == "r":
		if dest in rookMoves(start) : legal_moves.append(dest)
			

	print(legal_moves)
	if dest in legal_moves:
		isLegal = True
		turn = turn*-1

	return isLegal
