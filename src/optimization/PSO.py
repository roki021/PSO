'''
Created on Dec 29, 2018

@author: Vlada
'''

from optimization.ann_criterion import optimality_criterion
from numpy.random import uniform

cp_start = 2.5;   # inicijalna vrednost kognitivnog faktora
cp_end   = 0.5;   # finalna vrednost kognitivnog faktora
cg_start = 0.5;   # inicijalna vrednost socijalnog faktora
cg_end   = 2.5;   # finalna vrednost socijalna faktora 
w_start  = 0.9;   # inicijalna vrednost inercijalnog faktora
w_end    = 0.4;   # finalna vrednost inercijalnog faktora

class Particle(object):
    def __init__(self, w):
        self.position = w[:]
        self.velocity = list(uniform(-1, 1, 60))
        self.peronal_best = self.position[:]
        self.feval = optimality_criterion(self.position)
        self.feval_best = self.feval
    
    
class PSO(object):     
    def __init__(self):
        pass
        