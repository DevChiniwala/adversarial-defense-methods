# 6. Certified Adversarial Robustness via Randomized Smoothing (Cohen et al., 2019)

## 🤔 Why You Must Read This Paper
For years, the field was stuck in an arms race: an attack is published, a defense beats it, a stronger attack beats the defense. People wanted *guarantees*. This paper is a must-read because it shows how to mathematically prove that a model cannot be fooled within a certain radius, breaking the endless cycle.

## 💡 What It Contributed to the Field
It popularized 'Randomized Smoothing' at scale. By injecting Gaussian noise during inference and taking a majority vote, they were able to provide tight, provable robustness guarantees for massive architectures like ResNet on ImageNet, which was previously thought to be computationally impossible.

---
> *This summary is a humanized, educational analysis written to guide newcomers through the most foundational concepts in Adversarial Machine Learning without relying on copyrighted abstracts or academic jargon.*
