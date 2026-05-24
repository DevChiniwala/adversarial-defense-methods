# 7. Adversarial Examples Improve Image Recognition (Xie et al., 2020)

## 🤔 Why You Must Read This Paper
Historically, adversarial training made models robust but caused a severe drop in standard accuracy (how well it predicts clean images). Xie and team challenged this assumption. This paper is fascinating because it turns adversarial examples from a 'threat' into a 'feature' that actually improves the model.

## 💡 What It Contributed to the Field
It introduced AdvProp, a training scheme that uses separate batch normalization layers for clean and adversarial images. This allowed adversarial examples to act as a powerful regularizer, actively improving the model's performance on clean data and achieving State-of-the-Art on ImageNet.

---
> *This summary is a humanized, educational analysis written to guide newcomers through the most foundational concepts in Adversarial Machine Learning without relying on copyrighted abstracts or academic jargon.*
