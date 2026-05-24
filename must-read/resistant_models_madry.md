# Towards Deep Learning Models Resistant to Adversarial Attacks

**Authors:** Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, Adrian Vladu
**Venue:** ICLR
**Year:** 2018
**Official Paper:** [arXiv:1706.06083](https://arxiv.org/abs/1706.06083)
**Official Code:** [GitHub](https://github.com/MadryLab/mnist_challenge)

## Why This Paper Matters
This is arguably the most important paper on *defending* neural networks. It formulated the adversarial robustness problem as a massive min-max optimization game, providing the blueprint for how modern robust AI is trained.

## Core Idea
Robust training is a min-max game: the inner maximization finds the strongest adversarial example (using Projected Gradient Descent - PGD), and the outer minimization updates the model weights to correctly classify that example.

## What It Changed in the Field
It introduced PGD as the 'ultimate' first-order adversary. It proved that training a model against PGD (PGD-Adversarial Training) was the most effective way to achieve empirical robustness.

## Limitations
Adversarial training using PGD is immensely computationally expensive, often taking 3-10 times longer than standard training.

## Modern Impact
PGD-AT is still the fundamental baseline against which all new empirical defenses are measured. It fundamentally shifted the focus from 'obscure math tricks' to 'brute-force robust optimization'.

## Recommended Before Reading
[Explaining and Harnessing Adversarial Examples](./explaining_and_harnessing_goodfellow.md)

## Recommended After Reading
[Certified Adversarial Robustness via Randomized Smoothing](./randomized_smoothing_cohen.md)

---
> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
