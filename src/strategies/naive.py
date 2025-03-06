import random
from config import COOPERATE, DEFECT

# TODO: modify the code such that 0 and 1 are returned with a given probability distribution
def RAND(mem: list[int]):
    return random.randint(min(COOPERATE, DEFECT), max(COOPERATE, DEFECT))

def ALLC(mem: list[int]):
    return COOPERATE

def ALLD(mem: list[int]):
    return DEFECT