__TODO: fix formulas. Halve description of the paper, include short descriptions of our results__

# Introduction

The project is inspired by new approach for tackling the problem of finding game equilibriums, presented in [The Mechanics of n−Player Differentiable Games](https://arxiv.org/pdf/1802.05642.pdf) [1].  

The authors have proposed a new algorithm to find stable fixed points (which undersome conditions can be considered Nash equilibrium) by introducing the notion of Hamiltonian games and inventing a new algorithm to find stable fixed points (which under some conditions can be considered Nash equilibrium).

For a $n$-player game with parameter w, they define the Hessian of a game to be 
![equation](H(w) = \nabla_w \xi (w)^T)

Since this is a matrix, it always admits a symmetric and anti-symmetric decomposition: 
![equation](H(w) = S(w) + A(w))

This leads to a classification: Hamiltonian games are defined as games where the symmetric component is zero, *S(w) = 0*. Potential games are defined as games where the anti-symmetric component is zero, ![equation](A(w) = 0). 

One of the main theoretical contributions of this paper is that given an n-player Hamiltonian game with ![equation](H(w) = 1/2 \xi (w)^2), under some conditions the gradient descent on H converges to a Nash equilibrium.

# Code description

`four_player_SGA.ipynb` - convergence analysis of optimization methods on a simple four-player game from Appendix D in [1]

`rock_paper_scissors.ipynb` - analysis of dynamics of a rock-paper-scissors game

# References

[1] [The Mechanics of n−Player Differentiable Games](https://arxiv.org/pdf/1802.05642.pdf)
