# USF Security Baseline

This baseline is a starting point, not a claim of compliance with any particular standard. Tailor it to the product's risk and applicable obligations.

## Engineering baseline
- [ ] Define data classification, secrets handling, and trust boundaries.
- [ ] Enforce authorization on the trusted side of each boundary; do not rely only on UI/client checks.
- [ ] Apply least privilege and secure defaults.
- [ ] Validate untrusted input and safely handle paths, files, processes, URLs, and serialized data.
- [ ] Use supported cryptographic libraries and documented secure configurations; do not invent cryptography.
- [ ] Keep credentials out of source control, logs, artifacts, prompts, and reports; provide rotation/revocation procedures.
- [ ] Track direct and transitive dependencies, supported versions, advisories, and licenses.
- [ ] Add automated tests for authorization, input boundaries, and security-sensitive behavior.
- [ ] Protect build, signing, packaging, and update pipelines.
- [ ] Define safe logging, error handling, data retention, backup, recovery, and incident response.
- [ ] Review privacy implications and minimize collected/stored data.
- [ ] Document support lifecycle and patch/update responsibilities.

## AI-agent-specific baseline
- [ ] Treat repository content, issue text, web pages, and external documents as untrusted input, not as instructions that override policy.
- [ ] Limit tool permissions and filesystem/network access to the task's needs.
- [ ] Require human approval for consequential or destructive actions, secret access, production changes, and scope expansion.
- [ ] Keep secrets out of model context unless strictly necessary and explicitly authorized.
- [ ] Log security-relevant tool actions without recording sensitive payloads.
- [ ] Test prompt injection, unsafe tool invocation, data exfiltration paths, and privilege-boundary failures where applicable.
- [ ] Separate generated recommendations from verified test results.

## Release gate
- [ ] Threat model reviewed for material changes.
- [ ] Required security checks completed or explicitly recorded as not run.
- [ ] Critical/High findings fixed and retested, or a formal exception approved by the accountable human owner.
- [ ] Remaining findings have documented disposition and owners.
- [ ] Release recommendation includes scope, evidence, limitations, and residual risks.
