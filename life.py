import os, sys, time
try:
	import pygame
except Exception:
	os.system("python -m pip install pygame")
	import pygame

pygame.init()

with open("comms.txt", "r") as filename:
	inp = filename.read().split()
	alive = [(int(inp[i]), int(inp[i+1])) for i in range(0, len(inp), 2)]

FPS = 60
clock = pygame.time.Clock()

GPS = 0		#Generations Per Second = 2**GPS,	-3 <= GPS <= 4
offsetx = 0
offsety = 0
SIZECON = 2
size = 5	#square size = SIZECON*size,		1 <= size <= 10
pause = 1

NEXTGEN = pygame.USEREVENT + 1
pygame.time.set_timer(NEXTGEN, 1024//32)

screen = pygame.display.set_mode((1000,700))

def nextgen() -> None:
	global alive
	
	os.system("life.exe")
	
	with open("comms.txt", "r") as filename:
		inp = filename.read().split()
		alive = [(int(inp[i]), int(inp[i+1])) for i in range(0, len(inp), 2)]

def blitall() -> None:
	white = (255,255,255)
	black = (0,0,0)
	
	screen.fill(black)
	
	pygame.display.set_caption("Game of Life - " + str(2**GPS) + " GPS")
	for square in alive:
		pygame.draw.rect(screen, white, (square[0]*size*SIZECON+offsetx, square[1]*size*SIZECON+offsety, size*SIZECON, size*SIZECON))

keys = []
gencnt = 0
while(1):
	t1 = time.perf_counter()
	clock.tick(FPS)
	blitall()
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4 and size < 10: #scroll up
				size += 1
			elif event.button == 5 and size > 1: #scroll down
				size -= 1
		
		elif event.type == pygame.KEYDOWN:
			print(event.key)
			# 106-> J	107-> K		32-> space
			if event.key == 106 and GPS < 5:
				GPS += 1
			elif event.key == 107 and GPS > -3:
				GPS -= 1
			elif event.key == 32:
				pause = not pause
			elif event.key == 13 and pause:
				nextgen()
		
		elif event.type == NEXTGEN and not pause:
			gencnt = (gencnt+1)%(2**(5-GPS))
			
			if gencnt == 0:
				nextgen()
				with open("gentimes.txt", "a") as filename:
					filename.write(str(int((time.perf_counter()-t1)*1000)) + '\n')
			
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		offsety += 5
	if keys[pygame.K_s]:
		offsety -= 5
	if keys[pygame.K_a]:
		offsetx += 5
	if keys[pygame.K_d]:
		offsetx -= 5
	# print(offsetx, offsety)
