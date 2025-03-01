import random
from util.type import COOPERATE, DEFECT

# TODO: modify the code such that 0 and 1 are returned with a given probability distribution
def random():
    return random.randint(min(COOPERATE, DEFECT), max(COOPERATE, DEFECT))

def always_cooperate():
    return COOPERATE

def always_defect():
    return DEFECT