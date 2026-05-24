# Obfuscated Gradients Give a False Sense of Security

**Authors:** Anish Athalye, Nicholas Carlini, David Wagner
**Venue:** ICML
**Year:** 2018
**Official Paper:** [arXiv:1802.00420](https://arxiv.org/abs/1802.00420)
**Official Code:** [GitHub](https://github.com/anishathalye/obfuscated-gradients)

---

## Why This Paper Matters
This paper reads like a detective story. Athalye and his colleagues analyzed a slew of new defenses accepted at ICLR 2018 and realized they were all cheating (unintentionally) by breaking the math that gradient-based attacks rely on.

## Core Idea
Many proposed defenses (like input transformations or stochastic layers) don't make the model robust; they simply 'obfuscate' the gradient, preventing gradient-descent attacks from finding the adversarial examples. The authors introduced Backward Pass Differentiable Approximation (BPDA) to bypass this.

## What It Changed in the Field
It completely devastated the 2018 landscape of empirical defenses by bypassing 7 out of 9 ICLR defenses. It taught the community that breaking the attacker's tools doesn't mean your model is secure.

## Key Takeaway
Hiding or breaking gradients does not provide actual security; a true defense must withstand adaptive attackers who know how the defense operates.

## Limitations
The paper focuses on evaluating empirical defenses rather than proposing a new defense itself.

## Modern Impact
It established 'Adaptive Attacks' as a mandatory requirement for any security paper. You can no longer publish a defense without proving you haven't simply obfuscated the gradients.

## Recommended Before Reading
[Towards Evaluating the Robustness of Neural Networks](./evaluating_robustness_cw.md)

## Recommended After Reading
[Certified Adversarial Robustness via Randomized Smoothing](./randomized_smoothing_cohen.md)

---

> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
