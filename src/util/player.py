from config import *
from strategies.classic import *
from strategies.naive import *

def next_move(strat: str, opp_mem: list[int]):
    match strat:
        case 'tft':
            return TFT(opp_mem)
        case 'tf2t':
            return TF2T(opp_mem)
        case 'stft':
            return STFT(opp_mem)
        case 'rand':
            return RAND(opp_mem)
        case 'allc':
            return ALLC(opp_mem)
        case 'alld':
            return ALLD(opp_mem)
        
def play_match(strat_1: str, strat_2: str):
    mem_1 = []
    mem_2 = []
    score_1 = 0
    score_2 = 0
    for i in range(ITERATION):
        mem_1.append(next_move(strat_1, mem_2)) 
        mem_2.append(next_move(strat_2, mem_1))
        score = calculate_score(mem_1[-1], mem_2[-1])
        score_1 += score[0]
        score_2 += score[1]
    return mem_1, score_1, mem_2, score_2

def calculate_score(p1_move: int, p2_move: int):
    return PAYOFF[(p1_move, p2_move)]