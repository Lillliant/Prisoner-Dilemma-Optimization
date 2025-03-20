# Prisoner's Dilemma Optimization
The structure of the framework is as follows:
```
├── data
│   └── This folder contains the raw data from our experiment.
├── output
|   ├── visualizer.py: this file is used to generate the files given the appropriate data
│   └── This folder contains the processed data and figures
└── src
    ├── optimization: This folder contains the optimization methods (Hill Climbing, Tabu Search, Genetic Algorithm)
    ├── tournament: This folder contains the simulator, Player class, and human-designed strategies
    ├── config.py
    └── main.py
```
# Optimization Methods
This repository contains 3 optimization methods: Hill Climbing, Tabu Search, and Genetic Algorithm. Each method allows for an initial strategy (or population strategy). If no opponent strategy is passed, the method defaults to Neighbour Optimization.

The optimization parameters can be adjusted within `config.py` in `src` folder.
