from matplotlib import pyplot as plt
import numpy as np

# optimized strategies from neighbours optimization
m0001n_strategy = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
m001n_strategy = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
m01n_strategy = [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0]
data_neightbors = {
    0.001: {
        'ALLC': (0, 8, 6, 3174),
        'ALLD': (11, 3, 0, 2292),
        'APAVLOV': (0, 10, 4, 3500),
        'EXT_ZD': (9, 4, 1, 2234),
        'GENETIC': (4, 7, 3, 3224),
        'GEN_ZD': (8, 5, 1, 2210),
        'GRIM': (1, 10, 3, 3197),
        'GTFT': (1, 9, 4, 3213),
        'PAVLOV': (1, 9, 4, 3448),
        'RAND': (3, 4, 7, 2834),
        'STFT': (4, 10, 0, 2580),
        'TF2T': (0, 8, 6, 3295),
        'TFT': (0, 11, 3, 3520)
    },
    0.01: {
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
    0.1: {
        'ALLC': (0, 8, 6, 3432),
        'ALLD': (11, 3, 0, 2636),
        'APAVLOV': (0, 9, 5, 3444),
        'EXT_ZD': (10, 3, 1, 2435),
        'GENETIC': (6, 2, 6, 2959),
        'GEN_ZD': (9, 3, 2, 2479),
        'GRIM': (2, 9, 3, 3416),
        'GTFT': (2, 9, 3, 3535),
        'PAVLOV': (0, 8, 6, 3148),
        'RAND': (5, 2, 7, 2837),
        'STFT': (5, 9, 0, 2531),
        'TF2T': (0, 8, 6, 3403),
        'TFT': (0, 9, 5, 3414)
    }
}

# optimized strategies from TFT optimization
m0001t_strategy = [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0]
m001t_strategy = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
m01t_strategy = [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
data_tft = {
    0.001: {
        'ALLC': (0, 8, 6, 3447),
        'ALLD': (11, 3, 0, 2280),
        'APAVLOV': (0, 10, 4, 3470),
        'EXT_ZD': (7, 4, 3, 2323),
        'GENETIC': (4, 6, 4, 2490),
        'GEN_ZD': (8, 4, 2, 2403),
        'GRIM': (3, 10, 1, 3445),
        'GTFT': (2, 10, 2, 3466),
        'PAVLOV': (1, 9, 4, 3408),
        'RAND': (3, 4, 7, 2827),
        'STFT': (3, 11, 0, 2377),
        'TF2T': (0, 8, 6, 3491),
        'TFT': (0, 11, 3, 3511)
    },
    0.01: {
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
    0.1: {
        'ALLC': (0, 8, 6, 3465),
        'ALLD': (11, 3, 0, 2488),
        'APAVLOV': (0, 10, 4, 3498),
        'EXT_ZD': (10, 3, 1, 2331),
        'GENETIC': (3, 4, 7, 2990),
        'GEN_ZD': (9, 3, 2, 2440),
        'GRIM': (2, 9, 3, 3382),
        'GTFT': (2, 9, 3, 3422),
        'PAVLOV': (0, 8, 6, 3282),
        'RAND': (6, 3, 5, 2824),
        'STFT': (4, 10, 0, 2593),
        'TF2T': (0, 8, 6, 3496),
        'TFT': (0, 10, 4, 3502)
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
        plt.bar(x_axis + offset, wins, width, label=f"Mutation Rate {var}")
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
        plt.bar(x_axis + offset, score_deviation, width, label=f"Mutation Rate {var}")
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
    print("Parent: ", m0001n_strategy)
    color_difference(m0001n_strategy, m001n_strategy)
    color_difference(m0001n_strategy, m01n_strategy)
    print("===\nParent: ", m001n_strategy)
    color_difference(m001n_strategy, m01n_strategy)
    graph_win_count(data_neightbors, "no-tft")
    graph_score_count(data_neightbors, "no-tft")
    print("===\n===\nParent: ", m0001t_strategy)
    color_difference(m0001t_strategy, m001t_strategy)
    color_difference(m0001t_strategy, m01t_strategy)
    print("===\nParent: ", m001t_strategy)
    color_difference(m001t_strategy, m01t_strategy)
    graph_win_count(data_tft, "tft")
    graph_score_count(data_tft, "tft")