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
from HUD import *
from status import *

import random

class GameModel(Layer):

	def __init__(self):
		super(GameModel, self).__init__()
		self.mapx = Quad_side
		self.mapy = Quad_side
		self.init_map()

	def init_map(self):
		self.map = {}
		self.map['actual_tile'] = (-1, -1)
		w, h = director.get_window_size()
		for i in range (self.mapx):
			for j in range (self.mapy):
				self.map[(i, j)] = Tile(Tile_image.floortile, (2*i + 1)*Tile_size/2 + left_space, (2*j + 1)*Tile_size/2 + (h - Quad_side*Tile_size)/2, i, j)
				
				
class Tile(Sprite):

	def __init__(self, image, posx, posy ,map_pos_x, map_pos_y):
		super(Tile, self).__init__(image, (posx, posy))
		self.namenumber = 0
		self.name = 'red'
		self.map_pos_x = map_pos_x
		self.map_pos_y = map_pos_y
		self.open_P = 0
		self.open_DM = 0
	
	def on_click_DM(self):
		self.namenumber = (self.namenumber + 1) % len(names)
		self.name = names[self.namenumber]
		self.image = Tile_image.image[self.name] 
		self.open_DM = 1
	
	def on_click_P(self):
		self.open_P = 1