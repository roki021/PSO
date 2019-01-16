from optimization.ann_criterion import optimality_criterion
from optimization.PSO import PSO

if __name__ == '__main__':
    a = PSO(optimality_criterion)
    print(a[0], "\n", a[1])