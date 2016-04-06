from __future__ import division, print_function, unicode_literals
import six

import sys
import os

import random

class Controler():
	def __init__(self, model):
		self.model = model
	
	def damage_hero(self, name, damage):
		self.hero = self.model.heroes[name]
		self.hero.stats.health = self.hero.stats.health - damage
		self.model.interface_DM.portraits[name].reload(self.model, name)
		if (self.hero.stats.health <= 0):
			if (self.hero.alive):
				self.hero.health = 0
				self.kill_hero(name)
				
	def heal_hero(self, name, heal):
		self.hero = self.model.heroes[name]
		self.hero.stats.health = min(self.hero.stats.health + heal, self.hero.techstats.max_health)
		self.model.interface_DM.portraits[name].reload(self.model, name)
		
	def lvlup_hero(self, name):
		self.hero = self.model.heroes[name]
		self.hero.stats.lvl = self.hero.stats.lvl + 1
		self.hero.stats.exp = 0
		if len(self.hero.skills) >= self.hero.stats.lvl:
			self.hero.skills[self.hero.stats.lvl - 1].skill.learnt = 1
		
	
	def kill_hero(self, name):
		self.hero = self.model.heroes[name]
		surr = 0
		if self.hero.effects.revive_art:
			surr = 1
			del self.hero.staff[0]
			self.hero.av_art.append('redking_belt')
			self.heal_hero(self.hero.name, 50)
			for i in range(5):
				if (self.hero.staff.get(i) == None):
					self.hero.art_cell = i
					break
		if (surr == 0):
			self.hero.alive = 0
			self.model.alive_heroes.remove(self.hero.name)
			self.model.on_gameover()
	
		
		