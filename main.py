#!/usr/bin/python3
#-*-coding : utf-8 -*-
#author : vicherlys

"""Chess Engine AI"""

listcopy = lambda x: [ n for n in x]
# Table representation.

"""

chess board representaiton
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

chessTable = [["" for x in range(8)] for x in range(8)]
pions = ["p", "r","b" , "k" , "q" , "n"]
order =  ["r", "n", "b", "q", "k", "b", "n" , "r" ]

# Chess board initialisation.
chessTable[0] = listcopy( order )
chessTable[7] = listcopy( order )
chessTable[6] = ["p" for _ in range (8)]
chessTable[1]  = listcopy(chessTable[6])


for x in range(8) : print(chessTable[x], x )

""" Games rules implemenation."""
# Algebric notation translation to position
def translate_pos(pos):
  if pos != "" and len(pos) == 2:#replace to regex
    x= ["a","b","c","d","e","f","g","h"].index(pos[0])
    return [ int(pos[1])-1 , x] 
  else : raise Exception

inp = input("Enter position")
pos= translate_pos(inp)

def getTablePosContent(pos):
  return chessTable[pos[0]][pos[1]]

def setTablePosContent(pos , elt):
  chessTable[pos[0]][pos[1]] = elt
  return True

# Choice Making algorithm.
def move(chessTable):
  pass

# User Interface.

