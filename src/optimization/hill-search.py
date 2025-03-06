# How to structure prisoner's dilemma as a search problem?
from config import *

# General idea of hill climbing from geekforgeek
'''
def hill_climbing(f, x0):
    x = x0 # initial solution
    while True:
        neighbors = generate_neighbors(x) # generate neighbors of x
        # find the neighbor with the highest function value
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x): # if the best neighbor is not better than x, stop
            return x
        x = best_neighbor # otherwise, continue with the best neighbor
'''
# this generates neighbors of the state x
#def generate_neighbors():