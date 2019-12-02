import pygame
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


