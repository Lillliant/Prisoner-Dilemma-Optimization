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

# Evaluate a strategy by playing against a fixed opponent
def evaluate_strategy(strategy, opponent_strategy, rounds=10):
    """ Simulate a game and compute total score """
    strategy_moves = binary_to_strategy(strategy)
    opponent_moves = binary_to_strategy(opponent_strategy)
    
    score = 0
    for i in range(rounds):
        my_move = strategy_moves[i % len(strategy_moves)]
        opp_move = opponent_moves[i % len(opponent_moves)]
        score += PAYOFF_MATRIX[(my_move, opp_move)][0]  # Player 1's score
    return score

# Genetic Algorithm
def genetic_algorithm(initial_strategy, opponent_strategy, max_iterations=20, population_size=5):
    """ Perform Genetic Algorithm to find an optimal strategy """
    strategy_length = len(initial_strategy)
    
    # Initialize population with initial strategy and random ones
    population = [initial_strategy] + [generate_random_strategy(strategy_length) 
                                       for _ in range(population_size - 1)]
    best_strategy = initial_strategy
    best_score = evaluate_strategy(best_strategy, opponent_strategy)
    
    for _ in range(max_iterations):
        # Evaluate all strategies in the population
        scores = [evaluate_strategy(ind, opponent_strategy) for ind in population]
        
        # Find best in current population
        current_best_idx = max(range(len(scores)), key=lambda i: scores[i])
        if scores[current_best_idx] > best_score:
            best_strategy = population[current_best_idx]
            best_score = scores[current_best_idx]
        
        # Selection: Keep top 2 strategies (elitism)
        sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        parents = [population[sorted_indices[0]], population[sorted_indices[1]]]
        
        # Crossover: Create new children (single-point crossover)
        new_population = parents.copy()
        crossover_point = random.randint(1, strategy_length - 1)
        child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
        child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
        
        # Mutation: Flip one random bit in each child
        for child in [child1, child2]:
            mutate_pos = random.randint(0, strategy_length - 1)
            child_list = list(child)
            child_list[mutate_pos] = '1' if child_list[mutate_pos] == '0' else '0'
            new_population.append(''.join(child_list))
        
        # Fill remaining population with random strategies
        while len(new_population) < population_size:
            new_population.append(generate_random_strategy(strategy_length))
        
        # Update population
        population = new_population
    
    return best_strategy, best_score

# Run Test Case: Optimize against Always Cooperate Strategy ('000000')
if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    
    initial_strategy = generate_random_strategy()
    opponent_strategy = '000000'  # Always Cooperate
    optimized_strategy, optimized_score = genetic_algorithm(initial_strategy, opponent_strategy)
    
    # Display Results
    print(f"Initial Strategy: {initial_strategy}")
    print(f"Optimized Strategy: {optimized_strategy}")
    print(f"Optimized Score: {optimized_score}")
