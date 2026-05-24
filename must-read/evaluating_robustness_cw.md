# Towards Evaluating the Robustness of Neural Networks

**Authors:** Nicholas Carlini, David Wagner
**Venue:** IEEE S&P
**Year:** 2017
**Official Paper:** [arXiv:1608.04644](https://arxiv.org/abs/1608.04644)
**Official Code:** [GitHub](https://github.com/carlini/nn_robust_attacks)

---

## Why This Paper Matters
In 2016, researchers proposed dozens of 'defenses' (like defensive distillation) claiming to solve adversarial attacks. Carlini and Wagner stepped in and completely dismantled almost all of them, setting a new standard for evaluation.

## Core Idea
Instead of relying on cross-entropy loss, C&W reformulates the attack as an optimization problem over a margin-based objective function (the logit differences), minimizing the L2, L0, or L-infinity distance of the perturbation.

## What It Changed in the Field
It introduced the C&W attack, an optimization-based attack that is mathematically elegant and incredibly powerful. For years, the C&W attack stood as the gold-standard benchmark.

## Key Takeaway
The biggest lesson from this paper is that robustness cannot be evaluated using weak attacks alone; a defense must survive rigorous, optimization-based adversaries to be considered valid.

## Limitations
The attack is an iterative optimization process, making it very slow to compute compared to fast gradient-based methods.

## Modern Impact
The paper established the rigorous methodology required to evaluate new defenses. To this day, if a defense is broken, it is usually because the authors failed to run a strong enough attack like C&W.

## Recommended Before Reading
[Explaining and Harnessing Adversarial Examples](./explaining_and_harnessing_goodfellow.md)

## Recommended After Reading
[Obfuscated Gradients Give a False Sense of Security](./obfuscated_gradients_athalye.md)

---

> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
