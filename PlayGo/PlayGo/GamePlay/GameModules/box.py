# -*- coding:utf-8 -*-

import pyglet
import resource, fx
from .. import control

class Box(pyglet.sprite.Sprite):
    def __init__(self, initbox, *args, **kwargs):
        super(Box, self).__init__(initbox, *args, **kwargs)
        counter = 1
        self.mouseHandler = control.on_mouse_drag()

    def update(self, dt):
        #super(Box, self).update(dt)
        pass

    def checkNeighbor(self):
        cross = [(x,0) for x in [-1,1]]+[(0,y) for y in [-1,1]]

    def delete(self):
        return super(Box, self).delete()

    def boom(self):

        pass
    def boomAnimation(self):
        pass
    #def boomAnimation(self):
    #    self.explosion = pyglet.image.load('Explosion.png')
    #    self.explosion_seq = pyglet.image.ImageGrid(explosion, 1, 8)
    #    self.animation = pyglet.image.load_animation(self.explosion_seq)
    #    self.bin = pyglet.image.atlas.TextureBin()
    #    self.animation.add_to_texture_bin(self.bin)
    #    self.sprite = pyglet.sprite.Sprite(self.animation)

    
