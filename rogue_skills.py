from __future__ import division, print_function, unicode_literals
import six

from const import *

class Smoke():
	def __init__(self, hero, model):
	
		self.smoke_duration = 3
		self.cd = 3
		
		self.lvl = 1
		self.improve = 0
		self.learnt = 1
		self.hero = hero
		self.model = model
		self.cd_left = 0
		self.available = 1
		self.object = 'tile'
		
	def use(self):
		self.model.skill_use = self

	
	def end_cast(self, tile):
	
		tile.smoke = self.smoke_duration
		self.hero.turnav = self.hero.turnav - 1
		self.cd_left = self.cd
		self.available = 0
		self.model.skill_use = 0
		if self.improve:
			for dx, dy in adject_tiles:
				i = tile.map_pos_x + dx
				j = tile.map_pos_y + dy
				if (i >= 0) and (j >= 0) and (i < Quad_side) and (j < Quad_side):
					adtile = self.model.map.get((i, j))
					adtile.smoke = self.smoke_duration
	
	def next_turn(self):
		if self.cd_left:
			self.cd_left = self.cd_left - 1
			if self.cd_left == 0:
				self.available = 1
				
	def cancel(self):
		self.model.skill_use = 0


class Check_the_line():
	def __init__(self, hero, model):
	
		self.cd = 3
		
		self.lvl = 2
		self.learnt = 0
		self.hero = hero
		self.model = model
		self.cd_left = 0
		self.available = 1
		self.object = 'tile'
		
	def use(self):
		self.model.skill_use = self
	
	def end_cast(self, tile):
		if (self.hero.map_posx == tile.map_pos_x)^(self.hero.map_posy == tile.map_pos_y):
			if (self.hero.map_posx == tile.map_pos_x):
				dx = 0
				dy = -(self.hero.map_posy - tile.map_pos_y)/abs(self.hero.map_posy - tile.map_pos_y)
			elif (self.hero.map_posy == tile.map_pos_y):
				dx = -(self.hero.map_posx - tile.map_pos_x)/abs(self.hero.map_posx - tile.map_pos_x)
				dy = 0
			x = self.hero.map_posx + dx
			y = self.hero.map_posy + dy
			monster = 0 
			while (x >= 0) and (y >= 0) and (x < Quad_side) and (y < Quad_side) and (monster == 0):
				new_tile = self.model.map.get((x, y))
				if (new_tile.monster):
					new_tile.open_P = 1
					monster = 1
				x = x + dx
				y = y + dy
			self.hero.turnav = self.hero.turnav - 1
			self.cd_left = self.cd
			self.available = 0
			self.model.skill_use = 0
	
	def next_turn(self):
		if self.cd_left:
			self.cd_left = self.cd_left - 1
			if self.cd_left == 0:
				self.available = 1
				
	def cancel(self):
		self.model.skill_use = 0

Rogue_Skill = {'rogue_1': Smoke, 'rogue_2' : Check_the_line}