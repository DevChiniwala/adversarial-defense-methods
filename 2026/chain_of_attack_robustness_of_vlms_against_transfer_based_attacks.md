```bibtex
@article{chain_of_attack_vlms_2026,
  title={Chain of Attack: Robustness of VLMs Against Transfer-Based Attacks},
  author={Wu, Z. and Lin, T. and Zhao, Y.},
  journal={arXiv preprint},
  year={2026}
}
```

## Motivation
* Current evaluations of VLM robustness primarily focus on single-step, isolated gradient-based perturbations that fail to capture real-world adversarial complexity.
* Transfer-based attacks, where an adversarial image crafted on a surrogate model compromises a black-box target, remain highly successful and difficult to defend.
* Pixel-level modifications can silently deceive autonomous agents (e.g., shopping bots) into misinterpreting their visual environment, leading to critical action failures.
* Existing metrics fail to accurately assess the semantic degradation caused by step-by-step adversarial updates in multimodal contexts.

## Contribution
* Introduces the "Chain of Attack" (CoA) framework, employing a step-by-step semantic update of multimodal embeddings to craft highly potent adversarial images.
* Demonstrates that iteratively aligning image noise with target captions significantly enhances attack transferability across distinct VLM families.
* Develops a novel LLM-based evaluation metric to precisely quantify the success and semantic impact of transfer-based multimodal attacks.
* Reveals stark architectural differences in differential robustness, offering key insights for designing the next generation of secure VLM architectures.

## Links
* [Link Not Yet Available]
* [Link Not Yet Available]
