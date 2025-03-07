from config import *
from tournament.player import Player
from tournament.util import *

p1 = Player(type='ENCODED', encoded_strategy=generate_random_strategy(STRATEGY_LENGTH))
print(p1.get_mem_string())
print(p1.get_strategy_string())