import numpy as np
import random

# Define Prisoner's Dilemma Payoff Matrix
PAYOFF_MATRIX = {
    ('C', 'C'): (3, 3),  # Reward for mutual cooperation
    ('C', 'D'): (0, 5),  # Sucker's payoff and temptation to defect
    ('D', 'C'): (5, 0),  # Temptation and sucker's payoff (swapped)
    ('D', 'D'): (1, 1)   # Punishment for mutual defection
}

# Encode strategies as binary strings ('C' -> 0, 'D' -> 1)
def binary_to_strategy(binary_str):
    """ Convert binary string to strategy sequence ('C' or 'D') """
    return ['C' if bit == '0' else 'D' for bit in binary_str]

# Generate initial random strategy
def generate_random_strategy(length=6):
    """ Create a random strategy with given length """
    return ''.join(random.choice('01') for _ in range(length))

# Evaluate a strategy by playing against a fixed opponent (e.g., Always Cooperate '000000')
def evaluate_strategy(strategy, opponent_strategy, rounds=10):
    """ Simulate a game and compute total score """
    strategy_moves = binary_to_strategy(strategy)
    opponent_moves = binary_to_strategy(opponent_strategy)
    
    score = 0
    for i in range(rounds):
        my_move = strategy_moves[i % len(strategy_moves)]
        opp_move = opponent_moves[i % len(opponent_moves)]
        score += PAYOFF_MATRIX[(my_move, opp_move)][0]  # Take first player's score
    return score

# Generate neighborhood (flip one bit at a time)
def generate_neighbors(strategy):
    """ Generate neighboring strategies by flipping each bit """
    neighbors = []
    for i in range(len(strategy)):
        new_strategy = list(strategy)
        new_strategy[i] = '1' if strategy[i] == '0' else '0'  # Flip bit
        neighbors.append(''.join(new_strategy))
    return neighbors

# Tabu Search Algorithm
def tabu_search(initial_strategy, opponent_strategy, max_iterations=20, tabu_size=5):
    """ Perform Tabu Search to find an optimal strategy """
    current_strategy = initial_strategy
    best_strategy = current_strategy
    best_score = evaluate_strategy(current_strategy, opponent_strategy)
    
    tabu_list = []
    
    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_strategy)
        best_neighbor = None
        best_neighbor_score = float('-inf')
        
        for neighbor in neighbors:
            if neighbor not in tabu_list:  # Avoid revisiting solutions
                score = evaluate_strategy(neighbor, opponent_strategy)
                if score > best_neighbor_score:
                    best_neighbor = neighbor
                    best_neighbor_score = score
        
        if best_neighbor is None:  # No valid move found, stop
            break
        
        current_strategy = best_neighbor
        tabu_list.append(current_strategy)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)  # Maintain tabu list size

        # Update best strategy found
        if best_neighbor_score > best_score:
            best_strategy = best_neighbor
            best_score = best_neighbor_score

    return best_strategy, best_score

# Run Test Case: Optimize against Always Cooperate Strategy ('000000')
initial_strategy = generate_random_strategy()
optimized_strategy, optimized_score = tabu_search(initial_strategy, '000000')

# Display Results
print(f"Initial Strategy: {initial_strategy}")
print(f"Optimized Strategy: {optimized_strategy}")
print(f"Optimized Score: {optimized_score}")
