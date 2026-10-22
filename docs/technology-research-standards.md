# Technology Research Standards

## Evidence hierarchy
Prefer, in order appropriate to the claim:
1. Official documentation, support/lifecycle policies, release notes, security advisories, license texts, and vendor pricing.
2. Standards bodies, package registries, repository issue/release history, and reputable independent benchmarks.
3. Independent technical evaluations and documented operational experience.
4. Community discussion as contextual evidence, not as the sole basis for consequential claims.

## Research hygiene
- Record URLs and the date each source was checked.
- Check versions and platform compatibility, not just product names.
- Distinguish vendor claims from independently verified results.
- Do not infer that a project is actively maintained from a popular package count or an old blog post.
- Do not claim a dependency is secure merely because no vulnerability was found in one search.
- Confirm licenses and obligations for the actual versions and transitive dependencies.
- Treat benchmark results as workload-specific; document setup and limitations.
- Cite the evidence for consequential factual claims in the TDR.
- If evidence is unavailable, record the gap and decide whether it is acceptable, needs stakeholder approval, or requires a proof of concept.

## Stack decision quality
A decision is complete when a future team can understand why the option was chosen, what was rejected, which assumptions mattered, what evidence supported the choice, and what would cause reconsideration. The most heavily scored option is not automatically the winner if it violates a hard constraint or creates an unacceptable risk.
