from matplotlib import pyplot as plt
import numpy as np

init_strategy = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]

# optimized strategy as obtained from data folder
iter_100 = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
iter_500 = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
iter_1000 = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]

data = {
    100: {
        'ALLC': (0, 8, 6, 3222),
        'ALLD': (11, 3, 0, 2520),
        'APAVLOV': (0, 10, 4, 3450),
        'EXT_ZD': (8, 5, 1, 2255),
        'GEN_ZD': (9, 4, 1, 2389),
        'GRIM': (1, 10, 3, 3205),
        'GTFT': (2, 9, 3, 3511),
        'HILL_CLIMBING': (5, 6, 3, 2630),
        'PAVLOV': (1, 8, 5, 3231),
        'RAND': (2, 6, 6, 2851),
        'STFT': (3, 11, 0, 2560),
        'TF2T': (0, 8, 6, 3479),
        'TFT': (0, 10, 4, 3452)},
    500: {
        'ALLC': (0, 8, 6, 3288),
        'ALLD': (11, 3, 0, 2488),
        'APAVLOV': (0, 9, 5, 3423),
        'EXT_ZD': (9, 3, 2, 2126),
        'GEN_ZD': (9, 3, 2, 2361),
        'GRIM': (1, 10, 3, 3192),
        'GTFT': (2, 9, 3, 3594),
        'HILL_CLIMBING': (6, 4, 4, 2670),
        'PAVLOV': (1, 9, 4, 3218),
        'RAND': (4, 4, 6, 2743),
        'STFT': (3, 11, 0, 2524),
        'TF2T': (0, 8, 6, 3401),
        'TFT': (0, 9, 5, 3394)},
    1000: {
        'ALLC': (0, 8, 6, 3201),
        'ALLD': (11, 3, 0, 2512),
        'APAVLOV': (0, 10, 4, 3478),
        'EXT_ZD': (7, 4, 3, 2224),
        'GEN_ZD': (9, 4, 1, 2210),
        'GRIM': (1, 11, 2, 3212),
        'GTFT': (2, 9, 3, 3501),
        'HILL_CLIMBING': (6, 5, 3, 2725),
        'PAVLOV': (2, 8, 4, 3260),
        'RAND': (2, 4, 8, 2810),
        'STFT': (4, 10, 0, 2518),
        'TF2T': (0, 8, 6, 3450),
        'TFT': (0, 10, 4, 3417)}
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
    plt.title("Wins by Strategy")
    #plt.show()
    plt.savefig(f'hc-no-tft-win-count.png')
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
    plt.title("Deviation from Max Score by Strategy")
    #plt.show()
    plt.savefig(f'hc-no-tft-score-deviation.png')
    plt.close()

if __name__ == '__main__':
    print("Parent: ", init_strategy)
    color_difference(init_strategy, iter_100)
    color_difference(init_strategy, iter_500)
    color_difference(init_strategy, iter_1000)
    graph_win_count(data)
    graph_score_count(data)

