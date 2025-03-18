from matplotlib import pyplot as plt
import numpy as np

# optimized strategies from neighbours optimization
p50n_strategy = [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1]
p100n_strategy = [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
p500n_strategy = [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]
data_neightbors = {
    50: {
        'ALLC': (0, 8, 6, 3327),
        'ALLD': (11, 3, 0, 2496),
        'APAVLOV': (0, 11, 3, 3418),
        'EXT_ZD': (9, 3, 2, 2336),
        'GENETIC': (4, 5, 5, 2845),
        'GEN_ZD': (10, 3, 1, 2391),
        'GRIM': (2, 9, 3, 3333),
        'GTFT': (2, 9, 3, 3358),
        'PAVLOV': (1, 8, 5, 3248),
        'RAND': (3, 4, 7, 2761),
        'STFT': (3, 11, 0, 2479),
        'TF2T': (0, 8, 6, 3499),
        'TFT': (0, 10, 4, 3369)
    },
    100: {
        'ALLC': (0, 9, 5, 3498),
        'ALLD': (11, 3, 0, 2388),
        'APAVLOV': (0, 11, 3, 3484),
        'EXT_ZD': (9, 4, 1, 2218),
        'GENETIC': (1, 9, 4, 3525),
        'GEN_ZD': (9, 4, 1, 2246),
        'GRIM': (1, 10, 3, 3371),
        'GTFT': (1, 10, 3, 3451),
        'PAVLOV': (1, 9, 4, 3439),
        'RAND': (3, 3, 8, 2741),
        'STFT': (5, 9, 0, 2588),
        'TF2T': (0, 9, 5, 3481),
        'TFT': (0, 10, 4, 3508)
    },
    300: {
        'ALLC': (0, 8, 6, 3087),
        'ALLD': (11, 3, 0, 2404),
        'APAVLOV': (0, 10, 4, 3441),
        'EXT_ZD': (9, 3, 2, 2428),
        'GENETIC': (6, 2, 6, 2868),
        'GEN_ZD': (9, 3, 2, 2443),
        'GRIM': (3, 9, 2, 3398),
        'GTFT': (2, 9, 3, 3382),
        'PAVLOV': (0, 8, 6, 3318),
        'RAND': (3, 4, 7, 2759),
        'STFT': (5, 9, 0, 2517),
        'TF2T': (0, 8, 6, 3495),
        'TFT': (0, 10, 4, 3439)
    }
}

# optimized strategies from TFT optimization
p50t_strategy = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]
p100t_strategy = [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
p500t_strategy = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0]
data_tft = {
    50: {
        'ALLC': (0, 9, 5, 3444),
        'ALLD': (11, 3, 0, 2288),
        'APAVLOV': (0, 11, 3, 3507),
        'EXT_ZD': (8, 3, 3, 2163),
        'GENETIC': (0, 9, 5, 3524),
        'GEN_ZD': (9, 4, 1, 2507),
        'GRIM': (2, 10, 2, 3434),
        'GTFT': (1, 11, 2, 3469),
        'PAVLOV': (0, 9, 5, 3452),
        'RAND': (4, 5, 5, 2921),
        'STFT': (4, 10, 0, 2622),
        'TF2T': (0, 9, 5, 3483),
        'TFT': (0, 11, 3, 3495)
    },
    100: {
        'ALLC': (0, 8, 6, 3318),
        'ALLD': (11, 3, 0, 2508),
        'APAVLOV': (0, 11, 3, 3523),
        'EXT_ZD': (8, 4, 2, 2374),
        'GENETIC': (4, 4, 6, 3071),
        'GEN_ZD': (9, 3, 2, 2486),
        'GRIM': (3, 10, 1, 3414),
        'GTFT': (2, 9, 3, 3435),
        'PAVLOV': (0, 8, 6, 3324),
        'RAND': (4, 3, 7, 2720),
        'STFT': (5, 9, 0, 2582),
        'TF2T': (0, 8, 6, 3489),
        'TFT': (0, 10, 4, 3470)
    },
    300: {
        'ALLC': (0, 8, 6, 3444),
        'ALLD': (11, 3, 0, 2488),
        'APAVLOV': (0, 10, 4, 3383),
        'EXT_ZD': (8, 3, 3, 2162),
        'GENETIC': (5, 3, 6, 2648),
        'GEN_ZD': (10, 3, 1, 2351),
        'GRIM': (3, 9, 2, 3419),
        'GTFT': (2, 9, 3, 3194),
        'PAVLOV': (2, 8, 4, 3448),
        'RAND': (2, 5, 7, 2761),
        'STFT': (3, 11, 0, 2483),
        'TF2T': (0, 8, 6, 3496),
        'TFT': (0, 10, 4, 3365)
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
        plt.bar(x_axis + offset, wins, width, label=f"Population Size {var}")
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Wins")
    plt.title("Wins by Strategy")
    #plt.show()
    plt.savefig(f'ts-{name}-win-count.png')
    plt.close()

def graph_score_count(data:dict, name: str):
    x = len(list(data.values())[0])
    for var, results in data.items():
        plt.subplots(layout="constrained")
        strategy = list(results.keys())
        cumulative_score = [scores[3] for scores in results.values()]
        score_deviation = [s - max(cumulative_score) for s in cumulative_score]
        plt.bar(strategy, score_deviation, label=f"Population Size {var}")
        plt.legend()
        plt.xlabel("Strategy")
        plt.xticks(strategy, rotation=-90)
        plt.ylabel("Deviation from Max Score")
        plt.title("Deviation from Max Score by Strategy")
        #plt.show()
        plt.savefig(f'ts-{name}-score-deviation-{var}.png')
        plt.close()

if __name__ == '__main__':
    print("Parent: ", p50n_strategy)
    color_difference(p50n_strategy, p100n_strategy)
    color_difference(p50n_strategy, p500n_strategy)
    print("===\nParent: ", p100n_strategy)
    color_difference(p100n_strategy, p500n_strategy)
    graph_win_count(data_neightbors, "no-tft")
    graph_score_count(data_neightbors, "no-tft")
    print("===\n===\nParent: ", p50t_strategy)
    color_difference(p50t_strategy, p100t_strategy)
    color_difference(p50t_strategy, p500t_strategy)
    print("===\nParent: ", p100t_strategy)
    color_difference(p100t_strategy, p500t_strategy)
    graph_win_count(data_tft, "tft")
    graph_score_count(data_tft, "tft")