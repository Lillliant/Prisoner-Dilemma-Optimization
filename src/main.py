from config import *
from tournament.player import Player
from tournament.util import *
from optimization.hill import *
from optimization.tabu import *

# this is test code, not main program
p1 = Player(type='ENCODED', encoded_strategy=generate_random_strategy(STRATEGY_LENGTH))
print(p1.get_mem_string())
print(p1.get_strategy_string())

optimized_strategy = hill_climbing()

# 1. Find the optimized strategies
# 2. Run the tournament with the optimized strategies and the original strategies
# 3. Print the results
# 4. Save the results to a file
# 5. Print the file name
# 6. Print the time taken and other parameters

# 1. Find the optimized strategies for all optimization method
# 2. Run the tournament with the optimized strategies and the original strategies