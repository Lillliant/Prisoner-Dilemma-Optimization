from config import *
from strategies.player import Player
from util.util import *

p1 = Player(type='ENCODED', encoded_strategy=generate_random_strategy(STRATEGY_LENGTH))
print(p1.get_mem_string())
print(p1.get_strategy_string())