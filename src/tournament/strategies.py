import random
from config import COOPERATE, DEFECT, MEMORY_DEPTH
from util.util import mem_to_idx

# naive strategies: RAND, ALLC, ALLD
def RAND():
    return random.randint(min(COOPERATE, DEFECT), max(COOPERATE, DEFECT))

def ALLC():
    return COOPERATE

def ALLD():
    return DEFECT

# classic strategies: TFT, TF2T, STFT
def TFT(opponent_mem: list[int]):
    if (len(opponent_mem) == 0):
        return COOPERATE
    return opponent_mem[-1] # there is at least one elements

def TF2T(opponent_mem: list[int]):
    if (len(opponent_mem) < 2):
        return COOPERATE
    elif (opponent_mem[-1] == DEFECT and opponent_mem[-2] == DEFECT):
        return DEFECT
    else:
        return COOPERATE

def STFT(opponent_mem: list[int]):
    if (len(opponent_mem) == 0):
        return DEFECT
    return opponent_mem[-1]

# TODO: implement the other 6 strategies

# encoded strategy
def ENCODED(encoded_strategy: list[int], player_mem: list[int], opponent_mem: list[int]):
    move_idx = mem_to_idx(player_mem[-MEMORY_DEPTH], opponent_mem[-MEMORY_DEPTH])
    return encoded_strategy[move_idx]