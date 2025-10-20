Q1. 

- $\pi_1$: S₀ → a₁, S₁ → a₀, S₂ → a₀, S₃ → a₀  
- $\pi_2$: S₀ → a₂, S₁ → a₀, S₂ → a₀, S₃ → a₀

Q2.

$$
V_0 = R(S_0) + \max_a \gamma \sum_{S'} T(S_0, a, S') V(S')
$$


Q3.
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


Q4.


