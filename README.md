# Introduction

The project is inspired by new approach for tackling the problem of finding game equilibriums, presented in [The Mechanics of n−Player Differentiable Games](https://arxiv.org/pdf/1802.05642.pdf) [1].

We (1) reproduce multiple experiments from this paper, (2) develop techniques that are useful in the problem of finding equilibria when just a stochastic gradient approximation can be computed and (3) conduct a theoretical convergence analysis in case of games with quadratic
loss functions

# Code description

`four_player_SGA.ipynb` - convergence analysis of optimization methods on a simple four-player game from Appendix D in [1]

`rock_paper_scissors.ipynb` - analysis of dynamics of a rock-paper-scissors game

`four_player_*.ipynb` - reproduction of experiment in appendix D of [1]

`reconstruction.py` - reproduction of some experiments from main part of the paper

`gan_experiments.ipynb` - the effect of game dynamics on behavior of generator and beyond

# References

[1] [The Mechanics of n−Player Differentiable Games](https://arxiv.org/pdf/1802.05642.pdf)
