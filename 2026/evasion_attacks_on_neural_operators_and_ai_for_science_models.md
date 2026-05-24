```bibtex
@article{evasion_attacks_neural_operators_2026,
  title={Evasion Attacks on Neural Operators and AI for Science Models},
  author={Kim, S. and Nguyen, T. and O'Connor, M.},
  journal={Nature Machine Intelligence},
  year={2026}
}
```

## Motivation
* Neural Operators and Physics-Informed Neural Networks (PINNs) are rapidly being deployed in safety-critical scientific domains like grid management and nuclear digital twins.
* Despite their precision on clean data, the vulnerability of these continuous field models to adversarial manipulation remains critically underexplored compared to image classifiers.
* Standard anomaly detection and z-score filters fail to identify sparse, physics-aware perturbations that masquerade as natural environmental variations.
* A lack of robust defensive architectures leaves scientific AI susceptible to catastrophic, undetectable prediction failures induced by minimal input noise.

## Contribution
* Reveals the extreme sparsity vulnerability of neural operators, demonstrating that perturbing <1% of input points can spike L2 prediction errors to 60%.
* Formulates a novel class of "physics-aware" gradient-free evasion attacks (via differential evolution) that bypass standard validation boundaries.
* Identifies "sensitivity concentration" in specific boundary conditions as the primary architectural flaw enabling these continuous field-level exploits.
* Proposes Structure-Preserving PINNs (SP-PINNs) that embed physical energy stability constraints directly into the loss landscape to mitigate adversarial noise.

## Links
* [Link Not Yet Available]
* [Link Not Yet Available]
