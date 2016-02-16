from __future__ import division, print_function, unicode_literals

import pyglet

class Tile_image(object):
	
	Tile_images = ['red', 'blue', 'yellow']
	
	image = {tile: pyglet.resource.image('block_%s.png' %tile) for tile in Tile_images}