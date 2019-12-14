listcopy = lambda x: [ n for n in x]

# Table representation.
"""
chess board representation

 ----------------
|r n b q k b n r |0 black side
|p p p p p p p p |1
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
chessBoard[1]  = ["P" for _ in range (8)]


""" Games rules implemenation."""
# coordinate translation to position notation
# position notation translation to coordinate
def translate_pos(pos):
  if pos != "" and len(pos) == 2:# make a regex later for checking this
    x= ["a","b","c","d","e","f","g","h"].index(pos[0])
    return [ int(pos[1])-1 , x] 
  else : raise Exception

def getTablePosContent(pos):
  return chessBoard[pos[0]][pos[1]]

def setTablePosContent(pos , elt):
  chessBoard[pos[0]][pos[1]] = elt
  return True

def checkmove( newpos ):
	pass	

# Choice Making algorithm.
def move(chessBoard,start,dest):
  pass
