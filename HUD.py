

from __future__ import division, print_function, unicode_literals
import six

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pyglet
from pyglet.gl import *
from pyglet import image

from cocos.director import *
from cocos.layer import *
from cocos.sprite import Sprite

from const import *

import random
				
class Background( Layer ):
    def __init__(self):
        super( Background, self ).__init__()
        self.img = pyglet.resource.image('Background.png')

    def draw( self ):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()

class Coin (Layer):
	def __init__(self):
		super(Coin, self).__init__()
<<<<<<< HEAD
		self.coins = [pyglet.resource.image('coins/coin%s.png' %  coin_image) for coin_image in range(Coin_image_number)]
		self.coin_anim  = pyglet.image.Animation.from_image_sequence(self.coins, 0.1, True)
		self.coin = Sprite(self.coin_anim, (1400, 900))
	def draw(self):
		self.coin.draw()
	
class HUD(Layer):
	def __init__(self):
		
		super( HUD, self).__init__()
		self.add( Background(), z = 0 )
		self.add( Coin(), z = 2 )
=======
		w, h = director.get_window_size()
		self.coins = [pyglet.resource.image('coins/coin%s.png' %  coin_image) for coin_image in range(Coin_image_number)]
		self.coin_anim  = pyglet.image.Animation.from_image_sequence(self.coins, 0.1, True)
		self.coin = Sprite(self.coin_anim, (w - 300, h - 50))
	def draw(self):
		self.coin.draw()		
	
class HUD_DM(Layer):
	def __init__(self):
		
		super( HUD_DM, self).__init__()
		#self.add( Background(), z = 0 )
		self.add( Coin(), z = 2 )
		
class HUD_P(Layer):
	def __init__(self):
		
		super( HUD_P, self).__init__()
		#self.add( Background(), z = 0 )
>>>>>>> origin/master
