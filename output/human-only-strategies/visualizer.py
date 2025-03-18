from matplotlib import pyplot as plt
import numpy as np

# Data as obtained from the data folder
# memory depth : results
data_r10 = {
    2: {
        'ALLC': (0, 9, 4, 318),
        'ALLD': (10, 3, 0, 262),
        'APAVLOV': (0, 9, 4, 308),
        'EXT_ZD': (6, 5, 2, 276),
        'GEN_ZD': (8, 3, 2, 285),
        'GRIM': (1, 9, 3, 312),
        'GTFT': (0, 9, 4, 329),
        'PAVLOV': (0, 9, 4, 322),
        'RAND': (5, 4, 4, 292),
        'STFT': (4, 9, 0, 265),
        'TF2T': (0, 9, 4, 336),
        'TFT': (0, 10, 3, 327)},
    3: {
        'ALLC': (0, 8, 5, 312),
        'ALLD': (10, 3, 0, 262),
        'APAVLOV': (0, 9, 4, 330),
        'EXT_ZD': (4, 7, 2, 353),
        'GEN_ZD': (8, 3, 2, 288),
        'GRIM': (1, 10, 2, 328),
        'GTFT': (0, 10, 3, 326),
        'PAVLOV': (0, 9, 4, 327),
        'RAND': (6, 5, 2, 321),
        'STFT': (3, 10, 0, 267),
        'TF2T': (0, 8, 5, 334),
        'TFT': (0, 10, 3, 337)},
    4: {
        'ALLC': (0, 8, 5, 324),
        'ALLD': (10, 3, 0, 274),
        'APAVLOV': (0, 9, 4, 321),
        'EXT_ZD': (5, 7, 1, 315),
        'GEN_ZD': (8, 4, 1, 302),
        'GRIM': (1, 10, 2, 328),
        'GTFT': (0, 10, 3, 345),
        'PAVLOV': (0, 8, 5, 319),
        'RAND': (6, 4, 3, 278),
        'STFT': (3, 10, 0, 275),
        'TF2T': (0, 8, 5, 324),
        'TFT': (0, 9, 4, 320)},
    10: {
        'ALLC': (0, 8, 5, 306),
        'ALLD': (10, 3, 0, 258),
        'APAVLOV': (2, 9, 2, 340),
        'EXT_ZD': (3, 5, 5, 281),
        'GEN_ZD': (9, 3, 1, 306),
        'GRIM': (2, 9, 2, 317),
        'GTFT': (0, 9, 4, 297),
        'PAVLOV': (0, 8, 5, 317),
        'RAND': (5, 3, 5, 279),
        'STFT': (4, 9, 0, 256),
        'TF2T': (0, 9, 4, 335),
        'TFT': (0, 11, 2, 345)}
}

# memory depth : results
data_r100 = {
    2: {
        'ALLC': (0, 8, 5, 3177),
        'ALLD': (10, 3, 0, 2180),
        'APAVLOV': (0, 9, 4, 3259),
        'EXT_ZD': (7, 4, 2, 2137),
        'GEN_ZD': (9, 3, 1, 2102),
        'GRIM': (1, 10, 2, 3125),
        'GTFT': (1, 9, 3, 3168),
        'PAVLOV': (0, 8, 5, 3133),
        'RAND': (4, 3, 6, 2655),
        'STFT': (4, 9, 0, 2322),
        'TF2T': (0, 8, 5, 3196),
        'TFT': (0, 10, 3, 3199)},
    3: {
        'ALLC': (0, 8, 5, 3183),
        'ALLD': (10, 3, 0, 2148),
        'APAVLOV': (0, 9, 4, 3173),
        'EXT_ZD': (7, 4, 2, 2045),
        'GEN_ZD': (8, 4, 1, 2132),
        'GRIM': (1, 11, 1, 3139),
        'GTFT': (1, 9, 3, 3168),
        'PAVLOV': (1, 8, 4, 3209),
        'RAND': (3, 4, 6, 2464),
        'STFT': (3, 10, 0, 2274),
        'TF2T': (0, 8, 5, 3234),
        'TFT': (0, 10, 3, 3202)},
    4: {
        'ALLC': (0, 8, 5, 3132),
        'ALLD': (10, 3, 0, 2204),
        'APAVLOV': (0, 9, 4, 3171),
        'EXT_ZD': (7, 3, 3, 2070),
        'GEN_ZD': (9, 3, 1, 2106),
        'GRIM': (2, 9, 2, 3118),
        'GTFT': (1, 9, 3, 3142),
        'PAVLOV': (0, 8, 5, 3120),
        'RAND': (5, 2, 6, 2638),
        'STFT': (4, 9, 0, 2285),
        'TF2T': (0, 8, 5, 3208),
        'TFT': (0, 9, 4, 3237)},
    10: {
        'ALLC': (0, 8, 5, 3135),
        'ALLD': (10, 3, 0, 2176),
        'APAVLOV': (1, 9, 3, 3082),
        'EXT_ZD': (7, 4, 2, 2096),
        'GEN_ZD': (9, 3, 1, 2107),
        'GRIM': (1, 9, 3, 3109),
        'GTFT': (1, 10, 2, 3201),
        'PAVLOV': (1, 8, 4, 3157),
        'RAND': (2, 3, 8, 2320),
        'STFT': (4, 9, 0, 2189),
        'TF2T': (0, 8, 5, 3190),
        'TFT': (0, 10, 3, 3215),
    }
}

