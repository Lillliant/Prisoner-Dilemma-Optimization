from config import *
from optimization.hill import hill_climbing
from optimization.tabu import tabu_search
from optimization.genetic import genetic
from tournament.tournament import tournament
from tournament.strategies import generate_encoding
from pprint import pprint
from tournament.player import Player

# MAIN PARAMETERS
USE_HILL_CLIMBING = False
USE_TABU_SEARCH = False
USE_GENETIC = False
human_strategy = ['ALLC', 'ALLD', 'RAND', 'TFT', 'TF2T', 'STFT', 'GTFT', 'PAVLOV', 'APAVLOV', 'GRIM', 'EXT_ZD', 'GEN_ZD']

# Get the list of strategies
strategies = []
for strategy in human_strategy:
    strategies.append((strategy, Player(strategy)))

if USE_HILL_CLIMBING:
    print("Hill Climbing")
    hill_climbing_strategy = hill_climbing()
    # hill_climbing_strategy = hill_climbing(opponent_strategy=generate_encoding('TFT'))
    strategies.append(('HILL_CLIMBING', Player('ENCODED', hill_climbing_strategy)))
    print("Hill Climbing Complete")
    print("optimized strategy: ", hill_climbing_strategy)

if USE_TABU_SEARCH:
    print("Tabu Search")
    tabu_search_strategy = tabu_search()
    strategies.append(('TABU_SEARCH', Player('ENCODED', tabu_search_strategy)))
    print("Tabu Search Complete")
    print("optimized strategy: ", tabu_search_strategy)

if USE_GENETIC:
    print("Genetic Algorithm")
    genetic_strategy = genetic()
    strategies.append(('GENETIC', Player('ENCODED', genetic_strategy)))
    print("Genetic Algorithms Complete")
    print("optimized strategy: ", genetic_strategy)

# Run the tournament with the optimized strategies and the original strategies
# (Win, Tie, Loss, Cumulative Score)
strategy_scores = {name: (0,0,0,0) for name, _ in strategies}
for i, (name_a, strategy_a) in enumerate(strategies):
    for name_b, strategy_b in strategies[i:]: # competes against itself, but avoid repeated matches
        players = [strategy_a, strategy_b]
        scores = tournament(players)
        #print(f"{name_a} vs {name_b}: {scores}")
        if (scores[0] < scores[1]): # strategy_b wins
            strategy_scores[name_b] = (strategy_scores[name_b][0] + 1, strategy_scores[name_b][1], strategy_scores[name_b][2], strategy_scores[name_b][3] + scores[1])
            strategy_scores[name_a] = (strategy_scores[name_a][0], strategy_scores[name_a][1], strategy_scores[name_a][2] + 1, strategy_scores[name_a][3] + scores[0])
        elif (scores[0] > scores[1]): # strategy_a wins
            strategy_scores[name_a] = (strategy_scores[name_a][0] + 1, strategy_scores[name_a][1], strategy_scores[name_a][2], strategy_scores[name_a][3] + scores[0])
            strategy_scores[name_b] = (strategy_scores[name_b][0], strategy_scores[name_b][1], strategy_scores[name_b][2] + 1, strategy_scores[name_b][3] + scores[1])
        else: # tie
            strategy_scores[name_a] = (strategy_scores[name_a][0], strategy_scores[name_a][1] + 1, strategy_scores[name_a][2], strategy_scores[name_a][3] + scores[0])
            strategy_scores[name_b] = (strategy_scores[name_b][0], strategy_scores[name_b][1] + 1, strategy_scores[name_b][2], strategy_scores[name_b][3] + scores[1])

pprint(strategy_scores)