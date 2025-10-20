Q1. 

- $\pi_1$: S₀ → a₁, S₁ → a₀, S₂ → a₀, S₃ → a₀  
- $\pi_2$: S₀ → a₂, S₁ → a₀, S₂ → a₀, S₃ → a₀

Q2.

White the equation for each  optimal value  for each state \(V^*(s)\) for each state \(\{S0,S1,S2,S3\}\)

General form:
\[
V^*(s)= R(s) + \max_a \gamma \sum_{s'} T(s,a,s')\,V^*(s').
\]

---

## Rewards
- \(R(S3)=10\)  
- \(R(S2)=1\)  
- \(R(S0)=R(S1)=0\)

---

## Transition summary

**Action \(a_0\)**  
- From \(S1\): \(S1 \to S1\) with \(1-x\), and \(S1 \to S3\) with \(x\)  
- From \(S2\): \(S2 \to S0\) with \(1-y\), and \(S2 \to S3\) with \(y\)  
- From \(S3\): \(S3 \to S0\) with prob. \(1\)  
- From \(S0\): null row

**Action \(a_1\)**  
- From \(S0\): \(S0 \to S1\) with prob. \(1\)  

**Action \(a_2\)**  
- From \(S0\): \(S0 \to S2\) with prob. \(1\)  
---
## Optimal equations per state

### 1) State \(S0\)
Usable actions:
- \(a_1:\; S0\to S1\)  
- \(a_2:\; S0\to S2\) 
- \(a_0:\) null row

\[
\boxed{V^*(S0)= \max\{\gamma V^*(S1),\;\gamma V^*(S2),\;0\}}
\]
---

### 2) State \(S1\)
Only \(a_0\) has transitions; \(a_1\) and \(a_2\) are null at \(S1\).
\[
\boxed{V^*(S1)= \max\big\{\gamma\big[(1-x)\,V^*(S1)+x\,V^*(S3)\big],\;0,\;0\big\}}
\]

---

### 3) State \(S2\)
- \(a_0:\; (1-y)\) to \(S0\) and \(y\) to \(S3\)  
- \(a_1, a_2:\) null rows  
Since \(R(S2)=1\):
\[
\boxed{V^*(S2)= \max\Big\{1+\gamma\big[(1-y)\,V^*(S0)+y\,V^*(S3)\big],\;1,\;1\Big\}}
\]

---

### 4) State \(S3\)
- \(a_0:\; S3\to S0\) deterministically  
- \(a_1, a_2:\) null rows  
Since \(R(S3)=10\):
\[
\boxed{V^*(S3)= \max\{10+\gamma V^*(S0),\;10,\;10\}}
\]

---

## Answers
```
V*(S0) = max{ γ V*(S1), γ V*(S2), 0 }
V*(S1) = max{ γ[(1−x) V*(S1) + x V*(S3)], 0, 0 }
V*(S2) = max{ 1 + γ[(1−y) V*(S0) + y V*(S3)], 1, 1 }
V*(S3) = max{ 10 + γ V*(S0), 10, 10 }
```


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


