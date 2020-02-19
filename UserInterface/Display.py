import pygame
from UserInterface.constants import *
from pygame.locals import *
pygame.init()

class Interface ():
  def __init__(self):
    self.case_size = 50
    self.height = self.width = self.case_size*8
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.init()
	
  def reverseChessBoard():
    """ Reversing chessboard for pvp mode """
    return True

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
  
  def DrawPieceDrag(self,piece , dragStart ,pos):
 
    img = pieces[piece.lower()]
    img = img[1] if piece.isupper() else img[0]
		
    startcase = pygame.Surface((self.case_size , self.case_size))
    startcase.fill(covercolor)

    pos = (pos[0]-self.case_size/2,pos[1]-self.case_size/2)
    startpos = ( dragStart[1]*self.case_size , dragStart[0]*self.case_size)

    self.screen.blit (startcase ,startpos)
    self.screen.blit( img,pos)
		

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
	    
