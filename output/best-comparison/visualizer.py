from matplotlib import pyplot as plt
import numpy as np

# Data as obtained from the data folder
# memory depth is set at 3
data = {
    'ALLC': (0, 11, 9, 4359),
    'ALLD': (17, 3, 0, 3780),
    'APAVLOV': (0, 14, 6, 5035),
    'EXT_ZD': (13, 4, 3, 3254),
    'GENETIC_D1': (1, 11, 8, 4807),
    'GENETIC_D2': (1, 11, 8, 4806),
    'GENETIC_S': (1, 11, 8, 4630),
    'GENETIC_W': (13, 4, 3, 3834),
    'GEN_ZD': (14, 3, 3, 3709),
    'GRIM': (2, 14, 4, 4587),
    'GTFT': (3, 12, 5, 4879),
    'HILL_CLIMBING': (9, 4, 7, 4248),
    'PAVLOV': (0, 11, 9, 4492),
    'RAND': (9, 2, 9, 3982),
    'STFT': (9, 11, 0, 4049),
    'TABU_SD': (7, 4, 9, 4917),
    'TABU_W': (10, 7, 3, 4759),
    'TF2T': (0, 11, 9, 4736),
    'TFT': (0, 14, 6, 5008)
}

# visualize the win count per strategy
def visualize_win(data: dict):
    plt.figure(layout="constrained")
    strategy = list(data.keys())
    wins = [scores[0] for scores in data.values()]
    plt.bar(strategy, wins)
    plt.xlabel("Strategy")
    plt.xticks(strategy, rotation=-90)
    plt.ylabel("Wins")
    plt.title("Wins by Strategy")
    plt.savefig(f'mem3-wincount.png')
    plt.close()

def visualize_score(data: dict):
    plt.figure(layout="constrained")
    strategy = list(data.keys())
    scores = [scores[3] for scores in data.values()]
    plt.bar(strategy, scores)
    #score_ratio = [score - max(cumulative_score) for score in cumulative_score]
    plt.bar(strategy, scores)
    plt.xlabel("Strategy")
    plt.xticks(strategy, rotation=-90)
    plt.ylabel("Cumulative Score")
    plt.title("Cumulative Score by Strategy")
    #plt.show()
    plt.savefig(f'm3-score-count.png')
    plt.close()

def visualize_score_deviation(data: dict):
    plt.figure(layout="constrained")
    strategy = list(data.keys())
    scores = [scores[3] for scores in data.values()]
    #plt.bar(strategy, scores)
    score_ratio = [score - max(scores) for score in scores]
    plt.bar(strategy, score_ratio)
    plt.xlabel("Strategy")
    plt.xticks(strategy, rotation=-90)
    plt.ylabel("Deviation from Max Score")
    plt.title("Deviation from Max Score by Strategy")
    #plt.show()
    plt.savefig(f'm3-score-deviation v2.png')
    plt.close()

if __name__ == "__main__":
    visualize_win(data)
    visualize_score(data)
    visualize_score_deviation(data)