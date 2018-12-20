# n-player-games

The project is inspired by new approach for tackling the problem of finding game equilibriums, presented in theThe Mechanics of n−Player Differentiable Games.  \newline

The authors have proposed a new algorithm to find stable fixed points (which undersome conditions can be considered Nash equilibrium) by introducing the notion of Hamiltonian games and inventing a new algorithm to find stable fixed points (which under some conditions can be considered Nash equilibrium).

The authors of $The\ Mechanics\ of\ n-Player\ Differentiable\ Games$ introduce the notion of Hamiltonian games to tackle the problem of finding game equilibriums. 

For a $n$-player game with parameter w, they define the Hessian of a game to be 
$$H(w) = \nabla_w \xi (w)^T $$

Since this is a matrix, it always admits a symmetric and anti-symmetric decomposition: 
$$H(w) = S(w) + A(w)$$ 

This leads to a classification: Hamiltonian games are defined as games where the symmetric component is zero, $S(w)$ = 0. Potential games are defined as games where the anti-symmetric component is zero, $A(w) = 0$. \newline 
One of the main theoretical contributions of this paper is that given an n-player Hamiltonian game with $H(w) = 1/2 \xi (w)^2$, under some conditions the gradient descent on H converges to a Nash equilibrium.

