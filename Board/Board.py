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

blacks : uppercase
whites  : lowercase

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

isEnnemy  = lambda target: target.isupper() != (turn>0)
# The following variables track the positions of both sides kings
blackKing , whiteKing = [0,4] , [7,4]


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

def setKingPos( king , pos):
	global blackKing , whiteKing
	if king < 0:
		whiteKing = pos
	else:
		blackKIng = pos

def pawnMoves (start):
	""" List all allowed moves for a pawns """
	global  turn , positions,currentPosIndex
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
					if isEnnemy(dest ) or dest == "" :
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
			elif caseContent != "" and isEnnemy(caseContent)   :
				followDir = False
				yield dirNextCase
			
			elif caseContent != "" and not (isEnnemy(caseContent)):
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
					elif caseContent != "" and isEnnemy(caseContent)   :
						followDir = False
						yield dirNextCase
			
					elif caseContent != "" and not (isEnnemy(caseContent)):
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
				elif caseContent != "" and isEnnemy(caseContent)   :
					followDir = False
					yield dirNextCase
			
				elif caseContent != "" and not (isEnnemy(caseContent)):
					followDir = False

				else:
					followDir = False
				dirNextCase = Pos(dirNextCase)+ direction

	

def knightMoves(start):
	def checkPosition(pos):
		#checking if the knight can go to this position
		if pos == None:
			return False
		p = getTablePosContent(pos)
		if p != "":
			if isEnnemy(p) :
				return True
			else:
				return False
		else :
			return True

	""""""
	global  turn, positions, currentPosIndex
	d = [-1,1]

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


def kingChecks(kingPos):
	""" This method , generate all positions from where
			the current king is checked , in the position taken
	"""
	# kingPos is a [y,x] position,translate to Pos instance
	kPos = Pos(kingPos)
	#current king's color , (lowercase:white , uppercase: black)
	king = 'k' if turn < 0 else 'K'
	check_position = []

	# case where the king is checked by a queen
	for position in queenMoves(kPos):
		positionContent = getTablePosContent(position)
		if positionContent.casefold() == "q" and isEnnemy(positionContent):
				check_position.append(position)
	
	# case where the king is checked by a bishop
	for position in bishopMoves(kPos):
		posContent = getTablePosContent(position)
		if posContent.casefold() == "b" and isEnnemy(posContent):
			check_position.append( position)

	# case where the king is checked by a bishop
	for position in knightMoves(kPos):
		posContent = getTablePosContent(position)
		if posContent.casefold() == "n" and isEnnemy(posContent):
			check_position.append( position)


	# case where the king is checked by a rook
	for position in rookMoves(kPos):
		posContent = getTablePosContent(position)
		if posContent.casefold() == "r" and isEnnemy(posContent):
			check_position.append( position)

	# for pawns moves , king is checked only if
	# the pawn can take the king
	for d in [1,-1]:
		position = kPos+Pos([1,d])
		try:
			posContent = getTablePosContent(position)
			if isEnnemy (posContent) and posContent.casefold() == "p":
				check_position.append(position)
		except IndexError :
			continue
	
	return check_position	

# kingIsChecked function ... that check checks :3 
kingIsChecked= lambda position: len(kingChecks(position)) > 0

def isCastle(start , dest):
	pass
def priseEnPassant(start , dest):
	pass

def isLegalMove( start,dest ):
	global chessBoard, turn , positions,currentPosIndex
	isLegal = False

	ptype = getTablePosContent(start , positions[currentPosIndex] )

	legal_moves = []
	start = Pos(start)

	if not (turn > 0) == ptype.isupper():
		return isLegal

	if start == dest: return False

	# implementation of pawns deplacement
	if ptype.casefold() == "p": # if is a pawn
		if dest in pawnMoves(start): legal_moves.append(dest)
	
	elif ptype.casefold() == "k":
		legal_moves = kingMoves(start)
		if  kingIsChecked(dest):
			return False

	elif ptype.casefold() == "b":
		if dest in bishopMoves(start): legal_moves.append(dest)

	elif ptype.casefold() == "n":
		if dest in knightMoves(start): legal_moves.append(dest)

	elif ptype.casefold() == "q":
		if dest in queenMoves(start): legal_moves.append(dest)

	elif ptype.casefold() == "r":
		if dest in rookMoves(start) : legal_moves.append(dest)

	
	if dest in legal_moves:
		isLegal = True
			
	currentking = whiteKing if turn < 0 else blackKing
	
	if isLegal:
		if ptype.casefold() != "k":
			# if the piece is pinned it can't move
			setTablePosContent(start.pos() , "")
			destCntnt = getTablePosContent(dest)
			setTablePosContent(dest , ptype)
	
			if kingIsChecked(currentking):
				isLegal= False
			setTablePosContent(start.pos(),ptype)
			setTablePosContent(dest , destCntnt)

		else:
			setKingPos(turn , dest)
	

	#everything is okey , switch turn
		
	if isLegal : turn = turn*-1
	print("whiteking :",whiteKing,"\n blackKing :", blackKing);
	 

	return isLegal
