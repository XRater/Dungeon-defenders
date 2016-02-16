

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
<<<<<<< HEAD
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
=======
from HUD import *
from status import *
from gamemodel import *

import random

class GameView(Layer):
	
	def __init__(self, model):
		super(GameView, self).__init__()
		self.mapx = Quad_side
		self.mapy = Quad_side
		self.end_of_init(model)
		
		
	def end_of_init(self, model):
		self.model = model
		self.PView = GameView_P(model)
		self.DMView = GameView_DM(model)
		self.curr_player = self.DMView
		self.add(self.curr_player)
				
	def next_turn(self):
		if (self.curr_player == self.PView):
			self.remove(self.PView)
			self.add(self.DMView)
			self.curr_player = self.DMView
		elif(self.curr_player == self.DMView):
			self.remove(self.DMView)
			self.add(self.PView)
			self.curr_player = self.PView
			
			
class GameView_DM(GameView):
	
	is_event_handler = True	
	
	def end_of_init(self, model):
		self.HUD = HUD_DM()
		self.add(Buttons())
		self.add(self.HUD, z = -1)
		self.act_tile_sprite = 0
	
	def reload(self):
		self.act_tile_sprite = 0
		
	def draw(self):
		if (self.act_tile_sprite):
			self.act_tile_sprite.draw()
		for i in range(self.mapx):
			for j in range (self.mapy):
				c = self.parent.model.map.get((i, j))
				if (c.open_DM == 1):
					c.draw()
				elif (c.open_DM == 0):
					floortile = Sprite(Tile_image.floortile, c.position)
					floortile.draw()
				if self.parent.model.map['actual_tile'] == (i, j):
					w, h = director.get_window_size()
					Sprite(pyglet.resource.image('frame.png'), ((2*i + 1)*Tile_size/2 + left_space, (2*j + 1)*Tile_size/2 + (h - Quad_side*Tile_size)/2)).draw()
	
	def on_mouse_release(self, x, y, buttons, modifiers):
	
		#reaction on map click
		w, h = director.get_window_size()
		mouse_x, mouse_y = director.get_virtual_coordinates(x, y)
		i = (mouse_x - left_space)//Tile_size
		j = (mouse_y - (h - Quad_side*Tile_size)/2)//Tile_size
		if self.parent.model.map['actual_tile']	!= (-1, -1):
			last_tile = self.parent.model.map['actual_tile']	= (i, j)
		if (i >= 0) and (j >= 0) and (i < self.mapx) and (j < self.mapy):
			c = self.parent.model.map.get((i, j))
			c.on_click_DM()
			self.act_tile_sprite = Sprite(c.image, (1500, 800), scale = 4)
			self.parent.model.map['actual_tile']	= (i, j)
		
		#reaction on next turn button  click		
		if (mouse_x <= w) and (mouse_x >= w - Button_size) and (mouse_y >= 0) and (mouse_y <= Button_size):
			self.parent.next_turn()


			
class GameView_P(GameView):
	
	is_event_handler = True	
	
	def end_of_init(self, model):
		self.HUD = HUD_P()
		self.add(Buttons())
		self.add(self.HUD, z = -1)
	
		
	def draw(self):
		for i in range(self.mapx):
			for j in range (self.mapy):
			
				c = self.parent.model.map.get((i, j))
				if (c.open_P == 1):
					c.draw()
				elif (c.open_P == 0):
					greytile = Sprite(Tile_image.greytile, c.position)
					greytile.draw()
					
				if self.parent.model.map['actual_tile'] == (i, j):
					w, h = director.get_window_size()
					Sprite(pyglet.resource.image('frame.png'), ((2*i + 1)*Tile_size/2 + left_space, (2*j + 1)*Tile_size/2 + (h - Quad_side*Tile_size)/2)).draw()
	
	def on_mouse_release(self, x, y, buttons, modifiers):
	
		#reaction on map click
>>>>>>> origin/master
		w, h = director.get_window_size()
		mouse_x, mouse_y = director.get_virtual_coordinates(x, y)
		i = (mouse_x - left_space)//Tile_size
		j = (mouse_y - (h - Quad_side*Tile_size)/2)//Tile_size
<<<<<<< HEAD
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
=======
		if self.parent.model.map['actual_tile']	!= (-1, -1):
			last_tile = self.parent.model.map['actual_tile']	= (i, j)
		if (i >= 0) and (j >= 0) and (i < self.mapx) and (j < self.mapy):
			c = self.parent.model.map.get((i, j))
			c.on_click_P()
			self.parent.model.map['actual_tile']	= (i, j)
			
		#reaction on next turn button  click
		if (mouse_x <= w) and (mouse_x >= w - Button_size) and (mouse_y >= 0) and (mouse_y <= Button_size):
			self.parent.next_turn()
			self.parent.curr_player.reload()
	
		
class Buttons (Layer):
	
	def __init__(self):
		super(Buttons, self).__init__()
		self.img = pyglet.resource.image('next_turn.png')
		w, h = director.get_window_size();
		self.nextturn_button = Sprite(self.img, (w - Button_size/2, Button_size/2))
	
	def draw ( self ):
		self.nextturn_button.draw()

	
def get_newgame_DM():
	gamescene = Scene()
	model = GameModel()
	gamescene.add(GameView(model))
	gamescene.add(Background(), z = -2)
>>>>>>> origin/master
	
	return gamescene