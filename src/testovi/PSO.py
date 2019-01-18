from ann_criterion import optimality_criterion
import numpy as np 


# opcije algoritma
options = { 'max_it'       : 100,       # broj iteracija
            'particle_num' : 30,        # broj cestica
            'dim'          : 60,        # dimenzija
            'bounds'       : (-10, 10), # opseg nasumicnih pocetnih vrednosti za svaku dimenziju
            'cp_start'     : 2.5,       # startna vrednost kognitivnog faktora
            'cp_end'       : 0.5,       # finalna vrednost kognitivnog faktora
            'cg_start'     : 0.5,       # startna vrednost socijalnog faktora
            'cg_end'       : 2.5,       # finalna vrednost socijalna faktora 
            'w_start'      : 0.9,       # startna vrednost inercijalnog faktora
            'w_end'        : 0.4 }      # finalna vrednost inercijalnog faktora


class Particle(object):
    """
        Klasa predstavlja jednu cesticu roja
        Sadrzi sve potrebne atribute vezane za cesticu
    """
    
    def __init__(self, w):
        self.position = np.copy(w)
        self.velocity = np.random.uniform(-1, 1, len(w))
        self.peronal_best = self.position
        self.feval = None
        self.feval_best = None
        
    def evalute(self, func):
        """
            Racuna vrednost trenutne pozicije tacke u prosledjenoj funkciji
        """
        self.feval = func(self.position)
        
        if self.feval_best is None or self.feval < self.feval_best:
            self.feval_best = self.feval
            self.peronal_best = np.copy(self.position)
            
    def update_data(self, swarm_best_pos, iteration, opt):
        """
            Azurira sve atribute za datu iteraciju
        """
        w = interpolation(opt['w_start'], opt['w_end'], opt['max_it'], 0, iteration)
        cp = interpolation(opt['cp_start'], opt['cp_end'], opt['max_it'], 0, iteration) 
        cg = interpolation(opt['cg_start'], opt['cg_end'], opt['max_it'], 0, iteration) 
        
        rp = np.random.random()
        rg = np.random.random()
        
        cognitive = np.multiply(cp * rp, np.subtract(self.peronal_best, self.position))
        social = np.multiply(cg * rg, np.subtract(swarm_best_pos, self.position))
        self.velocity = np.add(np.multiply(w, self.velocity), np.add(cognitive, social))
        
        self.peronal_best = np.add(self.position, self.velocity)
    
    
def PSO(func, opt = options):
    """
        Izvrsava algoritam optimizacije rojem cestica,
        Trazi minimum za prosledjenu funkciju
    """
    swarm = []
    swarm_best = None
    swarm_best_pos = np.full((opt['dim'], ), 0) 
    
    for i in range(opt['particle_num']):
        swarm.append(Particle(np.random.uniform(-10, 10, opt['dim'])))
    
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
        print(i)
            
    return np.array(swarm_best_pos), swarm_best
        
        
def interpolation(start, end, max_it, min_it, curr_it):
    """
        Interpolira izmenu za prosledjeni faktor
    """
    return start + ((end - start) / (max_it - min_it)) * (max_it - curr_it)