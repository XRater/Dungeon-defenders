from __future__ import division, print_function, unicode_literals
import six

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from const import *

class Aqua_Shield():
	def __init__(self, hero):
		self.hero = hero
	def effect(self):
		self.hero.stats.health = self.hero.stats.health + 20
		
class Glory_Cloak():
	def __init__(self, hero):
		self.hero = hero
	def effect(self):
		self.hero.techstats.exp_per_tile = self.hero.techstats.exp_per_tile*2

class Speed_Boots():
	def __init__(self, hero):
		self.hero = hero
	def effect(self):
		self.hero.techstats.speed = self.hero.techstats.speed + 1
		
class Flame_Sword():
	def __init__(self, hero):
		self.hero = hero
	def effect(self):
		self.hero.stats.attack = self.hero.stats.attack + 10
		
class Black_Mask():
	def __init__(self, hero):	
		self.hero = hero
		
	def effect(self):
		self.hero.effects.drain_life = 1
		
class Redking_Belt():
	def __init__(self, hero):	
		self.hero = hero
		
	def effect(self):
		self.hero.effects.revive_art = 1
		
class Holy_Wand():
	def __init__(self, hero):
		self.hero = hero
	def effect(self):
		self.hero.skills[0].skill.heal_power = self.hero.skills[0].skill.heal_power*2

class Redking_Amulet():
	def __init__(self, hero):
		self.hero = hero
	def effect(self):
		self.hero.skills[0].skill.add_armor = self.hero.skills[0].skill.add_armor + 3

class Smoke_Bomb():
	def __init__(self, hero):
		self.hero = hero
	def effect(self):
		self.hero.skills[0].skill.improve = 1
		
ArtEffects = {'aqua_shield' : Aqua_Shield, 'glory_cloak': Glory_Cloak, 'speed_boots': Speed_Boots, 'black_mask' : Black_Mask,
			  'holy_wand' : Holy_Wand, 'redking_belt' : Redking_Belt, 'redking_amulet' : Redking_Amulet, 'flame_sword' : Flame_Sword,
			  'smoke_bomb' : Smoke_Bomb}