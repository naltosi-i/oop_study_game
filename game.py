import getch


KEY_CTRL_C = 3
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_Z = 122


class Map:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		self.hero = Hero(3, 3, self.is_movable, self.draw)
		
	def run(self):
		self.hero.run()
	
	# 勇者が座標x,yに動ければTrueを返すメソッド
	def is_movable(self, x, y):
		if x < 0:
			return False
		elif self.width - 1 < x :
			return False
		elif y < 0:
			return False
		elif self.height - 1 < x:
			return False
		return True
	
	# 画面に現在の状態を描画するメソッド
	def draw(self):
		# 辞書のキーにx,yのタプル、バリューにキャラクターアイコンを登録
		characters = {}
		characters[(self.hero.x, self.hero.y)] = self.hero.icon
		
		# 各行をテキストで返すメソッド内の関数
		def get_row(y):
			row_list = []
			row_list.append('|') # 行の左端
			for x in range(0, self.width):
				# (x,y)にキャラクターがいればそれを描画し、いなければ空白を描画
				if (x, y) in characters:
					row_list.append(characters[(x,y)])
				else:
					row_list.append(' ')
			row_list.append('|') # 行の右端
			return ''.join(row_list)
			
		# 各行を連結してマップを作成
		map_list = []
		map_list.append('+{}+\n'.format('-' * self.width)) # 一番上の行
		for y in range(0, self.height):
			map_list.append(get_row(y))
		map_list.append('+{}+\n'.format('-' * self.width)) # 一番下の行
		
		# マップをprintで描画
		print(''.join(map_list))


class Hero:
	def __init__(self, x, y, is_movable, draw):
		self.x = x
		self.y = y
		self.icon = '^'
		self.is_movable = is_movable
		self.draw = draw
	
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
				if self.is_movable(self.x, self.y-1):
					self.y -= 1
			elif key == KEY_A: # Left
				self.icon = '<'
				if self.is_movable(self.x-1, self.y):
					self.x -= 1
			elif key == KEY_S: # Right
				self.icon = '>'
				if self.is_movable(self.x+1, self.y):
					self.x += 1
			elif key == KEY_Z: # Down
				self.icon = 'V'
				if self.is_movable(self.x, self.y+1)
					self.y += 1
			else:
				continue
				
			self.draw()
			
			
dqmap = Map(7,7)
dqmap.run()
