import pygame
import algorithm
import tools

pygame.init()
result = 0
EMPTY = 0
BLACK = 1
WHITE = 2
player_chess=0
black_color = [0, 0, 0]
white_color = [255, 255, 255]
pvp_result=0

class RenjuBoard(object):
	
	def __init__(self):
		self._board = [[]]*15
		self.reset()
	
	
	def reset(self):
		for row in range(len(self._board)):
			self._board[row] = [EMPTY]*15
			
	def move(self, row, col, is_black):
		if self._board[row][col] == EMPTY:
			self._board[row][col] = BLACK if is_black else WHITE
			return True
		return False
	

	def turn(self, text, screen, size):
		font = (255, 0, 0)
		flame = (255, 255, 255)
		pygame.draw.rect(screen, flame, [620,480,170,45], 2)
		self_font = pygame.font.SysFont(None, size)
		self_text = self_font.render(text , True, font)
		screen.blit(self_text, (630,490))
		pygame.display.flip()
		
	def draw(self, screen):
		global pvp_result
		global player_chess
		global result
		background = (139,105,20)
		screen.fill(background)
		Background = pygame.image.load("pictures/back.png").convert_alpha()
		screen.blit(Background,(0,0))
		
		for i in range(1, 16):
			pygame.draw.line(screen, black_color, [40, 40*i], [600, 40*i], 1)
			pygame.draw.line(screen, black_color, [40*i, 40], [40*i, 600], 1)
		
		pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)
		
		pygame.draw.circle(screen, black_color, [320, 320], 4, 0)
		pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
		pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
		pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
		pygame.draw.circle(screen, black_color, [480, 480], 3, 0)
		
		button = (52, 53, 54)
		pygame.draw.rect(screen, button, [640,100,145,40], 2)
		pygame.draw.rect(screen, button, [640,150,145,40], 2)
		pygame.draw.rect(screen, button, [640,200,145,40], 2)
		#pygame.draw.rect(screen, button, [640,250,120,40], 3)
		pygame.draw.rect(screen, button, [640,350,115,45], 3)
		self_font = pygame.font.SysFont(None, 40)
		text1 = self_font.render("man-man", True, button)
		text2 = self_font.render("man-com", True, button)
		text3 = self_font.render("com-man", True, button)
		#text4 = self_font.render("Retract", True, button)
		text5 = self_font.render("Replay", True, button)
		screen.blit(text1,(650,110))
		screen.blit(text2,(650,160))
		screen.blit(text3,(650,210))
		#screen.blit(text4,(650,260))
		screen.blit(text5,(650,360))
		
		for row in range(len(self._board)):
			for col in range(len(self._board[row])):
				if self._board[row][col] != EMPTY:
					ccolor = black_color if self._board[row][col] == BLACK else white_color
					pos = [40*(col+1), 40*(row+1)]
					
					if ccolor == black_color:
						Black_chess = pygame.image.load("pictures/black_chess.png").convert_alpha()
						width,height = Black_chess.get_size()
						Black_chess = pygame.transform.smoothscale(Black_chess,(width//11,height//11))
						screen.blit(Black_chess, (40*col+20,40*row+20))
						
					elif ccolor == white_color:
						White_chess = pygame.image.load("pictures/white_chess.png").convert_alpha()
						width,height = White_chess.get_size()
						White_chess = pygame.transform.smoothscale(White_chess,(width//11,height//11))
						screen.blit(White_chess, (40*col+20,40*row+20))
						
					if tools.check_win(self._board)!=False:
						if tools.check_win(self._board)[0]==player_chess:
							result=1
							Win = pygame.image.load("pictures/win.png").convert_alpha()
							width,height = Win.get_size()
							Win = pygame.transform.smoothscale(Win,(width//2,height//2))
							screen.blit(Win, (125,100))

						elif tools.check_win(self._board)[0]!=player_chess and tools.check_win(self._board)[0]!=0 and player_chess!=0:
							Lose = pygame.image.load("pictures/lose.png").convert_alpha()
							width,height = Lose.get_size()
							Lose = pygame.transform.smoothscale(Lose,(width//2,height//2))
							screen.blit(Lose, (125,100)) 
							result=1 
							
						elif tools.check_win(self._board)[0]==0:
							result=1
							Draw = pygame.image.load("pictures/draw.png").convert_alpha()
							width,height = Draw.get_size()
							Draw = pygame.transform.smoothscale(Draw,(width//2,height//2))
							screen.blit(Draw, (145,100))
    
						else:
							Win = pygame.image.load("pictures/win.png").convert_alpha()
							width,height = Win.get_size()
							Win = pygame.transform.smoothscale(Win,(width//2,height//2))
							screen.blit(Win, (125,100))
							result=1
							
							if tools.check_win(self._board)[0]==1:
								pvp_result=1
							else:
								pvp_result=2
						    	
	                        
					
					

class Chess(object):
	
	def __init__(self, x, y, is_black):
		self._is_black = is_black
		self._row = x
		self._col = y
	
	def is_black(self):
		return self._is_black
		
	def row(self):
		return self._row
		
	def col(self):
		return self._col



			
def main():
	global pvp_result
	global result
	board = RenjuBoard()
	is_black = True
	mode=''
	menu=1
	pygame.init()
	screen = pygame.display.set_mode((800, 640))
	pygame.display.set_caption('Gobang')
	board.draw(screen)
	board.turn("   choose", screen, 45)
	pygame.display.flip()
	running = True
	gameover = True
	
	while running:
		global player_chess
		if menu!=1 and pvp_result==0 and result!=1:
        
			if is_black == 1:
				board.draw(screen)
				board.turn("black walk", screen, 45)
			else:
				board.draw(screen)
				board.turn("white walk", screen, 45)
			    
		if pvp_result==1:
			board.draw(screen)
			board.turn("black win", screen, 45)
			pvp_result=-1
		if pvp_result==2:
			board.draw(screen)
			board.turn("white win", screen, 45)
			pvp_result=-1
		
			
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				running = False
			
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and result==1:
					board.reset()
					pvp_result=0
					result=0
					gameover = True
					is_black = True
					mode=''
					menu=1
					board.draw(screen)
					board.turn("   choose", screen, 45)
					pygame.display.flip()
				
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameover:
				x, y = event.pos
				if 20<=x<=600 and 20<=y<=600 and mode!='':
					row = round((y-40)/40)
					col = round((x-40)/40)

					if  mode=='man-man' and board.move(row, col, is_black):
						screen.fill((139, 105, 20))
						board.draw(screen)
						pygame.display.flip()
						is_black = not is_black
					
					if  mode=='man-com' and board.move(row, col, is_black):
						screen.fill((139, 105, 20))
						board.draw(screen)
						board.turn("white walk", screen, 45)
						pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
						pygame.display.flip()
						a=algorithm.choose(board._board,2,2)
						board.move(a[0], a[1], 0)
						board.draw(screen)
						board.turn("black walk", screen, 45)
						pygame.display.flip()
						pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
					if mode=='com-man' and board.move(row,col,is_black):	
						screen.fill((139, 105, 20))
						board.draw(screen)
						board.turn("black walk", screen, 45)
						pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
						pygame.display.flip()
						a=algorithm.choose(board._board,2,1)
						board.move(a[0], a[1], 1)
						board.draw(screen)
						pygame.display.flip()
						pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
				if 640<=x<=785 and 100<=y<=140:
					if(mode!='man-man'):
						menu=0
						mode='man-man'
						board.reset()
						gameover=True
						is_black=True
						board.draw(screen)
						board.turn("black walk", screen, 45)
						pygame.display.flip()
							
				if 640<=x<=785 and 150<=y<=190:
					print(mode)
					if(mode!='man-com'):
						menu=0
						mode='man-com'
						player_chess=BLACK
						board.reset()
						gameover=True
						is_black=True
						board.draw(screen)
						board.turn("black walk", screen, 45)
						pygame.display.flip()

				if 640<=x<=785 and 200<=y<=240:
					if(mode!='com-man'):
						menu=0
						mode='com-man'
						player_chess=WHITE
						board.reset()
						gameover=True
						is_black=False
						board.move(7, 7, 1)
						board.draw(screen)
						pygame.display.flip()
						
				if 640<=x<=755 and 350<=y<=395:
					board.reset()
					gameover = True
					is_black = True
					mode=''
					menu=1
					board.draw(screen)
					board.turn("   choose", screen, 45)
					pygame.display.flip()
										    
	pygame.quit()


if __name__ == '__main__':
	main()
