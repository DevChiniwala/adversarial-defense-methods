# Certified Adversarial Robustness via Randomized Smoothing

**Authors:** Jeremy M. Cohen, Elan Rosenfeld, J. Zico Kolter
**Venue:** ICML
**Year:** 2019
**Official Paper:** [arXiv:1902.02915](https://arxiv.org/abs/1902.02915)
**Official Code:** [GitHub](https://github.com/locuslab/smoothing)

---

## Why This Paper Matters
For years, the field was stuck in an endless cat-and-mouse game between empirical attacks and empirical defenses. This paper provided a breakthrough, showing how to mathematically prove that a model cannot be fooled within a certain radius.

## Core Idea
By taking a base classifier and creating a 'smoothed' classifier (which outputs the majority vote of the base classifier under Gaussian noise), one can mathematically guarantee an L2 robustness radius around the input.

## What It Changed in the Field
It popularized 'Randomized Smoothing' at scale. It allowed for tight, provable robustness guarantees on massive architectures like ResNet on ImageNet, which was previously thought to be computationally impossible.

## Key Takeaway
We can escape the endless cycle of attacks and defenses by shifting from empirical testing to mathematical certification.

## Limitations
Randomized smoothing significantly degrades the 'clean' accuracy of the model, and inference becomes very slow because it requires hundreds of forward passes (Monte Carlo sampling) for a single image.

## Modern Impact
It spawned an entire sub-field of Certified Robustness. It remains the only viable method for certifying deep networks on high-dimensional datasets like ImageNet.

## Recommended Before Reading
[Obfuscated Gradients Give a False Sense of Security](./obfuscated_gradients_athalye.md)

## Recommended After Reading
Any modern Certified Robustness paper.

---

> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
