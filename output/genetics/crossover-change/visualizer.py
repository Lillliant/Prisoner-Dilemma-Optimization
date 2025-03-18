from matplotlib import pyplot as plt
import numpy as np

# optimized strategies from neighbours optimization
c03n_strategy = [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1]
c05n_strategy = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
c07n_strategy = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
data_neightbors = {
    0.3: {
        'ALLC': (0, 8, 6, 3429),
        'ALLD': (11, 3, 0, 2484),
        'APAVLOV': (0, 10, 4, 3426),
        'EXT_ZD': (9, 3, 2, 2263),
        'GENETIC': (5, 4, 5, 2746),
        'GEN_ZD': (10, 3, 1, 2460),
        'GRIM': (2, 9, 3, 3377),
        'GTFT': (2, 9, 3, 3391),
        'PAVLOV': (0, 9, 5, 3323),
        'RAND': (3, 4, 7, 2787),
        'STFT': (4, 10, 0, 2523),
        'TF2T': (0, 8, 6, 3501),
        'TFT': (0, 10, 4, 3404)
    },
    0.5: {
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
    },
    0.7: {
        'ALLC': (0, 8, 6, 3288),
        'ALLD': (11, 3, 0, 2476),
        'APAVLOV': (0, 10, 4, 3436),
        'EXT_ZD': (7, 4, 3, 2353),
        'GENETIC': (2, 6, 6, 2772),
        'GEN_ZD': (9, 4, 1, 2432),
        'GRIM': (3, 10, 1, 3393),
        'GTFT': (2, 9, 3, 3409),
        'PAVLOV': (2, 9, 3, 3408),
        'RAND': (3, 4, 7, 2676),
        'STFT': (4, 10, 0, 2578),
        'TF2T': (0, 8, 6, 3362),
        'TFT': (0, 11, 3, 3452)
    }
}

# optimized strategies from TFT optimization
c03t_strategy = [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0]
c05t_strategy = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
c07t_strategy = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]
data_tft = {
    0.3: {
        'ALLC': (0, 9, 5, 3429),
        'ALLD': (11, 3, 0, 2348),
        'APAVLOV': (0, 10, 4, 3501),
        'EXT_ZD': (9, 3, 2, 2215),
        'GENETIC': (0, 9, 5, 3505),
        'GEN_ZD': (10, 3, 1, 2249),
        'GRIM': (1, 10, 3, 3364),
        'GTFT': (1, 10, 3, 3408),
        'PAVLOV': (1, 9, 4, 3416),
        'RAND': (5, 2, 7, 2796),
        'STFT': (5, 9, 0, 2623),
        'TF2T': (0, 9, 5, 3534),
        'TFT': (0, 10, 4, 3551)
    },
    0.5: {
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
    },
    0.7: {
        'ALLC': (0, 9, 5, 3468),
        'ALLD': (11, 3, 0, 2356),
        'APAVLOV': (0, 11, 3, 3476),
        'EXT_ZD': (9, 4, 1, 2173),
        'GENETIC': (1, 8, 5, 3372),
        'GEN_ZD': (9, 4, 1, 2318),
        'GRIM': (2, 9, 3, 3419),
        'GTFT': (2, 9, 3, 3485),
        'PAVLOV': (1, 9, 4, 3446),
        'RAND': (3, 3, 8, 2786),
        'STFT': (4, 10, 0, 2527),
        'TF2T': (0, 9, 5, 3515),
        'TFT': (0, 10, 4, 3472)
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
        plt.bar(x_axis + offset, wins, width, label=f"Crossover Rate {var}")
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
        plt.bar(x_axis + offset, score_deviation, width, label=f"Crossover Rate {var}")
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
    print("Parent: ", c03n_strategy)
    color_difference(c03n_strategy, c05n_strategy)
    color_difference(c03n_strategy, c07n_strategy)
    print("===\nParent: ", c05n_strategy)
    color_difference(c05n_strategy, c07n_strategy)
    graph_win_count(data_neightbors, "no-tft")
    graph_score_count(data_neightbors, "no-tft")
    print("===\n===\nParent: ", c03t_strategy)
    color_difference(c03t_strategy, c05t_strategy)
    color_difference(c03t_strategy, c07t_strategy)
    print("===\nParent: ", c05t_strategy)
    color_difference(c05t_strategy, c07t_strategy)
    graph_win_count(data_tft, "tft")
    graph_score_count(data_tft, "tft")