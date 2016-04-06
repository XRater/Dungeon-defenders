from __future__ import division, print_function, unicode_literals
import six

from const import *

class Flash_heal():
	def __init__(self, hero, model):
	
		self.heal_power = 5
		self.cd = 3
		
		self.lvl = 1
		self.learnt = 1
		self.hero = hero
		self.model = model
		self.cd_left = 0
		self.available = 1
		self.object = 'hero'
		
	def use(self):
		self.model.skill_use = self
	
	def end_cast(self, hero):
		self.model.controler.heal_hero(hero.name, self.heal_power)
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

class Circle_of_light():
	def __init__(self, hero, model):
	
		self.duration = 2 #Считая этот ход
		self.cd = 4
	
		self.lvl = 2
		self.learnt = 0
		self.hero = hero
		self.model = model
		self.cd_left = 0
		self.available = 1
		
	def use(self):
		self.hero.turnav = self.hero.turnav - 1
		self.hero.effects.circle_of_light = self.duration
		for dx, dy in adject_tiles:
				i = self.hero.map_posx + dx
				j = self.hero.map_posy + dy
				if (i >= 0) and (j >= 0) and (i < Quad_side) and (j < Quad_side):
					tile = self.model.map.get((i, j))
					tile.open_P = 1
		self.cd_left = self.cd
		self.available = 0
		
	def next_turn(self):
		if self.cd_left:
			self.cd_left = self.cd_left - 1
			if self.cd_left == 0:
				self.available = 1