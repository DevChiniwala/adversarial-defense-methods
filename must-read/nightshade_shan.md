# Nightshade: Prompt-Specific Poisoning Attacks on Text-to-Image Generative Models

**Authors:** Shawn Shan, Wenxin Ding, Josephine Passananti, Haitao Zheng, Ben Y. Zhao
**Venue:** IEEE S&P
**Year:** 2024
**Official Paper:** [arXiv:2310.13828](https://arxiv.org/abs/2310.13828)
**Official Code:** [Project Page](https://nightshade.cs.uchicago.edu/)

## Why This Paper Matters
As Generative AI exploded, artists were furious that their work was scraped for training data without consent. This paper flipped adversarial ML into an offensive weapon *for* the public to protect their copyright.

## Core Idea
Artists can invisibly alter the pixels of their digital art before uploading it to the web. When AI models scrape these 'poisoned' images, the adversarial perturbations map the visual features to a completely different concept (e.g., learning a 'dog' as a 'cat').

## What It Changed in the Field
It introduced highly effective data poisoning at the dataset-scraping level. It represented a huge shift in the ethical application of adversarial attacks—from 'breaking security' to 'enforcing copyright'.

## Limitations
The poisoning effect requires a critical mass of poisoned images to successfully corrupt a massive foundational model.

## Modern Impact
Nightshade (and its predecessor Glaze) became actual tools downloaded by millions of artists worldwide, bridging the gap between theoretical ML security and real-world legal/ethical battles.

## Recommended Before Reading
Basic understanding of Diffusion Models and Data Poisoning.

## Recommended After Reading
Literature on AI Copyright and Watermarking.

---
> **Educational Note:**
> This summary is an original educational interpretation written to help readers understand the historical importance and core contribution of the paper. Please refer to the official publication for the complete methodology and results.
