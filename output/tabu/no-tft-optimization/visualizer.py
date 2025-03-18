from matplotlib import pyplot as plt
import numpy as np

init_strategy = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1] 

# optimized strategy as obtained from data folder
ts_50 = [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0]
ts_100 = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1]
ts_500 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]

data = {
    50: {
        'ALLC': (0, 8, 6, 3279),
        'ALLD': (10, 4, 0, 2276),
        'APAVLOV': (0, 11, 3, 3520),
        'EXT_ZD': (7, 4, 3, 2220),
        'GEN_ZD': (9, 4, 1, 2300),
        'GRIM': (2, 11, 1, 3207),
        'GTFT': (1, 9, 4, 3283),
        'PAVLOV': (1, 8, 5, 3360),
        'RAND': (4, 4, 6, 2869),
        'STFT': (3, 11, 0, 2394),
        'TABU_SEARCH': (4, 7, 3, 2705),
        'TF2T': (0, 9, 5, 3509),
        'TFT': (0, 10, 4, 3500)},
    100: {
        'ALLC': (0, 8, 6, 3276),
        'ALLD': (11, 3, 0, 2320),
        'APAVLOV': (0, 10, 4, 3477),
        'EXT_ZD': (8, 4, 2, 2197),
        'GEN_ZD': (8, 5, 1, 2232),
        'GRIM': (1, 10, 3, 3188),
        'GTFT': (1, 9, 4, 3280),
        'PAVLOV': (1, 8, 5, 3320),
        'RAND': (4, 2, 8, 2636),
        'STFT': (5, 9, 0, 2584),
        'TABU_SEARCH': (6, 6, 2, 3345),
        'TF2T': (0, 8, 6, 3391),
        'TFT': (0, 10, 4, 3508)},
    500: {
        'ALLC': (0, 8, 6, 3186),
        'ALLD': (11, 3, 0, 2680),
        'APAVLOV': (0, 11, 3, 3499),
        'EXT_ZD': (10, 3, 1, 2338),
        'GEN_ZD': (9, 3, 2, 2549),
        'GRIM': (2, 9, 3, 3381),
        'GTFT': (2, 9, 3, 3404),
        'PAVLOV': (0, 8, 6, 3317),
        'RAND': (3, 5, 6, 2839),
        'STFT': (4, 10, 0, 2509),
        'TABU_SEARCH': (4, 4, 6, 3376),
        'TF2T': (0, 8, 6, 3355),
        'TFT': (0, 11, 3, 3477)}
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
    for i, (tabu_size, results) in enumerate(data.items()):
        strategy = list(results.keys())
        wins = [scores[0] for scores in results.values()]
        offset = width * i
        plt.bar(x_axis + offset, wins, width, label=f"Tabu Size {tabu_size}")
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Wins")
    plt.title("Wins by Strategy")
    #plt.show()
    plt.savefig(f'ts-no-tft-win-count.png')
    plt.close()

def graph_score_count(data:dict):
    x = len(list(data.values())[0])
    x_axis = np.arange(x)
    width = 0.2
    plt.figure(layout="constrained")
    for i, (tabu_size, results) in enumerate(data.items()):
        strategy = list(results.keys())
        cumulative_score = [scores[3] for scores in results.values()]
        score_deviation = [s - max(cumulative_score) for s in cumulative_score]
        offset = width * i
        plt.bar(x_axis + offset, score_deviation, width, label=f"Tabu Size {tabu_size}")
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Deviation from Max Score")
    plt.title("Deviation from Max Score by Strategy")
    #plt.show()
    plt.savefig(f'ts-no-tft-score-deviation.png')
    plt.close()

if __name__ == '__main__':
    print("Parent: ", init_strategy)
    color_difference(init_strategy, ts_50)
    color_difference(init_strategy, ts_100)
    color_difference(init_strategy, ts_500)
    print("===\nParent: ", ts_50)
    color_difference(ts_50, ts_100)
    color_difference(ts_50, ts_500)
    print("===\nParent: ", ts_100)
    color_difference(ts_100, ts_500)
    graph_win_count(data)
    graph_score_count(data)

