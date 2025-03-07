from config import *
from strategies.player import Player

# returns a tuple of the score of the two players
# in the form (p1_score, p2_score)
def calculate_score(p1_move: int, p2_move: int):
    return PAYOFF[(p1_move, p2_move)]

def match(player_1: Player, player_2: Player):
    for i in range(ROUNDS):
        move_1 = player_1.next_move(player_2.mem)
        move_2 = player_2.next_move(player_1.mem)
        score = calculate_score(move_1, move_2)

        player_1.add_score(score[0])
        player_2.add_score(score[1])
        player_1.add_memory(move_1)
        player_2.add_memory(move_2)

def tournament(players: list[Player]):
    # tournament_scores[i] is the tournament score of players[i]
    tournament_scores = []
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            match(players[i], players[j])
            tournament_scores[i] += players[i].score
            tournament_scores[j] += players[j].score
            players[i].reset()
            players[j].reset()
    return tournament_scores