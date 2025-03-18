from matplotlib import pyplot as plt
import numpy as np

init_strategy = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]

# optimized strategy as obtained from data folder
iter_100 = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
iter_500 = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
iter_1000 = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]

data = {
    100: {
        'ALLC': (0, 8, 6, 3261),
        'ALLD': (10, 4, 0, 2276),
        'APAVLOV': (0, 11, 3, 3451),
        'EXT_ZD': (9, 4, 1, 2278),
        'GEN_ZD': (9, 4, 1, 2394),
        'GRIM': (2, 9, 3, 3409),
        'GTFT': (2, 9, 3, 3526),
        'HILL_CLIMBING': (3, 6, 5, 2673),
        'PAVLOV': (0, 8, 6, 3205),
        'RAND': (4, 4, 6, 2802),
        'STFT': (4, 10, 0, 2397),
        'TF2T': (0, 8, 6, 3422),
        'TFT': (0, 11, 3, 3475)},
    500: {
        'ALLC': (0, 8, 6, 3210),
        'ALLD': (10, 4, 0, 2272),
        'APAVLOV': (0, 10, 4, 3466),
        'EXT_ZD': (8, 4, 2, 2324),
        'GEN_ZD': (10, 3, 1, 2397),
        'GRIM': (2, 10, 2, 3387),
        'GTFT': (2, 9, 3, 3419),
        'HILL_CLIMBING': (3, 6, 5, 2690),
        'PAVLOV': (0, 8, 6, 3277),
        'RAND': (6, 3, 5, 2891),
        'STFT': (3, 11, 0, 2415),
        'TF2T': (0, 8, 6, 3373),
        'TFT': (0, 10, 4, 3473)},
    1000: {
        'ALLC': (0, 8, 6, 3249),
        'ALLD': (10, 4, 0, 2276),
        'APAVLOV': (0, 11, 3, 3559),
        'EXT_ZD': (9, 3, 2, 2448),
        'GEN_ZD': (9, 3, 2, 2433),
        'GRIM': (3, 9, 2, 3406),
        'GTFT': (2, 9, 3, 3427),
        'HILL_CLIMBING': (4, 6, 4, 2703),
        'PAVLOV': (0, 8, 6, 3155),
        'RAND': (3, 5, 6, 2808),
        'STFT': (3, 11, 0, 2388),
        'TF2T': (0, 8, 6, 3417),
        'TFT': (0, 11, 3, 3480)}
}

def color_difference(strat_parent: list[int], strat_child: list[int]):
    print("Child: [", end="")
    for i in range(len(strat_child)):
        if strat_child[i] != strat_parent[i]:
            print(f"\033[91m{strat_child[i]}\033[0m", end=", ")
        else:
            print(strat_child[i], end=", ")
    print("]")

def graph_win_count(data: dict):
    x = len(list(data.values())[0])
    x_axis = np.arange(x)
    width = 0.2
    plt.figure(layout="constrained")
    for i, (iteration, results) in enumerate(data.items()):
        strategy = list(results.keys())
        wins = [scores[0] for scores in results.values()]
        offset = width * i
        plt.bar(x_axis + offset, wins, width, label=f"Iteration {iteration}")
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Wins")
    plt.title("Wins by Strategy (TFT)")
    #plt.show()
    plt.savefig(f'hc-tft-win-count.png')
    plt.close()

def graph_score_count(data:dict):
    x = len(list(data.values())[0])
    x_axis = np.arange(x)
    width = 0.2
    plt.figure(layout="constrained")
    for i, (iteration, results) in enumerate(data.items()):
        strategy = list(results.keys())
        cumulative_score = [scores[3] for scores in results.values()]
        offset = width * i
        #plt.bar(strategy, cumulative_score, label=f"Iteration {iteration}")
        score_deviation = [s - max(cumulative_score) for s in cumulative_score]
        plt.bar(x_axis + offset, score_deviation, width, label=f"Iteration {iteration}")
    
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Deviation from Max Score")
    plt.title("Deviation from Max Score by Strategy (TFT)")
    #plt.show()
    plt.savefig(f'hc-tft-score-deviation.png')
    plt.close()

if __name__ == '__main__':
    print("Parent: ", init_strategy)
    color_difference(init_strategy, iter_100)
    color_difference(init_strategy, iter_500)
    color_difference(init_strategy, iter_1000)
    graph_win_count(data)
    graph_score_count(data)

