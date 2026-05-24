```bibtex
@inproceedings{xie2020adversarial,
  title={Adversarial Examples Improve Image Recognition},
  author={Xie, Cihang and Tan, Mingxing and Gong, Boqing and Wang, Jiang and Yuille, Alan L. and Le, Quoc V.},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2020}
}
```

## Motivation
* Adversarial training was historically viewed purely as a defense mechanism, often resulting in a trade-off where clean accuracy degraded.
* Researchers wanted to see if the robust features learned from adversarial examples could actually be harnessed to improve standard model performance rather than hurt it.

## Contribution
* Introduced AdvProp, an enhanced adversarial training scheme that treats adversarial examples as additional data to prevent overfitting.
* Utilized auxiliary batch normalization networks specifically for adversarial examples to prevent them from degrading the clean image distributions.
* Achieved state-of-the-art results on ImageNet, proving that adversarial examples can boost clean accuracy when properly isolated during training.

## Links
* [arXiv](https://arxiv.org/abs/1911.09665)
* [GitHub](https://github.com/cihangxie/AdvProp)
