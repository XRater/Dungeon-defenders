

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
from cocos.euclid import Point2
from cocos.text import Label
from Tile_image import *

import random
				
class GameModel(Layer):

	is_event_handler = True
	
	def __init__(self):
		super(GameModel,self).__init__()
		
		self.x = 15
		self.y = 15
		
		self.map = {}
		for i in range (self.x):
			for j in range (self.y):
				self.map[(i, j)] = Tile(i, j)
			
	
	
	def draw(self):
		for i in range(self.x):
			for j in range (self.y):
				c = self.map.get((i, j))
				c.draw()
	
	def on_mouse_release(self, x, y, buttons, modifiers):
		mouse_x, mouse_y = director.get_virtual_coordinates(x, y)
		i = (mouse_x - 25)//50
		j = (mouse_y - 25)//50
		if (i >= 0) and (j >= 0) and (i < self.x) and (j < self.y):
			self.map[(i, j)].on_click()
				
								

class Tile(object):
	def __init__(self, map_pos_x, map_pos_y):
		super(Tile, self).__init__()
		global names
		self.namenumber = random.randint(0, 2)
		self.name = names[self.namenumber]
		self.map_pos_x = map_pos_x
		self.map_pos_y = map_pos_y
	
	def on_click(self):
		self.namenumber = (self.namenumber + 1) % len(names)
		self.name = names[self.namenumber]
	
	def draw(self):
		c = Tile_image.image[self.name]
		c.blit(self.map_pos_x*50 + 25, self.map_pos_y*50 + 25)
		
if __name__ == "__main__":	
	names = ['red', 'blue', 'yellow']
	director.init(width=800, height=800, caption="Hello World", fullscreen=False)
	backcolor = ColorLayer(255, 255, 255, 255)
	main_layer = GameModel()
	main_scene = Scene(backcolor, main_layer)
	director.run(main_scene)
