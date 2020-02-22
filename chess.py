from Board.Board import *

def pawnMoves (start):
	""" List all allowed moves for a pawns """
	global  turn , positions,currentPosIndex
	ptype  = False if turn < 0 else True

	if start.y == 1 or start.y==6:
		# Two steps for first move
		for i in range (2):
			position = start+Pos([(i+1)*turn , 0])
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

	
def checkPosition(pos):
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

def knightMoves(start):	
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
	if turn < 0 :
		king = 'k'
		rkingpos = whiteKing
		setTablePosContent(whiteKing, '')
	else :
		king = 'K'
		setTablePosContent(blackKing, '')
		rkingpos = blackKing
	check_position = []
	
	
	# case where the king is checked by a bishop
	for position in bishopMoves(kPos):
		posContent = getTablePosContent(position)
		if posContent.casefold() == "b" or posContent.casefold() == "q"  and isEnnemy(posContent):
			check_position.append( position)

	# case where the king is checked by a knight
	for position in knightMoves(kPos):
		posContent = getTablePosContent(position)
		if posContent.casefold() == "n" and isEnnemy(posContent):
			check_position.append( position)


	# case where the king is checked by a rook
	for position in rookMoves(kPos):
		posContent = getTablePosContent(position)
		if posContent.casefold() == "r" or posContent.casefold() == "q" and isEnnemy(posContent):
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
	setTablePosContent(rkingpos , king)
	return check_position	

# kingIsChecked function ... that check checks :3 
kingIsChecked= lambda position: len(kingChecks(position)) > 0

def isCastle(start , dest , king):
	""" allow castling """
	
	if king.casefold() != "k":
		return False 
	
	if turn>0:
		if blackCastled : return False
		king = Pos(blackKing)                  # e8
		kingsideRook  = Pos(translate_pos("a8"))  # a8 --> [0,0]
		queensideRook = Pos(translate_pos("h8"))  # h8 --> [0,7]
	else :
		if whiteCastled : return False
		king = Pos(whiteKing)                     # e1
		kingsideRook  = Pos(translate_pos("h1"))  # h1 --> [7,7]
		queensideRook = Pos(translate_pos("a1"))  # a1 --> [7,0]
	
	distK = ((kingsideRook.x - king.x)//2)*-1  # distance between the king and King-side rook
	distQ = ((queensideRook.x - king.x)//2)*-1 # distance between the king and Queen-side rook


	if dest == kingsideRook.pos() or dest == (kingsideRook.y, kingsideRook.x+distK ):
		for boardIndex in range(len(positions)):
			boardKing = getTablePosContent(king.pos() , positions[len(positions)-(boardIndex+1)])
			boardRook = getTablePosContent (kingsideRook.pos() , positions[len(positions)-(boardIndex+1)])
			if boardKing.casefold() != 'k' or boardRook.casefold() != 'r':
				return False

		if kingsideRook.x > king.x :
			sign  = 1
			space = 2
		else :
			sign  = -1
			space = 3
		
		for i in range(space ):
			pos = king+ Pos([0,(i+1)*sign])
			if getTablePosContent(pos) != "" :
				return False

			# if the 2 first cases  from king is intercepted by an ennemy , 
			# king can not castle
			if i<2:
				if kingIsChecked(pos):
					return False
	
	elif dest == queensideRook.pos() or dest == (queensideRook.y, queensideRook.x+distQ):
		for boardIndex in range (len(positions)):
			boardKing = getTablePosContent(king.pos() , positions[len(positions)-(boardIndex+1)])
			boardRook = getTablePosContent (queensideRook.pos() , positions[len(positions)-(boardIndex+1)])
			if boardKing.casefold() != 'k' or boardRook.casefold() != 'r':
				return False 

		if queensideRook.x > king.x :
			sign  = 1
			space = 2
		else :
			sign = -1
			space= 3
		
		for i in range(space ):
			pos = king+ Pos([0,(i+1)*sign])
			if getTablePosContent(pos) != "":
				return False
			if i<2:
				if kingIsChecked (pos):
					return False	
		
		
	else :
		return False
	
	return True

def castle(position, currentKing):
	"""castle the king"""
	global turn,currentPosIndex,positions,whiteCastled , blackCastled
	king = whiteKing if turn <0 else blackKing
	kingpos = Pos(king)
	x,y = kingpos.x ,str( 8-kingpos.y )
	if position[1] > x :
		rook = getTablePosContent( translate_pos("h"+y))
		setTablePosContent( translate_pos("e"+y) , "")
		setTablePosContent( translate_pos("h"+y) , "")
		setTablePosContent( translate_pos("f"+y) , rook)
		setTablePosContent( translate_pos("g"+y) , currentKing )
		king= translate_pos("g"+y)
	else :
		rook = getTablePosContent( translate_pos("a"+y))
		setTablePosContent( translate_pos("e"+y) , "")
		setTablePosContent( translate_pos("a"+y) , "")
		setTablePosContent( translate_pos("d"+y) , rook)
		setTablePosContent( translate_pos("c"+y) , currentKing )
		king = translate_pos("c"+y)
	
	if turn < 0:
		whiteKing[0],whiteKing[1]=king[0],king[1]
		whiteCastled = True
	else :
		blackKing[0],blackKing[1] = king[0],king[1]	
		blackCastled = True

	positions.append(copyboard(chessBoard))
	currentPosIndex += 1
	turn=turn*-1


def piecesMoves(p , pos ):

	p = p.casefold()

	if p == "p":
		return pawnMoves(pos)
	elif p == "b":
		return bishopMoves(pos)
	elif p == "r":
		return rookMoves(pos)
	elif p == "n":
		return knightMoves(pos)
	elif p == "q":
		return queenMoves(pos)
	elif p == "k":
		for move in kingMoves(pos):
			if not kingIsChecked(move):
				yield move
	else :
		return [] # returning an empty list of moves.

def checkmate(board):
	global currentPosIndex
	
	check = kingIsChecked(currentKing())
	if not check :
		return False	
	for y, row  in enumerate(board):
		for x, piece in enumerate(row):
			if rightTurnColor(piece  ) and piece != "":
				for move in piecesMoves(piece , Pos([y,x])   ):
					if not isPinned( piece , Pos([y,x]), move ):
						return False
	if check:
		return True   # checkmate
	else :
		return None   # pat 

def nullByMaterial (board):
	""" 
		 if there is only kings or only 1 bishop and / or 1 knight
	"""

	pass
	
def priseEnPassant(start , dest , pawn):
	""""""
	global currentPosIndex,positions
	moves = []
	start = Pos(start)
	
	if pawn.casefold() != "p":
		return False

	for i in [-1,1]:
		try:
			sp = start + Pos([0,i])

			target =  getTablePosContent(sp , positions[currentPosIndex])
			if target.casefold() == "p" and isEnnemy(target):
				if getTablePosContent( start+ Pos([turn*2 , i]) , positions[currentPosIndex-1]) == target:
					moves.append( start + Pos([turn , i]) )
		except IndexError:
			continue
	
	if dest in moves:
		return True
	return False

def prise( start , dest , pawn):
	makemove(start , dest , pawn)
	setTablePosContent( Pos(dest)+Pos([turn, 0]) , "")


def isPinned ( piece  , position  , dest):
	pinned = False
	setTablePosContent(position.pos() , "")
	destCntnt = getTablePosContent(dest)
	setTablePosContent(dest , piece)

	currentking = whiteKing if turn < 0 else blackKing
	if kingIsChecked(currentking):
		pinned = True

	setTablePosContent(position.pos(),piece)
	setTablePosContent(dest , destCntnt)
	return pinned


