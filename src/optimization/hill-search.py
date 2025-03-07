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

# return a list of neighbours of the current strategy.
# neighbours are defined to be strategies encodings 
# that differ from the current strategy by exactly one bit.
def generate_neighbours(strategy: list[int]):
    neighbours = []
    for i in range(len(strategy)):
        new_strategy = strategy.copy()
        new_strategy[i] = new_strategy[i] ^ 1 # flip the bits
        neighbours.append(new_strategy)
    return neighbours

def objective_function():