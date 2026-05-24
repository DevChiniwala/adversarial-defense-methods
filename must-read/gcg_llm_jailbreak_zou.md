# Universal and Transferable Adversarial Attacks on Aligned Language Models

**Authors:** Andy Zou, Zifan Wang, J. Zico Kolter, Matt Fredrikson
**Venue:** NeurIPS
**Year:** 2023
**Official Paper:** [arXiv:2307.15043](https://arxiv.org/abs/2307.15043)
**Official Code:** [GitHub](https://github.com/llm-attacks/llm-attacks)

---

## Why This Paper Matters
This is the paper that brought adversarial attacks from the computer vision era into the ChatGPT era. It proved that LLMs suffer from the exact same fundamental, mathematical vulnerabilities as image classifiers.

## Core Idea
By optimizing a discrete string of tokens using gradients (Greedy Coordinate Gradient - GCG), attackers can append a universal suffix to any malicious prompt, forcing the LLM to start its response affirmatively (e.g., 'Sure, here is how to build a bomb').

## What It Changed in the Field
It bypassed the alignment (RLHF) of top models like Llama-2, ChatGPT, and Claude. It proved that manual 'prompt engineering' was obsolete compared to automated adversarial optimization.

## Key Takeaway
Large Language Models, despite their generative nature, are fundamentally neural networks and are completely susceptible to mathematical, gradient-based adversarial optimization.

## Limitations
The GCG optimization process requires white-box access to a model to compute gradients, though the resulting strings are highly transferable to black-box commercial models.

## Modern Impact
It sparked the massive 2024-2025 wave of LLM Red Teaming and Alignment research, forcing AI labs to completely rethink how they defend foundation models.

## Recommended Before Reading
[Towards Evaluating the Robustness of Neural Networks](./evaluating_robustness_cw.md)

## Recommended After Reading
[Systematization of Agentic LLM Defenses](./agentic_llm_defenses_2026.md)

---

> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
