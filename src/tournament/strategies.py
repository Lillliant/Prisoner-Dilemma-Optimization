import random
from config import COOPERATE, DEFECT, MEMORY_DEPTH
from tournament.util import mem_to_idx

# naive strategies: RAND, ALLC, ALLD
def RAND():
    return random.randint(min(COOPERATE, DEFECT), max(COOPERATE, DEFECT))

def ALLC():
    return COOPERATE

def ALLD():
    return DEFECT

# classic strategies: TFT, TF2T, STFT
def TFT(player_mem: list[int], opponent_mem: list[int]):
    if (len(player_mem) == 0):
        return COOPERATE
    return opponent_mem[-1] # there is at least one elements

def TF2T(player_mem: list[int], opponent_mem: list[int]):
    if (len(player_mem) < 2):
        return COOPERATE
    elif (opponent_mem[-1] == DEFECT and opponent_mem[-2] == DEFECT):
        return DEFECT
    else:
        return COOPERATE

def STFT(player_mem: list[int], opponent_mem: list[int]):
    if (len(player_mem) == 0):
        return DEFECT
    return opponent_mem[-1]

# more strategies for comparison: GRIM, Pavlov, Adaptive Pavlov, GTFT (modified after Gradual), Extortionary ZD, Generous ZD

# this is the forgetful implementation of GRIM
def GRIM(opponent_mem: list[int]):
    if (DEFECT in opponent_mem[-MEMORY_DEPTH]):
        return DEFECT
    return COOPERATE

def PAVLOV(player_mem: list[int], opponent_mem: list[int]):
    if (len(player_mem) == 0):
        return COOPERATE
    if (player_mem[-1] == opponent_mem[-1]):
        return COOPERATE
    return DEFECT

# for memory depth less than 6, Adaptive Pavlov is equivalent to TFT
def ADAPTIVE_PAVLOV(player_mem: list[int], opponent_mem: list[int]):
    if len(player_mem) < 6 or MEMORY_DEPTH < 6:
        return TFT(opponent_mem)
    else:
        if (DEFECT not in opponent_mem[-6]): # classify opponent as cooperator
            return COOPERATE
        elif (opponent_mem[-6].count(DEFECT) >= 4): # classify opponent as defector
            return DEFECT
        elif (opponent_mem[-6].count(DEFECT) == 3): # classify opponent as STFT
            if (DEFECT in opponent_mem[-2]):
                return DEFECT
            else:
                return COOPERATE
        else: # defect < 3 times, classify opponent as Random
            return DEFECT

# keeps track of total number of betrayals and defect accordingly
def GTFT(player_mem: list[int], opponent_mem: list[int], punishment_count: int, reward_count: int):
    if (len(player_mem) == 0):
        return COOPERATE, 0, 0
    elif(punishment_count > 0):
        return DEFECT, punishment_count-1, reward_count
    elif(reward_count > 0):
        return COOPERATE, punishment_count, reward_count-1
    else: # both punishment and reward count are 0, but not in first round
        if (DEFECT in opponent_mem[-MEMORY_DEPTH]):
            return DEFECT, opponent_mem.count(DEFECT) - 1, 2
        return COOPERATE, 0, 0

# from stanford website of IPD strategies
# uses a modified variant of ZD strategy: initial step is to cooperate, then use ZD strategies
'''
EXT-ZD is Extort-2
Based on past outcome CC, CD, DC, DD, the strategy will cooperating with probability 7/8, 7/16, 3/8, 0 respectively.
'''
def EXT_ZD(player_mem: list[int], opponent_mem: list[int]):
    if (len(player_mem) == 0):
        return COOPERATE
    if (player_mem[-1] == COOPERATE and opponent_mem[-1] == COOPERATE):
        return random.choices([COOPERATE, DEFECT], weights=[0.875, 0.125])
    elif (player_mem[-1] == COOPERATE and opponent_mem[-1] == DEFECT):
        return random.choices([COOPERATE, DEFECT], weights=[0.4375, 0.5625])
    elif (player_mem[-1] == DEFECT and opponent_mem[-1] == COOPERATE):
        return random.choices([COOPERATE, DEFECT], weights=[0.375, 0.625])
    else:
        return DEFECT

'''
GEN-ZD is Generous-2
Based on past outcome CC, CD, DC, DD, the strategy will cooperating with probability 1, 9/16, 1/2, 1/8 respectively.
'''
def GEN_ZD(player_mem: list[int], opponent_mem: list[int]):
    if (len(player_mem) == 0):
        return COOPERATE
    if (player_mem[-1] == COOPERATE and opponent_mem[-1] == COOPERATE):
        return random.choices([COOPERATE, DEFECT], weights=[0.5625, 0.4375])
    elif (player_mem[-1] == COOPERATE and opponent_mem[-1] == DEFECT):
        return random.choices([COOPERATE, DEFECT], weights=[0.5, 0.5])
    elif (player_mem[-1] == DEFECT and opponent_mem[-1] == COOPERATE):
        return random.choices([COOPERATE, DEFECT], weights=[0.125, 0.875])
    else:
        return DEFECT

# encoded strategy
def ENCODED(encoded_strategy: list[int], player_mem: list[int], opponent_mem: list[int]):
    move_idx = mem_to_idx(player_mem[-MEMORY_DEPTH], opponent_mem[-MEMORY_DEPTH])
    return encoded_strategy[move_idx]