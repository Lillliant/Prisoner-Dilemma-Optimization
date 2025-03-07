import random
import strategies
from config import COOPERATE, DEFECT, MEMORY_DEPTH, INIT_LENGTH

class Player:
    def __init__(self, type: str, encoded_strategy: list[int] = []):
        # initialize variables
        self.type = type
        self.mem: list[int] = [] # memory of play history
        self.encoded_strategy = encoded_strategy # if the player is based on an encoded strategy
        self.score: int = 0

        # additional fields based on type
        if (type == 'GTFT'):
            self.punishment_count = 0
            self.reward_count = 0
            self.num_betrayals = 0

    def get_mem_string(self):
        return "".join(map(str, self.mem))
    
    def init_encoded_mem(self):
        self.mem = self.encoded_strategy[-INIT_LENGTH::2]
    
    def get_strategy_string(self):
        return "".join(map(str, self.encoded_strategy))
    
    def add_score(self, score: int):
        self.score += score

    def add_memory(self, move: int):
        self.mem.append(move)

    def reset(self):
        self.score = 0
        self.mem = []

    def next_move(self, opponent_mem: list[int]):
        match self.type:
            case 'ENCODED':
                if len(self.mem) == 0:
                    self.init_encoded_mem()
                    move_idx = int("".join(map(str, self.mem[-INIT_LENGTH])), 2)
                    return self.encoded_strategy[move_idx]
                else:
                    return strategies.ENCODED(self.encoded_strategy, self.mem, opponent_mem)
            case 'RAND':
                return strategies.RAND()
            case 'ALLC':
                return strategies.ALLC()
            case 'ALLD':
                return strategies.ALLD()
            case 'TFT':
                return strategies.TFT(self.mem)
            case 'TF2T':
                return strategies.TF2T(self.mem)
            case 'STFT':
                return strategies.STFT(self.mem)
            case 'GTFT':
                move, punishment_count, reward_count = strategies.GTFT(self, opponent_mem, self.punishment_count, self.reward_count)
                self.punishment_count = punishment_count
                self.reward_count = reward_count
                return move
            case _:
                raise NotImplementedError
    