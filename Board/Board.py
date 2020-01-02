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

def isLegalMove( chessBoard,start,dest ):
	global turn , positions,currentPosIndex
	isLegal = False

	print (len(positions) )	
	ptype = getTablePosContent(start , positions[currentPosIndex] )

	print( "this should'nt output -1 : the output-> ", ptype)

	legal_moves = []
	start = Pos(start)


	if start == dest: return False

	# implementation of pawns deplacement
	if ptype.casefold() == "p": # if is a pawn
		if start.y == 1 or start.y==6:
			# Two steps for first move
			for i in range (2):
				position = start+Pos([(i+1)*turn , 0])
				print("position = {}".format(position))
				try:
					if ( getTablePosContent(position) == ""):
						legal_moves.append(position)
				except IndexError:
					continue
		else:
			# normal pawn moves
			movePos = start+Pos([turn,0])
			try:
				if getTablePosContent(movePos) == "":
					legal_moves.append(movePos)
			except IndexError:
				pass
		
		for i in [-1,1]:
			try:
				p = start +Pos([turn,i])				
				target =  getTablePosContent(p , positions[currentPosIndex])
				#allowing to take ennemies
				if  target != "" and ptype.isupper() != target.isupper():
					legal_moves.append(p)
				#taking by side pass (prise en passant)
				
				sp = start + Pos([0,i])
				target =  getTablePosContent(sp , positions[currentPosIndex])
				if target.casefold() == "p"and ptype.isuper() != target.isupper():
					if getTablePosContent( start+ Pos([turn*2 , i]) , positions[currentPosIndex-1]) == target:
						legal_moves.append(p) 
				
			except IndexError :
				continue
		
			

		print(legal_moves)
		if dest in legal_moves:
			isLegal = True
			turn = turn*-1

	return isLegal
