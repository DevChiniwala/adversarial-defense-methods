```bibtex
@inproceedings{madry2018towards,
  title={Towards Deep Learning Models Resistant to Adversarial Attacks},
  author={Madry, Aleksander and Makelov, Aleksandar and Schmidt, Ludwig and Tsipras, Dimitris and Vladu, Adrian},
  booktitle={International Conference on Learning Representations},
  year={2018}
}
```

## Motivation
* While adversarial training showed promise, models were still vulnerable to stronger, iterative attacks.
* There was a lack of a theoretical framework connecting adversarial training with principled, robust optimization guarantees.
* The community needed a universal, first-order adversary to train against that could provide a reliable lower bound on model robustness.

## Contribution
* Framed adversarial robustness as a minimax optimization problem, providing a mathematically grounded approach to adversarial training.
* Introduced Projected Gradient Descent (PGD) as the "ultimate" first-order adversary, showing it is a universal attack method.
* Demonstrated that training networks against PGD attacks significantly improves resistance to a wide range of adversarial threats.

## Links
* [arXiv](https://arxiv.org/abs/1706.06083)
* [GitHub](https://github.com/MadryLab/mnist_challenge)
