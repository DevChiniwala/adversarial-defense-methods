```bibtex
@inproceedings{carlini2017towards,
  title={Towards Evaluating the Robustness of Neural Networks},
  author={Carlini, Nicholas and Wagner, David},
  booktitle={IEEE Symposium on Security and Privacy (S\&P)},
  year={2017}
}
```

## Motivation
* Defensive distillation and other early defense mechanisms claimed to provide robustness against adversarial attacks like FGSM and L-BFGS.
* Existing attacks were often failing because of gradient masking or suboptimal optimization techniques rather than true model robustness.
* The field lacked a rigorous attack framework to genuinely evaluate whether a defense was effective or just hiding its gradients.

## Contribution
* Introduced the Carlini & Wagner (C&W) attack, a powerful optimization-based white-box attack using three different distance metrics (L0, L2, L∞).
* Completely broke defensive distillation and demonstrated that gradient masking is insufficient for true security.
* Established a new gold standard for evaluating the robustness of adversarial defenses that remains highly relevant today.

## Links
* [arXiv](https://arxiv.org/abs/1608.04644)
* [GitHub](https://github.com/carlini/nn_robust_attacks)
