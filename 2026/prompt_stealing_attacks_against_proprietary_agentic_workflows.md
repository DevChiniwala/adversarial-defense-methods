```bibtex
@inproceedings{prompt_stealing_agentic_workflows_2026,
  title={Prompt-Stealing Attacks against Proprietary Agentic Workflows},
  author={Fischer, B. and Nakamura, K. and Silva, J.},
  booktitle={Proceedings of the ACM Conference on Computer and Communications Security (CCS)},
  year={2026}
}
```

## Motivation
* Multi-agent workflows heavily depend on proprietary system prompts and implicit inter-agent trust to manage complex tasks and API access.
* Indirect prompt injection—where malicious instructions are embedded in external documents—can exploit this trust to manipulate downstream, highly privileged agents.
* The resulting propagation of malicious payloads allows attackers to silently exfiltrate highly confidential internal logic, system configurations, and API keys.
* Traditional data-layer access controls are frequently bypassed due to the blurred boundary between trusted system instructions and untrusted user input within the LLM context.

## Contribution
* Exposes how implicitly trusted multi-agent pipelines facilitate severe prompt-stealing and configuration leakage via indirect input injections.
* Demonstrates successful exfiltration attacks across simulated proprietary workflows, achieving a 95% success rate in capturing hidden system directives.
* Introduces the concept of "Semantic Gatekeepers" and cryptographic prompt provenance to verify instruction origin and prevent payload propagation.
* Proposes a defense-in-depth architecture that enforces strict data-layer input sanitization and isolates privileged agents from raw external inputs.

## Links
* [Link Not Yet Available]
* [Link Not Yet Available]
