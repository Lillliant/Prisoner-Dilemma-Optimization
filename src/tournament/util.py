import random
from config import COOPERATE, DEFECT, MEMORY_DEPTH
import itertools

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
    return int("".join(map(str, bin_code)), 2)