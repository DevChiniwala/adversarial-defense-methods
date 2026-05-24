# 2. Explaining and Harnessing Adversarial Examples (Goodfellow et al., 2014)

## 🤔 Why You Must Read This Paper
While Szegedy discovered the vulnerability, Ian Goodfellow provided the most elegant, widely accepted explanation for *why* it happens. He argued that neural networks are actually too linear, not too non-linear. This paper is essential reading because it introduces the absolute baseline attack that everyone learns first: the Fast Gradient Sign Method (FGSM).

## 💡 What It Contributed to the Field
It introduced FGSM, a computationally cheap and blazing-fast method to generate adversarial examples by taking a single step in the direction of the gradient. It also introduced the concept of 'adversarial training'—feeding these adversarial examples back into the training data to make the model stronger.

---
> *This summary is a humanized, educational analysis written to guide newcomers through the most foundational concepts in Adversarial Machine Learning without relying on copyrighted abstracts or academic jargon.*
