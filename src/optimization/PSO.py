from optimization.ann_criterion import optimality_criterion
import numpy as np 

# inicijalne opcije algoritma
options = { 'max_it'       : 100,
            'particle_num' : 10,
            'dim'          : 60,
            'bounds'       : (-10, 10), 
            'cp_start'     : 2.5,   # inicijalna vrednost kognitivnog faktora
            'cp_end'       : 0.5,   # finalna vrednost kognitivnog faktora
            'cg_start'     : 0.5,   # inicijalna vrednost socijalnog faktora
            'cg_end'       : 2.5,   # finalna vrednost socijalna faktora 
            'w_start'      : 0.9,   # inicijalna vrednost inercijalnog faktora
            'w_end'        : 0.4 }   # finalna vrednost inercijalnog faktora}

class Particle(object):
    def __init__(self, w):
        self.position = np.array(w)
        self.velocity = list(np.random.uniform(-1, 1, 60))
        self.peronal_best = self.position[:]
        self.feval = None
        self.feval_best = None
        
    def evalute(self, func):
        self.feval = func(self.position)
        
        if self.feval_best is None or self.feval < self.feval_best:
            self.feval_best = self.feval
            self.peronal_best = self.position
        #elif self.feval < self.feval_best:
        #    self.feval_best = self.feval
        #    self.peronal_best = self.position
    
    def update_data(self, swarm_best_pos, iteration, opt):
        w = interpolation(opt['w_start'], opt['w_end'], opt['max_it'], 0, iteration)
        cp = interpolation(opt['cp_start'], opt['cp_end'], opt['max_it'], 0, iteration) 
        cg = interpolation(opt['cg_start'], opt['cg_end'], opt['max_it'], 0, iteration) 
        
        rp = np.random.random()
        rg = np.random.random()
        
        cognitive = np.multiply(cp * rp, np.subtract(self.peronal_best, self.position))
        social = np.multiply(cg * rg, np.subtract(swarm_best_pos, self.position))
        v = np.add(np.multiply(w, self.velocity), np.add(cognitive, social))
        self.velocity = v.tolist()
        
        p = np.add(self.position, self.velocity)
        self.peronal_best = p.tolist()
    
def PSO(func, opt = options):
    swarm = []
    swarm_best = None
    swarm_best_pos = []
    
    for i in range(opt['particle_num']):
        swarm.append(Particle(list(np.random.uniform(-10, 10, 60))))
    
    i = 0
    while i < opt['max_it']:
        for particle in swarm:
            particle.evalute(func)
            
            if swarm_best is None or swarm_best > particle.feval_best:
                swarm_best = particle.feval_best
                swarm_best_pos = particle.peronal_best[:]
            
        for particle in swarm:
            particle.update_data(swarm_best_pos, i, opt)
            
        i += 1
            
    
    return swarm_best_pos, swarm_best
        
def interpolation(start, end, max_it, min_it, curr_it):
    return start + ((end - start) / (max_it - min_it)) * (max_it - curr_it);