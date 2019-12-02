
import pygame
from pygame.locals import *
pygame.init()
# Colors
black = 0x33333
white = 0xffffff
#Pieces
wpawn = pygame.image.load("./Sprites/whitePawn.png")
bpawn = pygame.image.load("./Sprites/blackPawn.png")
wKing = pygame.image.load("./Sprites/whiteKing.png")
bKing = pygame.image.load("./Sprites/blackKing.png")
wQueen= pygame.image.load("./Sprites/whiteQueen.png")
bQueen= pygame.image.load("./Sprites/blackQueen.png")
wbishop = pygame.image.load("./Sprites/whiteBishop.png")
bbishop = pygame.image.load("./Sprites/blackBishop.png")
wknight = pygame.image.load("./Sprites/whiteKnight.png")
bknight = pygame.image.load("./Sprites/blackKnight.png")
wrook = pygame.image.load("./Sprites/whiteRook.png")
brook = pygame.image.load("./Sprites/blackRook.png")

pieces = { "r": [wrook,brook] , 'p': [wpawn,bpawn] , 'k':[wKing,bKing] , 'q': [wQueen, bQueen], 'b':[wbishop,bbishop] , 'n' :[wknight,bknight]}

class Interface ():

  def __init__(self):
    self.case_size = 50
    self.height = self.width = self.case_size*8
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.init()
  
  def DrawChessBoard(self):
    case_color = lambda x : black if x == -1 else white

    for x in range(8):
      f_col = 1 if (x%2 == 0 ) else -1
      for y in range(8):
        col = f_col
        if (y %2 ==1):
          col = -(f_col)
        case = pygame.Surface((self.case_size , self.case_size))
        case.fill(case_color(col))
        self.screen.blit(case, (x*self.case_size , y*self.case_size))
  def DrawPieces(self,board):
    for x in range(len(board)):
      for y in range(len(board)):
        for p in pieces:
          images = pieces[p]
          image = ""
          if board[x][y] == p:
            image= images[0]
          elif  board[x][y] == p.capitalize():
            image= images[1]
          if image != "":
            self.screen.blit(image , (y*self.case_size , x*self.case_size))
     
