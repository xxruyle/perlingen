import noise 
import pygame 
import numpy as np 
from perlin_noise import PerlinNoise


noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=15)
noise4 = PerlinNoise(octaves=40)


def clamp(num, min_value, max_value): 
    return max(min(num, max_value), min_value)



grid_size = 1000
wind_size = grid_size * 1
scale = grid_size // 1

diff = 350.0

world = []
for i in range(grid_size): 
    row = []
    for j in range(grid_size):
        noise_val = noise1([i/diff, j/diff])
        noise_val += 0.5 * noise2([i/diff, j/diff])
        noise_val += 0.25 * noise3([i/diff, j/diff])
        noise_val += 0.125 * noise4([i/diff, j/diff])
        row.append(noise_val)
    world.append(row)


print(world)

screen = pygame.display.set_mode((wind_size, wind_size))
loop = True 


def draw_grid(grid): 
    x = 0 
    y = 0 
    for row in grid: 
        for char in row: 
            if char < -0.24: 
                color = pygame.Color("#00a3cc")
            elif char < -0.18: 
                color = pygame.Color("#00cafc")
            elif char < -0.09:
                color = pygame.Color("#2ed5ff")
            elif char < -.045: # Water
                color = pygame.Color("#5fdfff")
            elif char < -0.01: # Sand
                color = pygame.Color(255,238,173)
            elif char < 0.1: 
                color = pygame.Color(38,139,7)
            elif char < 0.2: 
                color = pygame.Color(19,133,16)
            elif char < 0.3: 
                color = pygame.Color(17,124,19)
            elif char < 0.4: 
                color = pygame.Color(19,109,21)
            elif char < 0.5: 
                color = pygame.Color("#a8a6a5")
            elif char < 0.6: 
                color = pygame.Color("#6a6963")
            elif char < 0.7: 
                color = pygame.Color("White")
            bar = pygame.Rect(x, y, grid_size // scale, grid_size // scale)
            pygame.draw.rect(screen, color, bar) 
            x += grid_size // scale
        x = 0 
        y += grid_size // scale 

while loop: 
    draw_grid(world)


    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
           loop = False 