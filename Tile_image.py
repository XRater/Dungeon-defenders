from __future__ import division, print_function, unicode_literals

import pyglet

class Tile_image(object):
	
	Tile_images = ['red', 'blue', 'yellow', 'floor']
	
	greytile = pyglet.resource.image('tiles/block_black.png')
	floortile = pyglet.resource.image('tiles/block_floor.png')
	image = {tile: pyglet.resource.image('tiles/block_%s.png' %tile) for tile in Tile_images}