# types
COOPERATE = 0
DEFECT = 1

MEMORY_DEPTH = 3
STRATEGY_LENGTH = int(4**MEMORY_DEPTH) + int(2*MEMORY_DEPTH)
ITERATION = 1000

# payoff matrix
PAYOFF = {
    (COOPERATE,COOPERATE):(3,3),
    (DEFECT,COOPERATE):(5, 0),
    (COOPERATE,DEFECT):(0, 5),
    (DEFECT, DEFECT):(1,1)
}

# parameters specific for genetic algorithm
MUTATION_RATE=0.001
POPULATION_SIZE=100

# parameters for hill climbing

# parameters for tabu search