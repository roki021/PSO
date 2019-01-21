from optimization.ann_criterion import optimality_criterion
from optimization.PSO import PSO, options
from time import time
    

if __name__ == '__main__':
    opt = dict(options)
    opt['particle_num'] = 30
    opt['max_it'] = 100
    
    f = open("log1.txt", "w")
    num_exec = 5
    time_diff_list = [0] * num_exec
    val_list = [0] * num_exec
    pos_list = [None] * num_exec
    
    for i in range(num_exec):
        start = time()
        pos, val = PSO(optimality_criterion, opt)
        time_diff = time() - start
        time_diff_list[i] = time_diff
        val_list[i] = val
        pos_list[i] = pos
        
    min_index = val_list.index(min(val_list))
  
    f.write("Particle number: " + str(opt['particle_num']) + "\n")
    f.write("Max iteration: " + str(opt['max_it']) + "\n")
    f.write("Bounds: " + str(opt['bounds']) + "\n\n")
    f.write("Best position = [\n")
    for dim in pos_list[min_index]:
        f.write("\t" + str(dim) + "\n")
        
    f.write("]\n")
    
    f.write("Value of best position = " + str(val_list[min_index]) + "\n")
    f.write("Execution time: " + str(round(time_diff_list[min_index])) + " seconds\n")
    
    f.close()
    print("Finished...")
    