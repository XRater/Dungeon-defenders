

from __future__ import division, print_function, unicode_literals
import six

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pyglet
from pyglet.gl import *
from pyglet import image

from cocos.director import *
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.actions import *
from cocos.sprite import Sprite
from cocos.text import Label

from Tile_image import *
from const import *
from HUD import HUD

import random
				
class GameModel(Layer):

	is_event_handler = True
	global coin_images
	def __init__(self):
		super(GameModel,self).__init__()
		
		
		self.x = Quad_side
		self.y = Quad_side
		self.init_map()
	def draw(self):
		for i in range(self.x):
			for j in range (self.y):
				c = self.map.get((i, j))
				c.draw()
				if self.map['actual_tile'] == (i, j):
					w, h = director.get_window_size()
					Sprite(pyglet.resource.image('frame.png'), ((2*i + 1)*Tile_size/2 + left_space, (2*j + 1)*Tile_size/2 + (h - Quad_side*Tile_size)/2)).draw()
	
	def init_map(self):
		self.map = {}
		self.map['actual_tile'] = (-1, -1)
		w, h = director.get_window_size()
		for i in range (self.x):
			for j in range (self.y):
				self.map[(i, j)] = Tile(Tile_image.image['red'], (2*i + 1)*Tile_size/2 + left_space, (2*j + 1)*Tile_size/2 + (h - Quad_side*Tile_size)/2, i, j)
		
		
	def on_mouse_release(self, x, y, buttons, modifiers):
		w, h = director.get_window_size()
		mouse_x, mouse_y = director.get_virtual_coordinates(x, y)
		i = (mouse_x - left_space)//Tile_size
		j = (mouse_y - (h - Quad_side*Tile_size)/2)//Tile_size
		if self.map['actual_tile']	!= (-1, -1):
			last_tile = self.map['actual_tile']	= (i, j)
			#last_tile.unclick()
		if (i >= 0) and (j >= 0) and (i < self.x) and (j < self.y):
			c = self.map.get((i, j))
			c.on_click()
			self.map['actual_tile']	= (i, j) 

				
class Tile(Sprite):
	def __init__(self, image, posx, posy ,map_pos_x, map_pos_y):
		super(Tile, self).__init__(image, (posx, posy))
		self.namenumber = 0
		self.name = 'red'
		self.map_pos_x = map_pos_x
		self.map_pos_y = map_pos_y
	
	def on_click(self):
		self.namenumber = (self.namenumber + 1) % len(names)
		self.name = names[self.namenumber]
		self.image = Tile_image.image[self.name] 
		
	
	#def unclick(self):	

def get_newgame():
	gamescene = Scene()
	hud_layer = HUD()
	main_layer = GameModel()
	gamescene.add(hud_layer, z = 2)
	gamescene.add(main_layer, z = 3)
	
	return gamescene