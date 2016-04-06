from __future__ import division, print_function, unicode_literals
import six

from const import *

class Clairvoyance():
	def __init__(self, hero, model):
	
		self.cd = 3
		
		self.lvl = 1
		self.learnt = 1
		self.hero = hero
		self.model = model
		self.cd_left = 0
		self.available = 1
		self.object = 'tile'
		
	def use(self):
		self.model.skill_use = self
	
	def end_cast(self, tile):
		self.hero.turnav = self.hero.turnav - 1
		tile.open_P = 1
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
		
class Teleport():
	def __init__(self, hero, model):
	
		self.cd = 3
		self.distance = 5
		
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
		if (tile.open_P) and (abs(self.hero.map_posx - tile.map_pos_x) + abs(self.hero.map_posy - tile.map_pos_y) < self.distance):
			self.hero.turnav = self.hero.turnav - 1
			self.hero.on_turn(tile)
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
