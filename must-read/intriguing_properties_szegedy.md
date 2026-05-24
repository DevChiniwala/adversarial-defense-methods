# Intriguing properties of neural networks

**Authors:** Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan, Ian Goodfellow, Rob Fergus
**Venue:** ICLR
**Year:** 2014
**Official Paper:** [arXiv:1312.6199](https://arxiv.org/abs/1312.6199)
**Official Code:** N/A (Conceptual Discovery)

---

## Why This Paper Matters
This is the 'Big Bang' paper of Adversarial Machine Learning. Before this, the community largely believed deep neural networks were robust feature extractors. Szegedy and his team shocked the world by demonstrating that you could apply an imperceptible, carefully calculated layer of noise to an image, and the most advanced neural networks would confidently misclassify it.

## Core Idea
Neural networks learn input-output mappings that are discontinuous. By solving a targeted optimization problem (L-BFGS), one can find a visually imperceptible perturbation that forces the network to misclassify an image as a specific target class.

## What It Changed in the Field
It fundamentally proved the existence of 'adversarial examples' in modern deep learning, shattering the illusion that high accuracy on test sets equated to true semantic understanding of images.

## Key Takeaway
The biggest lesson from this paper is that high model accuracy on clean data does not equal true conceptual understanding; deep models have massive, exploitable blind spots.

## Limitations
The attack method (L-BFGS optimization) was incredibly slow and computationally expensive, making real-time or large-scale attacks difficult.

## Modern Impact
This paper single-handedly birthed the entire field of adversarial robustness, spawning thousands of subsequent papers trying to explain or fix the vulnerability.

## Recommended Before Reading
Basic understanding of Convolutional Neural Networks (CNNs).

## Recommended After Reading
[Explaining and Harnessing Adversarial Examples](./explaining_and_harnessing_goodfellow.md)

---

> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
