```bibtex
@inproceedings{hypnotic_jailbreaks_contextual_overloading_2026,
  title={Hypnotic Jailbreaks: Bypassing Advanced LLM Defenses via Contextual Overloading},
  author={Carter, E. and Simmons, B. and Davis, M.},
  booktitle={Proceedings of the Network and Distributed System Security Symposium (NDSS)},
  year={2026}
}
```

## Motivation
* State-of-the-art LLM defenses rely heavily on semantic filtering, boundary alignment, and intent recognition, which have proven brittle against highly complex prompts.
* Adversaries are increasingly shifting from overt command injections to sophisticated narrative and structural exploits that obscure malicious intent.
* Context windows in modern LLMs have expanded massively, but this increased capacity creates a vulnerability where excessive benign context can overshadow security guardrails.
* "Hypnotic" or cognitive-style prompt engineering methods bypass simple keyword blocking by mimicking benign, complex human reasoning.

## Contribution
* Discovers and defines "Contextual Overloading," a novel class of jailbreak attacks that exploits large context windows to induce "attentional drift" away from safety prompts.
* Proposes the "Hypnotic Jailbreak" methodology, embedding malicious payloads deep within multi-layered, highly logical narratives that bypass semantic gatekeepers.
* Empirically demonstrates a near 90% success rate against advanced alignment mechanisms across leading proprietary models (e.g., GPT-4, Claude).
* Suggests a new defensive paradigm utilizing dynamic attention-steering to anchor safety constraints regardless of prompt length or complexity.

## Links
* [Link Not Yet Available]
* [Link Not Yet Available]
