import random
from tournament.strategies import TFT, ALLC, ALLD, RAND  
from config import COOPERATE, DEFECT, MEMORY_DEPTH  

class PrisonersDilemmaSimulator:
    def __init__(self, strategy1, strategy2, rounds=10):
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.rounds = rounds
        self.scores = {1: 0, 2: 0}  # Tracking scores
        self.memory = {1: [], 2: []}  # Tracking moves history

    def play_round(self, round_num):
        # Player 1 and Player 2 make decisions based on their strategies
        if self.strategy1 == TFT:
            move1 = self.strategy1(self.memory[1], self.memory[2])  # TFT uses opponent's history
        elif self.strategy1 == ALLD or self.strategy1 == ALLC or self.strategy1 == RAND:
            move1 = self.strategy1()  # No memory needed for naive strategies
        else:
            move1 = self.strategy1(self.memory[2], self.memory[1])  # Player 1 uses Player 2's history (opponent's moves)

        if self.strategy2 == TFT:
            move2 = self.strategy2(self.memory[2], self.memory[1])  # TFT uses Player 1's history
        elif self.strategy2 == ALLD or self.strategy2 == ALLC or self.strategy2 == RAND:
            move2 = self.strategy2()  # No memory needed for naive strategies
        else:
            move2 = self.strategy2(self.memory[1], self.memory[2])  # Player 2 uses Player 1's history

        # Assign scores based on the IPD matrix
        if move1 == COOPERATE and move2 == COOPERATE:
            score1, score2 = 3, 3
        elif move1 == COOPERATE and move2 == DEFECT:
            score1, score2 = 0, 5
        elif move1 == DEFECT and move2 == COOPERATE:
            score1, score2 = 5, 0
        else:  # Both Defect
            score1, score2 = 1, 1

        # Update scores and memory
        self.scores[1] += score1
        self.scores[2] += score2
        self.memory[1].append(move1)
        self.memory[2].append(move2)

        # Print round results
        print(f"Round {round_num}: Player 1 ({move1}), Player 2 ({move2})")
        print("+------------+----------------+--------------+")
        print("| Player     | Round Score    | Total Score  |")
        print("+------------+----------------+--------------+")
        print(f"| Player 1   | {score1:^14} | {self.scores[1]:^12} |")
        print(f"| Player 2   | {score2:^14} | {self.scores[2]:^12} |")
        print("+------------+----------------+--------------+\n")

    def run_simulation(self):
        print(f"\nStarting Simulation: {self.strategy1.__name__} vs {self.strategy2.__name__}")
        for round_num in range(1, self.rounds + 1):
            self.play_round(round_num)
        
        print("Final Scores:")
        print("+------------+--------------+")
        print("| Player     | Total Score  |")
        print("+------------+--------------+")
        print(f"| Player 1   | {self.scores[1]:^12} |")
        print(f"| Player 2   | {self.scores[2]:^12} |")
        print("+------------+--------------+")

# Run the simulation with chosen strategies
if __name__ == "__main__":
    simulator = PrisonersDilemmaSimulator(TFT, ALLD, rounds=5)
    simulator.run_simulation()
