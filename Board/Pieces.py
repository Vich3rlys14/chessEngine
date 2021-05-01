from Board.Board import *

pieces  = {
	"p" : {  # pawn
		"moves" : pawnMoves ,
		"value" : 10 ,
	},
	"k": {
		"moves" : kingMoves,
		"value" : 900
	},
	"q": {
		"moves" : queenMoves,
		"value" : 90
	},
	"n": {
		"moves" : knightMoves,
		"value" : 30
	},
	"b": {
		"moves" : bishopMoves,
		"value" : 30
	},
	"r": {
		"moves" : rookMoves,
		"value" : 50
	}
}