from testovi.ann_criterion import optimality_criterion
from testovi.PSO import PSO, options
    

if __name__ == '__main__':
    opt = dict(options)
    opt['particle_num'] = 100
    opt['max_it'] = 100
    opt['bounds'] = (-100, -95)
    step = 5
    i = 1
    
    while opt['bounds'][1] <= 100:
        pos, val = PSO(optimality_criterion, opt)
        f = open("local_optim/log" + str(i) + ".txt", "w")
        f.write("Particle number: " + str(opt['particle_num']) + "\n")
        f.write("Max iteration: " + str(opt['max_it']) + "\n")
        f.write("Bounds: " + str(opt['bounds']) + "\n\n")
        f.write("Best position = [\n")
        for dim in pos:
            f.write("\t" + str(dim) + "\n")
            
        f.write("]\n")
        
        f.write("Value of best position = " + str(val) + "\n")
        
        f.close()
        opt['bounds'] = (opt['bounds'][0] + step, opt['bounds'][1] + step)
        i = i + 1;
        print("Finished " + str(i) + ". test")
        
    
    print("Finished all")
    