class Pos():

	""" class Pos for position handling"""
	def __init__(self,pos):
		self.x , self.y= pos[1] , pos[0]

	def __add__(self, pos):
		x= self.x + pos.x
		y= self.y + pos.y
		if 7 >= y >= 0 and 7 >= x>=0:
			return (y , x)	

	def pos(self):
		return (self.y ,self.x)
