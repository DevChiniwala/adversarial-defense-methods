# 4. Towards Deep Learning Models Resistant to Adversarial Attacks (Madry et al., 2017)

## 🤔 Why You Must Read This Paper
This is arguably the most important paper on *defending* neural networks. While FGSM was fast, it was too weak to train truly robust models. Madry formulated the adversarial robustness problem as a massive min-max optimization game. This is the blueprint for how modern robust AI is trained.

## 💡 What It Contributed to the Field
It introduced Projected Gradient Descent (PGD) as the 'ultimate' first-order adversary. The authors proved that training a model against PGD (PGD-Adversarial Training) was the most effective way to achieve empirical robustness. Even today, PGD-AT is the baseline against which all new defenses are measured.

---
> *This summary is a humanized, educational analysis written to guide newcomers through the most foundational concepts in Adversarial Machine Learning without relying on copyrighted abstracts or academic jargon.*
