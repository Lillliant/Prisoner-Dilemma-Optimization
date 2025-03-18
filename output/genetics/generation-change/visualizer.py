from matplotlib import pyplot as plt
import numpy as np

# optimized strategies from neighbours optimization
g50n_strategy = [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0]
g250n_strategy = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
g500n_strategy = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
data_neightbors = {
    50: {
        'ALLC': (0, 8, 6, 3150),
        'ALLD': (11, 3, 0, 2476),
        'APAVLOV': (0, 11, 3, 3393),
        'EXT_ZD': (9, 3, 2, 2144),
        'GENETIC': (6, 4, 4, 2285),
        'GEN_ZD': (8, 3, 3, 2153),
        'GRIM': (2, 9, 3, 3391),
        'GTFT': (2, 9, 3, 3370),
        'PAVLOV': (1, 8, 5, 3419),
        'RAND': (3, 4, 7, 2731),
        'STFT': (4, 10, 0, 2492),
        'TF2T': (0, 8, 6, 3292),
        'TFT': (0, 10, 4, 3357)
    },
    250: {
        'ALLC': (0, 8, 6, 3390),
        'ALLD': (11, 3, 0, 2440),
        'APAVLOV': (0, 11, 3, 3415),
        'EXT_ZD': (9, 3, 2, 2382),
        'GENETIC': (3, 6, 5, 2735),
        'GEN_ZD': (10, 3, 1, 2367),
        'GRIM': (2, 9, 3, 3407),
        'GTFT': (2, 9, 3, 3392),
        'PAVLOV': (0, 9, 5, 3342),
        'RAND': (4, 4, 6, 2694),
        'STFT': (3, 11, 0, 2496),
        'TF2T': (0, 8, 6, 3447),
        'TFT': (0, 10, 4, 3438)
    },
    500: {
        'ALLC': (0, 8, 6, 3162),
        'ALLD': (11, 3, 0, 2292),
        'APAVLOV': (0, 9, 5, 3297),
        'EXT_ZD': (8, 4, 2, 2175),
        'GENETIC': (10, 3, 1, 2483),
        'GEN_ZD': (8, 4, 2, 2132),
        'GRIM': (1, 9, 4, 3186),
        'GTFT': (1, 9, 4, 3231),
        'PAVLOV': (1, 8, 5, 3244),
        'RAND': (4, 2, 8, 2728),
        'STFT': (4, 10, 0, 2395),
        'TF2T': (0, 8, 6, 3323),
        'TFT': (0, 9, 5, 3289)
    }
}

# optimized strategies from TFT optimization
g50t_strategy = [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]
g250t_strategy = [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1]
g500t_strategy = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
data_tft = {
    50: {
        'ALLC': (0, 8, 6, 3315),
        'ALLD': (11, 3, 0, 2416),
        'APAVLOV': (0, 10, 4, 3399),
        'EXT_ZD': (9, 4, 1, 2283),
        'GENETIC': (2, 4, 8, 2635),
        'GEN_ZD': (9, 4, 1, 2411),
        'GRIM': (2, 9, 3, 3351),
        'GTFT': (2, 9, 3, 3371),
        'PAVLOV': (1, 8, 5, 3569),
        'RAND': (6, 2, 6, 2830),
        'STFT': (5, 9, 0, 2507),
        'TF2T': (0, 8, 6, 3403),
        'TFT': (0, 10, 4, 3415)
    },
    250: {
        'ALLC': (0, 9, 5, 3420),
        'ALLD': (11, 3, 0, 2676),
        'APAVLOV': (0, 10, 4, 3512),
        'EXT_ZD': (7, 4, 3, 2313),
        'GENETIC': (0, 10, 4, 3443),
        'GEN_ZD': (10, 3, 1, 2486),
        'GRIM': (1, 11, 2, 3379),
        'GTFT': (1, 10, 3, 3423),
        'PAVLOV': (2, 9, 3, 3506),
        'RAND': (5, 2, 7, 2790),
        'STFT': (4, 10, 0, 2536),
        'TF2T': (0, 9, 5, 3509),
        'TFT': (0, 10, 4, 3490)
    },
    500: {
        'ALLC': (0, 9, 5, 3450),
        'ALLD': (11, 3, 0, 2432),
        'APAVLOV': (0, 11, 3, 3478),
        'EXT_ZD': (9, 3, 2, 2360),
        'GENETIC': (0, 9, 5, 3531),
        'GEN_ZD': (10, 3, 1, 2374),
        'GRIM': (1, 10, 3, 3394),
        'GTFT': (1, 10, 3, 3421),
        'PAVLOV': (0, 9, 5, 3451),
        'RAND': (5, 3, 6, 2892),
        'STFT': (5, 9, 0, 2590),
        'TF2T': (0, 9, 5, 3567),
        'TFT': (0, 10, 4, 3487)
    }
}

def color_difference(strat_parent: list[int], strat_child: list[int]):
    print("Child: [", end="")
    for i in range(len(strat_child)):
        if strat_child[i] != strat_parent[i]:
            print(f"\033[91m{strat_child[i]}\033[0m", end=", ")
        else:
            print(strat_child[i], end=", ")
    print("]")

def graph_win_count(data: dict, name: str):
    x = len(list(data.values())[0])
    x_axis = np.arange(x)
    width = 0.2
    plt.figure(layout="constrained")
    for i, (var, results) in enumerate(data.items()):
        strategy = list(results.keys())
        wins = [scores[0] for scores in results.values()]
        offset = width * i
        plt.bar(x_axis + offset, wins, width, label=f"Generation {var}")
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Wins")
    if name == "tft":
        plt.title("Wins by Strategy (TFT)")
    else:
        plt.title("Wins by Strategy")
    #plt.show()
    plt.savefig(f'ts-{name}-win-count.png')
    plt.close()

def graph_score_count(data:dict, name: str):
    x = len(list(data.values())[0])
    x_axis = np.arange(x)
    width = 0.2
    plt.figure(layout="constrained")
    for i, (var, results) in enumerate(data.items()):
        #plt.subplots(layout="constrained")
        strategy = list(results.keys())
        cumulative_score = [scores[3] for scores in results.values()]
        score_deviation = [s - max(cumulative_score) for s in cumulative_score]
        offset = width * i
        plt.bar(x_axis + offset, score_deviation, width, label=f"Generation {var}")
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Deviation from Max Score")
    if name == 'tft':
        plt.title("Deviation from Max Score by Strategy (TFT)")
    else:
        plt.title("Deviation from Max Score by Strategy")
    #plt.show()
    plt.savefig(f'ts-{name}-score-deviation.png')
    plt.close()

if __name__ == '__main__':
    print("Parent: ", g50n_strategy)
    color_difference(g50n_strategy, g250n_strategy)
    color_difference(g50n_strategy, g500n_strategy)
    print("===\nParent: ", g250n_strategy)
    color_difference(g250n_strategy, g500n_strategy)
    graph_win_count(data_neightbors, "no-tft")
    graph_score_count(data_neightbors, "no-tft")
    print("===\n===\nParent: ", g50t_strategy)
    color_difference(g50t_strategy, g250t_strategy)
    color_difference(g50t_strategy, g500t_strategy)
    print("===\nParent: ", g250t_strategy)
    color_difference(g250t_strategy, g500t_strategy)
    graph_win_count(data_tft, "tft")
    graph_score_count(data_tft, "tft")