import getch


KEY_CTRL_C = 3
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_Z = 122

class Hero:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.icon = '^'
	
	def run(self):
		print('---------------------')
		print('w:up, a:left, s:right, z:down')
		print('ctrl-c:quit')
		print('---------------------')
		
		while(True):
			key = ord(getch.getch())
			if key == KEY_CTRL_C: # Quit
				print('bye!!')
				break;
			elif key == KEY_W: # Up
				self.icon = '^'
				self.y -= 1
			elif key == KEY_A: # Left
				self.icon = '<'
				self.x -= 1
			elif key == KEY_S: # Right
				self.icon = '>'
				self.x += 1
			elif key == KEY_Z: # Down
				self.icon = 'V'
				self.y += 1
			else:
				continue
			print('ICON:{}, X{}, Y{}'.format(self.icon, self.x, self.y))
			
			
hero = Hero(0,0)
hero.run()
