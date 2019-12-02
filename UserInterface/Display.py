
import pygame
from pygame.locals import *
pygame.init()
black = 0x000000
white = 0xffffff
class Interface ():

  def __init__(self):
    self.case_size = 50
    self.height = self.width = self.case_size*8
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.init()
  
  def DrawChessBoard(self):
    case_color = lambda x : black if x == -1 else white

    for x in range(8):

      f_col = -1
      if (x%2 == 0 ):
        f_col = 1
      for y in range(8):
        col = f_col
        if (y %2 ==1):
          col = -(f_col)

        case = pygame.Surface((self.case_size , self.case_size))
        case.fill(case_color(col))
        self.screen.blit(case, (x*self.case_size , y*self.case_size))   
