from mcpi.minecraft import *
from time import *
mc = Minecraft.create()
class Tree(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def build(self):
        mc.setBlocks(self.x-1, self.y+3, self.z-1, self.x+1, self.y + 6, self.z+1, 18)
        mc.setBlocks(self.x,self.y,self.z,self.x,self.y+4,self.z,17)
    def clear(self):
        mc.setBlocks(self.x - 1, self.y + 3, self.z - 1, self.x + 1, self.y + 6, self.z + 1, 0)
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y + 4, self.z, 0)
pos = mc.player.getTilePos()
tree = Tree(pos.x,pos.y,pos.z)
while True:
    sleep(5)
    tree.build()
    sleep(5)
    tree.clear()