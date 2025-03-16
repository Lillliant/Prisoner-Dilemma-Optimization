import random
from config import *
import itertools
from tournament.player import Player

# naive strategies: RAND, ALLC, ALLD
def RAND():
    return random.randint(min(COOPERATE, DEFECT), max(COOPERATE, DEFECT))

def ALLC():
    return COOPERATE

def ALLD():
    return DEFECT

# classic strategies: TFT, TF2T, STFT
def TFT(player_mem: list[int], opponent_mem: list[int]):
    if (len(opponent_mem) == 0):
        return COOPERATE
    return opponent_mem[-1] # there is at least one elements

def TF2T(player_mem: list[int], opponent_mem: list[int]):
    if (len(opponent_mem) < 2):
        return COOPERATE
    elif (opponent_mem[-1] == DEFECT and opponent_mem[-2] == DEFECT):
        return DEFECT
    else:
        return COOPERATE

def STFT(player_mem: list[int], opponent_mem: list[int]):
    if (len(opponent_mem) == 0):
        return DEFECT
    return opponent_mem[-1]

# more strategies for comparison: GRIM, Pavlov, Adaptive Pavlov, GTFT (modified after Gradual), Extortionary ZD, Generous ZD

# this is the forgetful implementation of GRIM
def GRIM(opponent_mem: list[int]):
    if (DEFECT in opponent_mem[-MEMORY_DEPTH:]):
        return DEFECT
    return COOPERATE

def PAVLOV(player_mem: list[int], opponent_mem: list[int]):
    if (len(opponent_mem) == 0):
        return COOPERATE
    if (player_mem[-1] == opponent_mem[-1]):
        return COOPERATE
    return DEFECT

# for memory depth less than 6, Adaptive Pavlov is equivalent to TFT
def ADAPTIVE_PAVLOV(player_mem: list[int], opponent_mem: list[int]):
    if len(opponent_mem) < 6 or MEMORY_DEPTH < 6:
        return TFT(player_mem, opponent_mem)
    else:
        if (DEFECT not in opponent_mem[-6:]): # classify opponent as cooperator
            return COOPERATE
        elif (opponent_mem[-6:].count(DEFECT) >= 4): # classify opponent as defector
            return DEFECT
        elif (opponent_mem[-6:].count(DEFECT) == 3): # classify opponent as STFT
            if (DEFECT in opponent_mem[-2:]):
                return DEFECT
            else:
                return COOPERATE
        else: # defect < 3 times, classify opponent as Random
            return DEFECT

# keeps track of total number of betrayals and defect accordingly
def GTFT(player_mem: list[int], opponent_mem: list[int], punishment_count: int, reward_count: int):
    if (len(opponent_mem) == 0):
        return COOPERATE, 0, 0
    elif(punishment_count > 0):
        return DEFECT, punishment_count-1, reward_count
    elif(reward_count > 0):
        return COOPERATE, punishment_count, reward_count-1
    else: # both punishment and reward count are 0, but not in first round
        if (DEFECT in opponent_mem[-MEMORY_DEPTH:]):
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
        return random.choices([COOPERATE, DEFECT], weights=[0.875, 0.125], k=1)[0]
    elif (player_mem[-1] == COOPERATE and opponent_mem[-1] == DEFECT):
        return random.choices([COOPERATE, DEFECT], weights=[0.4375, 0.5625], k=1)[0]
    elif (player_mem[-1] == DEFECT and opponent_mem[-1] == COOPERATE):
        return random.choices([COOPERATE, DEFECT], weights=[0.375, 0.625], k=1)[0]
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
        return random.choices([COOPERATE, DEFECT], weights=[0.5625, 0.4375], k=1)[0]
    elif (player_mem[-1] == COOPERATE and opponent_mem[-1] == DEFECT):
        return random.choices([COOPERATE, DEFECT], weights=[0.5, 0.5], k=1)[0]
    elif (player_mem[-1] == DEFECT and opponent_mem[-1] == COOPERATE):
        return random.choices([COOPERATE, DEFECT], weights=[0.125, 0.875], k=1)[0]
    else:
        return DEFECT

# encoded strategy
def ENCODED(encoded_strategy: list[int], player_mem: list[int], opponent_mem: list[int]):
    move_idx = mem_to_idx(player_mem[-MEMORY_DEPTH:], opponent_mem[-MEMORY_DEPTH:])
    return encoded_strategy[move_idx]

# generate a randomized strategy
def generate_random_strategy(length: int):
    # random bit for each position of the strategy
    random_strategy = [random.randint(min(COOPERATE, DEFECT), max(COOPERATE, DEFECT)) for i in range(length)]
    return random_strategy 

# generate a list of distinct strategies based on the given length
def generate_unique_strategies(length: int):
    # itertools.product generates all possible combinations of the given elements
    strategies = [list(s) for s in itertools.product([COOPERATE, DEFECT], repeat=length)]
    return strategies

def mem_to_idx(player_mem: list[int], opponent_mem: list[int]):
    bin_code = []
    for bit_1, bit_2 in zip(player_mem, opponent_mem):
        bin_code.append(bit_1)
        bin_code.append(bit_2)
    index = int("".join(map(str, bin_code)), 2)
    print(index)
    return int("".join(map(str, bin_code)), 2)

# Generate an encoding string based on the specific human designed strategy
# Not suitable for GTFT as its actions are also based on the count of retaliation and reward
def generate_encoding(player: Player):
    encoded_strategy = []
    premise_move = player.next_move([]) # initial move
    for i in range(STRATEGY_LENGTH - INIT_LENGTH):
        binary_code = bin(i)[2:].zfill(INIT_LENGTH)
        opponent_mem = []
        for i, move in enumerate(binary_code): # separate player and opponent history
            if i % 2 == 0:
                player.add_memory(int(move))
            else:
                opponent_mem.append(int(move))
        move = player.next_move(opponent_mem) # determine next action accordingly
        encoded_strategy.append(move)
    premise_binary = bin(encoded_strategy.index(premise_move))[2:].zfill(INIT_LENGTH)
    encoded_strategy += [int(bit) for bit in premise_binary] # add premise bits to encoding
    return encoded_strategy