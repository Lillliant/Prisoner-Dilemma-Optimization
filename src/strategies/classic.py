# TFT, TF2T, STFT
# TODO: Take a look at the other Axelrod tournament strategies and whether they should be implemented in this module
from config import COOPERATE, DEFECT

def TFT(mem: list[int]):
    if (len(mem) == 0):
        return COOPERATE
    return mem[-1] # there is at least one elements

def TF2T(mem: list[int]):
    if (len(mem) < 2):
        return COOPERATE
    elif (mem[-1] == DEFECT and mem[-2] == DEFECT):
        return DEFECT
    else:
        return COOPERATE

def STFT(mem: list[int]):
    if (len(mem) == 0):
        return DEFECT
    return mem[-1]