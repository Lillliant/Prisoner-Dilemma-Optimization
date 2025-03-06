# global variables used like macros
COOPERATE = 0
DEFECT = 1

MEMORY_DEPTH=3
ITERATION=100

# payoff matrix
PAYOFF = {
    (COOPERATE,COOPERATE):(3,3),
    (DEFECT,COOPERATE):(5, 0),
    (COOPERATE,DEFECT):(0, 5),
    (DEFECT, DEFECT):(1,1)
}