data_r1000 = {
    2:  {'ALLC': (0, 8, 5, 31296),
        'ALLD': (10, 3, 0, 21080),
        'APAVLOV': (0, 9, 4, 31848),
        'EXT_ZD': (8, 4, 1, 18492),
        'GEN_ZD': (7, 5, 1, 20169),
        'GRIM': (1, 10, 2, 30657),
        'GTFT': (1, 9, 3, 30912),
        'PAVLOV': (1, 8, 4, 31393),
        'RAND': (4, 3, 6, 25935),
        'STFT': (3, 10, 0, 22311),
        'TF2T': (0, 8, 5, 31919),
        'TFT': (0, 9, 4, 31790)},
    3: {'ALLC': (0, 8, 5, 31365),
        'ALLD': (10, 3, 0, 21048),
        'APAVLOV': (0, 10, 3, 31761),
        'EXT_ZD': (8, 3, 2, 18450),
        'GEN_ZD': (9, 3, 1, 20285),
        'GRIM': (1, 9, 3, 30784),
        'GTFT': (1, 9, 3, 31116),
        'PAVLOV': (0, 8, 5, 31248),
        'RAND': (3, 5, 5, 25330),
        'STFT': (3, 10, 0, 22422),
        'TF2T': (0, 8, 5, 31855),
        'TFT': (0, 10, 3, 31745)},
    4: {'ALLC': (0, 8, 5, 31176),
        'ALLD': (10, 3, 0, 21008),
        'APAVLOV': (0, 10, 3, 31700),
        'EXT_ZD': (8, 3, 2, 18437),
        'GEN_ZD': (9, 3, 1, 20162),
        'GRIM': (1, 9, 3, 30915),
        'GTFT': (1, 9, 3, 31025),
        'PAVLOV': (0, 8, 5, 31392),
        'RAND': (4, 3, 6, 25252),
        'STFT': (4, 9, 0, 22384),
        'TF2T': (0, 8, 5, 31927),
        'TFT': (0, 9, 4, 31767)},
    10: {'ALLC': (0, 8, 5, 31452),
        'ALLD': (10, 3, 0, 21152),
        'APAVLOV': (1, 9, 3, 30910),
        'EXT_ZD': (7, 3, 3, 18309),
        'GEN_ZD': (9, 3, 1, 20308),
        'GRIM': (2, 9, 2, 30917),
        'GTFT': (1, 9, 3, 30992),
        'PAVLOV': (1, 8, 4, 31379),
        'RAND': (3, 2, 8, 23217),
        'STFT': (4, 9, 0, 20788),
        'TF2T': (0, 8, 5, 31973),
        'TFT': (0, 9, 4, 31746)}
}

# visualize the win count per strategy for a specific memory depth
# given a fixed number of rounds
def visualize_win_by_memory(data: dict, name: str):
    # x: strategies
    # y_i: wins for memory depth i, ordered by strategy
    x = len(list(data.values())[0])
    x_axis = np.arange(x)
    width = 0.2
    plt.figure(layout="constrained")
    for i, (memory_depth, results) in enumerate(data.items()):
        #plt.subplots(layout="constrained")
        strategy = list(results.keys())
        wins = [scores[0] for scores in results.values()]
        offset = width * i
        plt.bar(x_axis + offset, wins, width, label=f"Memory Depth {memory_depth}")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    plt.legend()
    plt.xlabel("Strategy")
    plt.xticks(x_axis + width, strategy, rotation=-90)
    plt.ylabel("Wins")
    plt.title("Wins by Strategy")
    #plt.show()
    plt.savefig(f'{name}-wincount.png')
    plt.close()

def visualize_score_by_memory(data: dict , name:str):
        # x: strategies
    # y_i: wins for memory depth i, ordered by strategy
    x = len(list(data.values())[0])
    x_axis = np.arange(x)
    width = 0.2
    for i, (memory_depth, results) in enumerate(data.items()):
        plt.subplots(layout="constrained")
        strategy = list(results.keys())
        cumulative_score = [scores[3] for scores in results.values()]
        score_ratio = [score - max(cumulative_score) for score in cumulative_score]
        offset = width * i
        plt.bar(strategy, score_ratio, label=f"Memory Depth {memory_depth}")
        plt.legend()
        plt.xlabel("Strategy")
        plt.xticks(strategy, rotation=-90)
        plt.ylabel("Deviation from Max Score")
        plt.title("Deviation from Max Score by Strategy")
        #plt.show()
        plt.savefig(f'{name}-{memory_depth}-score-deviation.png')
        plt.close()

if __name__ == "__main__":
    visualize_win_by_memory(data_r1000, name="R1000")
    #visualize_score_by_memory(data_r10, name="R10")