```bibtex
@inproceedings{szegedy2014intriguing,
  title={Intriguing properties of neural networks},
  author={Szegedy, Christian and Zaremba, Wojciech and Sutskever, Ilya and Bruna, Joan and Erhan, Dumitru and Goodfellow, Ian J. and Fergus, Rob},
  booktitle={International Conference on Learning Representations},
  year={2014}
}
```

## Motivation
* Deep neural networks were achieving state-of-the-art results, but their high expressiveness made them uninterpretable and prone to counter-intuitive properties.
* It was widely believed that small perturbations to an input image should not change the model's prediction, given the data distribution.
* The researchers wanted to investigate the semantic meaning of individual neurons and the stability of neural networks against visually imperceptible input changes.

## Contribution
* Discovered that networks are highly vulnerable to adversarial examples—imperceptible, non-random perturbations that cause arbitrary misclassification.
* Demonstrated that these adversarial examples generalize across different neural network architectures and disjoint training sets.
* Showed that it is the entire space of activations, rather than individual high-level units, that contains semantic information.

## Links
* [arXiv](https://arxiv.org/abs/1312.6199)
