```bibtex
@article{dds_adversarial_attack_methodologies_2026,
  title={Denoising Diffusion Sampling (DDS): Adversarial Attack Methodologies in Generative Audio-Video},
  author={Cohen, A. and Yamamoto, H. and Meier, F.},
  journal={arXiv preprint},
  year={2026}
}
```

## Motivation
* Generative diffusion models have become the standard for high-fidelity text-to-video (T2V) and audio generation, but their adversarial vulnerabilities are largely unexplored.
* The reverse-time Denoising Diffusion Sampling (DDS) process can be hijacked to create highly stealthy and transferable adversarial perturbations.
* In temporal media (video and audio), attackers can disrupt semantic alignment and temporal consistency, severely degrading the output quality without obvious input noise.
* While diffusion models are heavily utilized for adversarial purification (defense), adaptive attackers leveraging the very same sampling mechanics can bypass these defenses entirely.

## Contribution
* Explores novel adversarial attack methodologies targeting the DDS pipeline, focusing on text-to-video and audio-generative domains.
* Introduces targeted semantic/temporal attacks (e.g., T2VAttack frameworks) that use greedy search to insert optimized perturbations, disrupting generative fidelity.
* Develops "Codebook-based" adversarial generation, utilizing predefined noise codebooks rather than additive noise to ensure extreme stealth and high transferability.
* Critically evaluates the robustness of diffusion-based purification defenses (like AudioPure) against sophisticated, white-box adaptive attacks.

## Links
* [Link Not Yet Available]
* [Link Not Yet Available]
