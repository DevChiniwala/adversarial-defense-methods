```bibtex
@inproceedings{anyattack_large_scale_self_supervised_2026,
  title={AnyAttack: Towards Large-scale Self-supervised Adversarial Attacks on Vision-language Models},
  author={Zheng, K. and Liu, M. and Zhang, X.},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2026}
}
```

## Motivation
* Traditional adversarial attacks on VLMs are limited by their reliance on specific target labels, severely hampering their scalability to large, open-world datasets.
* Evaluating the robustness of massive, web-scale multimodal models requires an attack framework capable of operating without manual label supervision.
* The transferability of targeted adversarial attacks from open-source to black-box commercial models like Gemini and GPT-4 has remained largely unquantified.
* There is a critical need for efficient noise generators that can be pre-trained on vast datasets to induce arbitrary desired outputs.

## Contribution
* Introduces "AnyAttack", the first framework adopting a self-supervised pre-training and fine-tuning paradigm for targeted multimodal adversarial attacks.
* Pre-trains a universal noise generator on the massive LAION-400M dataset, establishing a novel method where images act as their own supervision.
* Demonstrates highly effective zero-shot attack transferability to major commercial systems including Google Gemini, Claude Sonnet, and OpenAI GPT.
* Reveals a systemic, scalable vulnerability in state-of-the-art VLMs, achieving unprecedented attack success rates across diverse downstream tasks.

## Links
* [Link Not Yet Available]
* [Link Not Yet Available]
