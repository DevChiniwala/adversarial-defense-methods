```bibtex
@inproceedings{goodfellow2015explaining,
  title={Explaining and harnessing adversarial examples},
  author={Goodfellow, Ian J. and Shlens, Jonathon and Szegedy, Christian},
  booktitle={International Conference on Learning Representations},
  year={2015}
}
```

## Motivation
* Previous explanations for adversarial examples suggested they were caused by extreme non-linearity and overfitting in deep neural networks.
* Existing adversarial generation methods were computationally expensive, making it difficult to use them effectively during the training phase.

## Contribution
* Proposed the "Linearity Hypothesis," arguing that neural networks are vulnerable because they behave too linearly in high-dimensional spaces, not because they are overly non-linear.
* Introduced the Fast Gradient Sign Method (FGSM), a highly efficient, single-step method for generating adversarial examples using the gradient of the loss.
* Demonstrated that adversarial training using FGSM could serve as an effective regularizer, improving model robustness.

## Links
* [arXiv](https://arxiv.org/abs/1412.6572)
