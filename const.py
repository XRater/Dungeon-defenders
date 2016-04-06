from __future__ import division, print_function, unicode_literals

from tech_const import *

screen_scale = 1

tile_names = ['lava', 'ice', 'poison', 
			  'fly_weak', 'fly_strong', 
			  'beatwidow_weak', 'beatwidow_strong',
			  'floor', 'wall',
			  'treasure', 'smoke']
hero_stat = ['health', 'int', 'exp']
heroes = ['wizard', 'priest', 'warrior', 'rogue']


ExpNeed = [0, 30, 70, 120, 180]
maxlvl = 5
exp_per_tile = 10
luck_per_tile = 40

Tech_stat = {
			'wizard': {'speed': 1, 'maxhp': 100, 'attack': 30, 'armor': 30},
			'priest': {'speed': 1, 'maxhp': 100, 'attack': 30, 'armor': 30},
			'warrior': {'speed': 1, 'maxhp': 140, 'attack': 30, 'armor': 30},
			'rogue': {'speed': 2, 'maxhp': 80, 'attack': 30, 'armor': 30}
			}	
	
Skills = ['warrior_1', 'wizard_1', 'priest_1', 'rogue_1',
		  'rogue_2', 'wizard_2', 'priest_2', 'warrior_2']
			
			
Wizard_skills = [('wizard_1', 0), ('wizard_2', 1)]			
Priest_skills = [('priest_1', 0), ('priest_2', 1)]
Warrior_skills = [('warrior_1', 0), ('warrior_2', 1)]
Rogue_skills = [('rogue_1', 0), ('rogue_2', 1)]

Hero_skills = {'wizard': Wizard_skills, 'priest' : Priest_skills, 'warrior': Warrior_skills, 'rogue': Rogue_skills}

Traps = ['lava', 'ice', 'poison']
Monsters = ['fly', 'beatwidow']
Magic = ['curse']
Walls = ['wall', 'floor']

lava_damage = 100
trap_poison_damage = 7
trap_poison_duration = 5

Object_list = {'trap': Traps, 'monster': Monsters, 'magic': Magic, 'wall': Walls}
Cost_list = {'lava': 100, 'ice' : 100, 'poison' : 100, 
             'fly' : 250, 'beatwidow' : 250,
			 'curse': 500,
			 'wall': 100, 'floor': 0}
			 
Moneyperturn = 200
starting_money = 1000

Artefacts = ['mage_wand', 'aqua_shield', 'bandit_sword',
			'black_mask', 'crystal_dagger', 'frost_staff', 
			'glory_cloak', 'katana_sword', 'mage_hat',
			'priest_robe', 'redking_amulet', 'redking_belt',
			'redking_hat', 'rogue_knife', 'royal_ring',
			'sharp_ring', 'speed_boots', 'holy_wand',
			'redking_boots', 'flame_sword', 'smoke_bomb']

drain_health = 5
drain_armor = 1
drain_attack = 1	

Art_wizard_1 = ['royal_ring', 'black_mask', 'redking_belt', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_wizard_2 = ['black_mask', 'holy_wand', 'royal_ring', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_wizard_3 = ['frost_staff', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_wizard_4 = ['mage_hat', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_wizard_5 = ['black_mask', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']

Art_priest_1 = ['holy_wand', 'glory_cloak', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_priest_2 = ['holy_wand', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_priest_3 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_priest_4 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_priest_5 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']

Art_warrior_1 = ['aqua_shield', 'redking_amulet', 'flame_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_warrior_2 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_warrior_3 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_warrior_4 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_warrior_5 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']

Art_rogue_1 = ['aqua_shield', 'flame_sword', 'smoke_bomb', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_rogue_2 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_rogue_3 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_rogue_4 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']
Art_rogue_5 = ['aqua_shield', 'flame_sword', 'katana_sword', 'bandit_sword', 'mage_hat', 'frost_staff']

Art_wizard = {1 : Art_wizard_1, 2 : Art_wizard_2, 3 : Art_wizard_3, 4 : Art_wizard_4, 5 : Art_wizard_5}
Art_priest = {1 : Art_priest_1, 2 : Art_priest_2, 3 : Art_priest_3, 4 : Art_priest_4, 5 : Art_priest_5}
Art_warrior = {1 : Art_warrior_1, 2 : Art_warrior_2, 3 : Art_warrior_3, 4 : Art_warrior_4, 5 : Art_warrior_5}
Art_rogue = {1 : Art_rogue_1, 2 : Art_rogue_2, 3 : Art_rogue_3, 4 : Art_rogue_4, 5 : Art_rogue_5} 
Art_menu = {'wizard': Art_wizard, 'priest': Art_priest, 'warrior': Art_warrior, 'rogue': Art_rogue}