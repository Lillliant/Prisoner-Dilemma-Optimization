import random
from config import COOPERATE, DEFECT

# generate a randomized strategy
def generate_random_strategy(length: int):
    return [random.randint(min(COOPERATE, DEFECT), max(COOPERATE, DEFECT)) for i in range(length)]

# generate a **list** of distinct strategies based on the
# given length of a strategy
def generate_unique_strategies(length: int):
    strategies = []
    # TODO: implement the code (like generating truth table)
    return strategies