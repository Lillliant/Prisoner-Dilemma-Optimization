My Optimized Genetic Algorithm for Prisoner’s Dilemma

Overview

This a Genetic Algorithm (GA) to find the best strategy for the Iterated Prisoner’s Dilemma (IPD). I tweaked it to optimize against an opponent who always cooperates, aiming to get the highest possible score. My idea was to start with a random strategy and evolve it over time, making it super good at beating this specific opponent.

How It Works

Strategy Encoding:
I use binary strings for my strategies:
'0' = Cooperate (C)
'1' = Defect (D)
For example, '01011' means I cooperate, defect, cooperate, defect, defect.

Evaluation Function:
I check how good my strategy is by playing it against '00000' (Always Cooperate) for 10 rounds. I add up my points using the Prisoner’s Dilemma payoffs to see my total score.

Group Generation:
I start with a small group of strategies—my initial one plus a few random ones. This is my team that I improve step-by-step.

My Genetic Algorithm Process:
- Scoring: I test each strategy in my group against the opponent to get their scores.
- Picking Winners: I grab the two strategies with the highest scores.
- Mixing: I mix these two at a random spot to make two new strategies.
- Tweaking: I change one bit in each new strategy, leaning towards defecting since that’s better against cooperation.
- Updating: I keep the top two and add my new ones to form the next group.
- I repeat this for a few steps to evolve the best strategy.

Output:
My code prints:
- My Starting Strategy (where I kicked things off)
- My Best Strategy (the optimized winner)
- My Best Score (the total points I got)

Dependencies:
Just Python is needed. Nothing fancy, so it’s easy to run!
