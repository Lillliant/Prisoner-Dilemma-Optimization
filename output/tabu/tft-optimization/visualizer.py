from matplotlib import pyplot as plt
import numpy as np

init_strategy = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]

# optimized strategy as obtained from data folder
ts_50 = [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
ts_100 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
ts_500 = [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]

data = {
    50: {
        'ALLC': (0, 9, 5, 3420),
        'ALLD': (11, 3, 0, 2688),
        'APAVLOV': (0, 10, 4, 3480),
        'EXT_ZD': (9, 3, 2, 2297),
        'GEN_ZD': (10, 3, 1, 2381),
        'GRIM': (2, 9, 3, 3373),
        'GTFT': (2, 9, 3, 3444),
        'PAVLOV': (0, 9, 5, 3513),
        'RAND': (5, 3, 6, 2837),
        'STFT': (5, 9, 0, 2564),
        'TABU_SEARCH': (0, 7, 7, 2873),
        'TF2T': (0, 9, 5, 3481),
        'TFT': (0, 11, 3, 3474)},
    100: {
        'ALLC': (0, 9, 5, 3417),
        'ALLD': (11, 3, 0, 2656),
        'APAVLOV': (0, 11, 3, 3471),
        'EXT_ZD': (8, 4, 2, 2399),
        'GEN_ZD': (9, 4, 1, 2441),
        'GRIM': (3, 9, 2, 3448),
        'GTFT': (2, 9, 3, 3439),
        'PAVLOV': (1, 9, 4, 3429),
        'RAND': (4, 4, 6, 2777),
        'STFT': (4, 10, 0, 2576),
        'TABU_SEARCH': (0, 7, 7, 3041),
        'TF2T': (0, 9, 5, 3550),
        'TFT': (0, 10, 4, 3475)},
    500: {
        'ALLC': (0, 9, 5, 3429),
        'ALLD': (11, 3, 0, 2672),
        'APAVLOV': (0, 11, 3, 3502),
        'EXT_ZD': (10, 3, 1, 2286),
        'GEN_ZD': (9, 3, 2, 2406),
        'GRIM': (2, 9, 3, 3391),
        'GTFT': (2, 9, 3, 3401),
        'PAVLOV': (1, 9, 4, 3442),
        'RAND': (2, 5, 7, 2763),
        'STFT': (4, 10, 0, 2571),
        'TABU_SEARCH': (1, 7, 6, 3071),
        'TF2T': (0, 9, 5, 3492),
        'TFT': (0, 11, 3, 3509)}
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
    plt.title("Wins by Strategy (TFT)")
    #plt.show()
    plt.savefig(f'ts-tft-win-count.png')
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
    plt.title("Deviation from Max Score by Strategy (TFT)")
    #plt.show()
    plt.savefig(f'ts-tft-score-deviation.png')
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

