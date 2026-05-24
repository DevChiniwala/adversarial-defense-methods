# Explaining and Harnessing Adversarial Examples

**Authors:** Ian J. Goodfellow, Jonathon Shlens, Christian Szegedy
**Venue:** ICLR
**Year:** 2015
**Official Paper:** [arXiv:1412.6572](https://arxiv.org/abs/1412.6572)
**Official Code:** N/A (Foundational Algorithm)

## Why This Paper Matters
While Szegedy discovered the vulnerability, Ian Goodfellow provided the most elegant, widely accepted explanation for *why* it happens and introduced the absolute baseline attack that everyone learns first.

## Core Idea
Neural networks are actually too linear, not too non-linear. In high-dimensional spaces, a tiny perturbation across many input dimensions adds up linearly to cause a massive shift in the activation of the final layer. They introduced the Fast Gradient Sign Method (FGSM) to exploit this.

## What It Changed in the Field
It introduced FGSM, a computationally cheap and blazing-fast method to generate adversarial examples by taking a single step in the direction of the gradient. It also introduced the concept of 'adversarial training'.

## Limitations
FGSM is a single-step attack, meaning it is relatively weak compared to modern iterative attacks. Models defended solely against FGSM can easily be bypassed.

## Modern Impact
FGSM remains the 'Hello World' of adversarial attacks. Every new defense is still evaluated against it as a baseline sanity check.

## Recommended Before Reading
[Intriguing properties of neural networks](./intriguing_properties_szegedy.md)

## Recommended After Reading
[Towards Evaluating the Robustness of Neural Networks](./evaluating_robustness_cw.md)

---
> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
