from __future__ import division, print_function, unicode_literals
import six

from const import *

class Weapon_upgrade():
	def __init__(self, hero, model):
	
		self.add_armor = 2
		self.cd = 3
	
		self.lvl = 1
		self.learnt = 1
		self.hero = hero
		self.model = model
		self.cd_left = 0
		self.available = 1
		
	def use(self):
		self.hero.turnav = self.hero.turnav - 1
		self.hero.stats.armor = self.hero.stats.armor + self.add_armor
		self.cd_left = self.cd
		self.available = 0
		
	def next_turn(self):
		if self.cd_left:
			self.cd_left = self.cd_left - 1
			if self.cd_left == 0:
				self.available = 1
				
class Break_the_wall():
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
		if (tile.open_P) and (abs(self.hero.map_posx - tile.map_pos_x) + abs(self.hero.map_posy - tile.map_pos_y) <= 1) and (tile.name == 'wall'):
			tile.name = 'floor'
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
	
#	def get_layer(self)
#		layer = Weapon_upgrade_layer()

#class Weapon_upgrade_layer():
	