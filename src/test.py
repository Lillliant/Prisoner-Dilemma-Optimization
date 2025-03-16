# This file is used for testing different parts of the codebase
from config import *
from tournament.strategies import generate_encoding
from tournament.tournament import tournament
from tournament.player import Player
from optimization.hill import hill_climbing
from optimization.tabu import tabu_search
from optimization.genetic import genetic


# This should generate the same expected score as from the class PowerPoint slide
# (Except RAND-related encounters, as that is based on a sum of probability)
def test_tournament(strategies: list[str]):
    players = [(name, Player(name)) for name in strategies]
    tournament_scores = {name: [] for name, _ in players}
    print("| \t\t |"+ "".join(f" \t{name}\t |" for name, _ in players)+" \tAvg\t |") # print header
    for name_1, player_1 in players:
        for name_2, player_2 in players:
            scores = tournament([player_1, player_2])
            tournament_scores[name_1].append(scores[0])
        print(f"| \t{name_1}\t |" + "".join(f" \t{score}\t |" for score in tournament_scores[name_1]) + f"\t{sum(tournament_scores[name_1])/len(tournament_scores[name_1])}\t |") # print score 

# TODO: Test the main method

if __name__ == '__main__':
    strategies = ['ALLC', 'RAND', 'ALLD', 'TFT']
    #test_tournament(strategies)
    #print(hill_climbing([0 for _ in range(STRATEGY_LENGTH)], [1 for _ in range(STRATEGY_LENGTH)]))
    #encoding = generate_encoding(Player('TFT'))
    #print(encoding)
    #print(len(encoding))
