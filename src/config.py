# types
COOPERATE = 0
DEFECT = 1

MEMORY_DEPTH = 3
INIT_LENGTH = int(2*MEMORY_DEPTH)
STRATEGY_LENGTH = int(4**MEMORY_DEPTH) + INIT_LENGTH

# payoff matrix
PAYOFF = {
    (COOPERATE,COOPERATE):(3,3),
    (DEFECT,COOPERATE):(5, 0),
    (COOPERATE,DEFECT):(0, 5),
    (DEFECT, DEFECT):(1,1)
}

ITERATIONS = 100

# parameters specific for genetic algorithm
MUTATION_RATE = 0.001
CROSSOVER_RATE = 0.5
POPULATION_SIZE = 100
GENERATIONS =100
ROULETTE_SELECTION=False # if false, top-k selection is used
SELECTION_SIZE = 10

# parameters for hill climbing
ROUNDS = 3 # for tournament scoring

# parameters for tabu search
TABU_SIZE = 5