Group:
Davy Araujo Sa Teles
Nuno Kuschnaroff Barbosa

## Q1.

- $\pi_1$: S₀ → a₁, S₁ → a₀, S₂ → a₀, S₃ → a₀  
- $\pi_2$: S₀ → a₂, S₁ → a₀, S₂ → a₀, S₃ → a₀

## Q2.

Given the equation for each  optimal value  for each state 

$$
V(s) = R(s) + \max_a \ \gamma \sum_{s'} T(s, a, s') \ V(s')
$$

Applied for each state:


$$
V(S_0) = γ \max_a [V(S1), V(S2)]
$$

$$
V(S_1) = γ((1−x) V(S_1) + x V(S_3))
$$

$$
V(S_2) = 1 + γ((1−y) V(S_0) + y V(S_3))
$$

$$
V(S_3) = 10 + γ V(S_0)
$$


## Q3.
The equation for the policy at state \(S_0\) is: 
$$
\pi (S_0) = argmax_a \sum_{S'} T(S_0, a, S') V(S') 
$$

if $\pi (S_0) = a2$:

$$
\sum_{S'} T(S_0, a2, S') V(S') > \sum_{S'} T(S_0, a1, S') V(S')
$$

$$
T(S_0, a2, S_2) V(S_2) > T(S_0, a1, S_1) V(S_1)
$$

Since $T(S_0, a2, S_2) = T(S_0, a1, S_1) = 1$:

$$
V(S_2) > V(S_1)
$$

Assuming x=0:

$$
V(S_1) = \gamma ((1-x) V(S_1) + x V(S_3)
$$

$$
V(S_1) = \gamma V(S_1)
$$

For this to be true for all $\gamma \in [0,1)$, 

$$
V(S_1) = 0
$$

Since 

$$
V(S_2) = R(S_2) + \gamma (yV(S_0) + (1-y)V(S_3))
$$

and, for all $\gamma \in [0,1)$ and $y \in[0,1]$, 

$$
R(S_2)\geq1
$$

So for $x=0$, $V(S_2) > V(S_1)$ and $\pi (S_0) = a2$.

## Q4.

Using the same logic as in question 3, for $\pi (S_0) = a1$:

$$
V(S_1) > V(S_2)
$$

For all $\gamma \in [0,1)$ and $x > 0$, $V(S_1)$ will only be 0 if both $V(S_1)$ and $V(S_3)$ are 0. But because 

$$
V(S_3) = 10 + \gamma V(S_0)
$$

and since there is no negative rewards, it isn't possible for $V(S_3)$ = 0, and consequently is also impossible for $V(S_1)$ to be 0 for all $\gamma \in [0,1)$.

So to respect $V(S_1) > V(S_2)$ it is necesasry that $V(S_2) = 0$. Since $R(S_2) = 1$ and V(S_0) and V(S_3) > 0, V(S2) > 1. So there is no value for y, that for all $x>0$ and $\gamma \in [0,1)$, $\pi (S_0) = a1$.


