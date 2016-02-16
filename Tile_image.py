from __future__ import division, print_function, unicode_literals

import pyglet

class Tile_image(object):
	
<<<<<<< HEAD
	Tile_images = ['red', 'blue', 'yellow']
	
	image = {tile: pyglet.resource.image('block_%s.png' %tile) for tile in Tile_images}
=======
	Tile_images = ['red', 'blue', 'yellow', 'floor']
	
	greytile = pyglet.resource.image('tiles/block_black.png')
	floortile = pyglet.resource.image('tiles/block_floor.png')
	image = {tile: pyglet.resource.image('tiles/block_%s.png' %tile) for tile in Tile_images}
>>>>>>> origin/master
