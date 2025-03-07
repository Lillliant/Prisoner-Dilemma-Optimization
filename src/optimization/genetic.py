#Optimized Genetic Algorithm

import random
import numpy as np
# Define the Prisoner's Dilemma payoff matrix
PAYOFFS = {
    ('C', 'C'): (3, 3),  # Both cooperate: 3 points each
    ('C', 'D'): (0, 5),  # I cooperate, they defect: 0 for me, 5 for them
    ('D', 'C'): (5, 0),  # I defect, they cooperate: 5 for me, 0 for them
    ('D', 'D'): (1, 1)   # Both defect: 1 point each
}

# Turn a binary string into moves (C or D)
def decode_strategy(binary):
    """ 
    Change a string like '010' into moves ['C', 'D', 'C']
    '0' is Cooperate (C), '1' is Defect (D)
    """
    return ['C' if bit == '0' else 'D' for bit in binary]

# Make a random starting strategy
def make_random_strategy(length=5):
    """ 
    Create a random strategy like '01011'
    Each spot is randomly '0' or '1'
    """
    return ''.join(random.choice('01') for _ in range(length))

# Calculate my score against the opponent
def get_score(my_strategy, opponent_strategy, rounds=10):
    """ 
    Play my strategy vs the opponent for 10 rounds and get my score
    Repeats the strategy if it’s shorter than 10 rounds
    """
    my_moves = decode_strategy(my_strategy)
    opp_moves = decode_strategy(opponent_strategy)
    my_score = 0
    
    for i in range(rounds):
        my_move = my_moves[i % len(my_moves)]  # Loop my moves
        opp_move = opp_moves[i % len(opp_moves)]  # Loop opponent’s moves
        my_score += PAYOFFS[(my_move, opp_move)][0]  # Add my points
    return my_score

# Mix two strategies to create a new one
def mix_strategies(parent1, parent2):
    """ 
    Combine two strategies at a random point
    Like '010' and '111' might make '011' if split at 2
    """
    split = random.randint(1, len(parent1) - 1)
    return parent1[:split] + parent2[split:]

# Change a strategy to favor defecting
def tweak_strategy(strategy):
    """ 
    Flip one random bit, but prefer turning '0' to '1' (defecting)
    Helps optimize against Always Cooperate
    """
    pos = random.randint(0, len(strategy) - 1)
    new_strategy = list(strategy)
    # If it’s '0', flip to '1' more often (80% chance), else flip '1' to '0' less often
    if new_strategy[pos] == '0' and random.random() < 0.8:
        new_strategy[pos] = '1'
    elif new_strategy[pos] == '1' and random.random() < 0.2:
        new_strategy[pos] = '0'
    return ''.join(new_strategy)

# My optimized Genetic Algorithm
def my_genetic_algorithm(start_strategy=None, group_size=4, steps=10):
    """ 
    My GA to find the best strategy against 'Always Cooperate'
    Tuned to favor defecting for max points
    """
    opponent = '00000'  # Always Cooperate opponent (all C’s)
    
    # Start with a random strategy if none given
    if start_strategy is None:
        start_strategy = make_random_strategy()
    
    # Build a group with my start strategy and random ones
    group = [start_strategy]
    for _ in range(group_size - 1):
        group.append(make_random_strategy(len(start_strategy)))
    
    best_strategy = start_strategy
    best_score = get_score(best_strategy, opponent)
    
    # Evolve the group over a few steps
    for step in range(steps):
        # Get scores for all strategies
        scores = [get_score(strategy, opponent) for strategy in group]
        
        # Check if we’ve beaten our best score
        top_score = max(scores)
        top_index = scores.index(top_score)
        if top_score > best_score:
            best_strategy = group[top_index]
            best_score = top_score
        
        # Sort and pick the top two strategies
        sorted_group = [x for _, x in sorted(zip(scores, group), reverse=True)]
        parent1 = sorted_group[0]  # Best
        parent2 = sorted_group[1]  # Second best
        
        # Make new strategies by mixing
        new1 = mix_strategies(parent1, parent2)
        new2 = mix_strategies(parent2, parent1)
        
        # Tweak them to lean towards defecting
        new1 = tweak_strategy(new1)
        new2 = tweak_strategy(new2)
        
        # New group: keep top two, add tweaked ones
        group = [parent1, parent2, new1, new2]
        
        # Show progress every few steps
        if step % 5 == 0:
            print(f"Step {step}: Best Score = {best_score}")

    return best_strategy, best_score

# Test my optimized GA
if __name__ == "__main__":
    random.seed(42)  # Keep results the same each time
    
    my_start = make_random_strategy()
    final_strategy, final_score = my_genetic_algorithm(my_start)
    
    print(f"\nMy Starting Strategy: {my_start} ({decode_strategy(my_start)})")
    print(f"My Best Strategy: {final_strategy} ({decode_strategy(final_strategy)})")
    print(f"My Best Score: {final_score}")
