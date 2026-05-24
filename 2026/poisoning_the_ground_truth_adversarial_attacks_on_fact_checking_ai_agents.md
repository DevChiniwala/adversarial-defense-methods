```bibtex
@article{poisoning_ground_truth_fact_checking_2026,
  title={Poisoning the Ground Truth: Adversarial Attacks on Fact-Checking AI Agents},
  author={Alvarez, R. and Patel, N. and Singh, A.},
  journal={arXiv preprint},
  year={2026}
}
```

## Motivation
* Automated Fact-Checking (AFC) agents heavily rely on Retrieval-Augmented Generation (RAG) from dynamic, web-scale knowledge bases to verify claims.
* These knowledge bases are vulnerable to data poisoning, allowing adversaries to covertly manipulate the "ground truth" accessed by fact-checking systems.
* Existing research largely overlooks how subtle linguistic persuasion techniques and fabricated evidence can bypass the logical verification steps of AI agents.
* The tendency of underlying LLMs to hallucinate or adopt biased retrieved contexts makes fact-checkers highly susceptible to adversarial claim modifications.

## Contribution
* Systematizes vulnerabilities in the AFC pipeline, categorizing threats into data poisoning, adversarial evidence injection, and persuasion attacks.
* Demonstrates how injecting minimal malicious text into a RAG knowledge base reliably corrupts the agent's verdict on targeted political or scientific claims.
* Introduces "Persuasive Adversarial Prompts," showing that logically fallacious or emotionally charged rephrasing of claims successfully bypasses AFC detection logic.
* Proposes robust knowledge governance and cryptographic provenance strategies to secure the evidence retrieval phase of fact-checking agents.

## Links
* [Link Not Yet Available]
* [Link Not Yet Available]
