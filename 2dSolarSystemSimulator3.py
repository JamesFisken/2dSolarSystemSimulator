import pygame
import time
import random
import math

#variables

width = 800
height = 600
fps = 60
delay = 1000 / fps
background_color = (0, 0, 20)
planet_color =(255, 255, 255)
celestial_bodies = []
num_of_bodies = 2

unit = 5.972 * 10**24 

G = 66.73
pi = 3.141592

x = 300
y = 300


#start pygame
pygame.init()


screen = pygame.display.set_mode((width, height))



#title and icon
pygame.display.set_caption("2dSolarSystemSimulator")
#icon = pygame.image.load("")


class celestial_body:
	def __init__(self, x, y, radius, density, velocity_x, velocity_y):
		self.x = x 					#LocationX
		self.y = y 					#LocationY
		self.radius = radius
		self.density = density	
		self.mass = self.radius*self.density
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y
		self.body_color = (self.radius*5, self.radius*3.5, self.radius*3.5)
		
def find_distance(x1, x2, y1, y2):
	return ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
	
def find_direction(x1, x2, y1, y2):
	value = math.atan2(x2-x1, y2-y1) # in radians
	if value  < 0:
		value = value * -1
		value += 180
	return value



for x in range(num_of_bodies):
	celestial_bodies.append(celestial_body(random.randint(0, 600), random.randint(0, 600), random.randint(5, 50), 1, 0, 0))
	

def checkforcollisions():
	for x, celestial_body in enumerate(celestial_bodies):
		for i, celestial_body2 in enumerate(celestial_bodies):
				
				if x != i and find_distance(celestial_body.x, celestial_body2.x, celestial_body.y, celestial_body2.y) < celestial_body.radius + celestial_body2.radius:
					print("collision")
					del celestial_bodies[x]

def calculate_new_xy(old_xy,speed,angle_in_radians):
	
    new_x = old_xy.x + (speed*math.cos(angle_in_radians))
    new_y = old_xy.y + (speed*math.sin(angle_in_radians))
    
    return new_x, new_y
    
    
def calculate_gravity(body):
	global G
	other_bodies = celestial_bodies.copy()
	other_bodies.remove(body)
	
	
	for other_body in other_bodies:
		distance = abs(find_distance(body.x, other_body.x, body.y, other_body.y))
		direction = find_direction(body.x, other_body.x, body.y, other_body.y)
		gradient = math.tan(direction)
		
		mass1 = body.mass
		mass2 = other_body.mass
		
		
		
		#force = (G*mass1*mass2)/(distance**2) 
		forceMagnitude = G * (mass1 * mass2) / distance**2
		
		
		xy = calculate_new_xy(body, 0.1, direction)
		body.x = xy[0] 
		body.y = xy[1]
		print(forceMagnitude)
	
		
#GameLoop
running = True
while running:
	time.sleep(delay/1000)
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			running = False
	
	keys = pygame.key.get_pressed()
	
	screen.fill(background_color)
	
	for celestial_body in celestial_bodies:
		
		calculate_gravity(celestial_body)
		
		
		celestial_body.x += celestial_body.velocity_x
		celestial_body.y += celestial_body.velocity_y
		
		
		
		if celestial_body.y > height or celestial_body.y < 0:
			celestial_body.velocity_y = celestial_body.velocity_y*-1
			
		if celestial_body.x > width or celestial_body.x < 0:
			celestial_body.velocity_x = celestial_body.velocity_x*-1
		pygame.draw.circle(screen, celestial_body.body_color,[celestial_body.x, celestial_body.y], celestial_body.radius, 0)
			

	
			
			
	
	#checkforcollisions()
	
	pygame.display.flip()
