# How to structure prisoner's dilemma as a search problem?
from config import *
from tournament.strategies import generate_random_strategy
from tournament.player import Player
from tournament.tournament import tournament

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

# define the objective function to be the cumulative score
# of the current strategy against all the other strategies
# in a round-robin tournament.
def objective_function(strategies: list[list[int]], opponent: list[int]):
    players = []
    for s in strategies:
        players.append(Player('ENCODED', s))
    if opponent is not None:
        opponent_player = Player('ENCODED', opponent)
        tournament_scores = []
        for p in players:
            tournament_scores.append(tournament([p, opponent_player]))
        print("Maximum score: ", max(tournament_scores))
        return [t[0] for t in tournament_scores]
    else:
        return tournament(players) # returns a list where tournament_scores[i] is the tournament score of strategies[i]
    
# hill climbing method
# randomly generate a initial state if none is given
# if stuck in iterations, return the current state after configured iteration
def hill_climbing(initial_strategy: list[int] = None, opponent_strategy: list[int] = None):
    if initial_strategy is None: initial_strategy = generate_random_strategy(STRATEGY_LENGTH)
    current_strategy = initial_strategy
    for i in range(ITERATIONS):
        print("Iteration ", i)
        neighbours = generate_neighbours(current_strategy)
        all_strategies = neighbours
        all_strategies.append(current_strategy)
        all_strategies_scores = objective_function(all_strategies, opponent_strategy)

        current_strategy_score = all_strategies_scores[-1]
        best_neighbour_score = max(all_strategies_scores[:-1])
        best_neighbour = neighbours[all_strategies_scores.index(best_neighbour_score)]
        if i % 1 == 0:
            print("Current strategy: ", current_strategy, current_strategy_score)
            print("Best neighbour: ", best_neighbour, best_neighbour_score)

        if best_neighbour_score < current_strategy_score:
            print("Current strategy (maxima): ", current_strategy, current_strategy_score)
            print("Best neighbour (maxima): ", best_neighbour, best_neighbour_score)
            return current_strategy
        current_strategy = best_neighbour
        
    return current_strategy