from __future__ import division, print_function, unicode_literals
import six

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.append("../skills")

import pyglet
from pyglet.gl import *
from pyglet import image

from cocos.director import *
from cocos.layer import *
from cocos.sprite import Sprite

from const import *
from wizard_skills import *
from warrior_skills import *
from rogue_skills import *
from priest_skills import *
	
Skills = {'wizard_1': Clairvoyance, 'wizard_2' : Teleport, 
		  'priest_1': Flash_heal, 'priest_2': Circle_of_light,
		  'warrior_1': Weapon_upgrade, 'warrior_2': Break_the_wall,
		  'rogue_1' : Smoke, 'rogue_2': Check_the_line}	

