import random
from config import *
from tournament.player import Player
from tournament.util import generate_random_strategy
from tournament.tournament import tournament


# randomly flip a bit in the strategy given a set mutation rate in config.py
def mutate(strategy: list[int]):
    new_strategy = list(strategy)
    for i in range(len(new_strategy)):
        mutate = random.choices([True, False], p=[MUTATION_RATE, 1 - MUTATION_RATE])
        if mutate:
            new_strategy[i] = new_strategy[i] ^ 1
    return new_strategy

# given a random k population, reproduce them to get a new population of size POPULATION_SIZE
def reproduce_population(selected_population: list[list[int]]):
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        parent_1 = random.choice(selected_population)
        idx = selected_population.index(parent_1)
        parent_2 = random.choice(selected_population[:idx] + selected_population[idx+1:]) # ensure unique parents

        crossover = random.choices([True, False], p=[CROSSOVER_RATE, 1 - CROSSOVER_RATE])
        if not crossover:
            child_1 = parent_1
            child_2 = parent_2
        else:
            child_1, child2 = crossover(parent_1, parent_2)
        
        # mutate the children based on given mutation rate
        child_1 = mutate(child_1)
        child_2 = mutate(child_2)

        # keep returned population size consistent to be at POPULATION_SIZE
        if child_1 not in new_population and len(new_population) < POPULATION_SIZE:
            new_population.append(child_1)
        if child_2 not in new_population and len(new_population) < POPULATION_SIZE:
            new_population.append(child_2)
    return new_population

# Combine two strategies at a random point (e.g., '010' and '111' produces '011' if split at the 2nd bit)
def crossover(parent1: list[int], parent2: list[int]):
    split = random.randint(1, len(parent1) - 1)
    new_strategy = parent1[:split] + parent2[split:]
    assert len(new_strategy) == len(parent1)
    return new_strategy

# selection can be based on the top-k scores, or random roulette
# customizable based on config.py
def selection_function(population: list[list[int]], population_score: list[int]):
    if ROULETTE_SELECTION:
        selected_population = random.choices[population, population_score, SELECTION_SIZE]
    else:
        sorted_score = sorted(population_score, reverse=True)
        selected_population = []
        for score in sorted_score[:SELECTION_SIZE]:
            selected_population.append(population[population_score.index(score)])
    return selected_population

# same as objective function in hill climbing
def fitness_function(strategies: list[list[int]]):
    players = []
    for s in strategies:
        players.append(Player('ENCODED', s))
    return tournament(players) # returns a list where tournament_scores[i] is the tournament score of strategies[i]

# generate the population of strategies
# with no specified population 
def generate_population():
    population = []
    while len(population) < POPULATION_SIZE:
        random_strategy = generate_random_strategy(STRATEGY_LENGTH)
        if random_strategy not in population:
            population.append(random_strategy)
    return population
    
# allows two optimization comparisons:
# 1. returns the best strategy against a particular opponent
# 2. returns the best strategy against its random populations
def genetic(population: list[list[int]] = None, opponent: list[int] = None):
    if population is None: population = generate_population()

    # For optimizing against a particular opponent
    if opponent is not None:
        population_score = []
        for i in range(population):
            population_score[i] = tournament([Player('ENCODED', population[i]), Player('ENCODED', opponent)])
            selected_population = selection_function(population, population_score)
            population = reproduce_population(selected_population)
    else: # for optimizing against a random population
        for _ in range(GENERATIONS):
            population_score = fitness_function(population)
            selected_population = selection_function(population, population_score)
            population = reproduce_population(selected_population)
    
    # return the best strategy based on the final population
    return population[population_score.index(max(population_score))]
