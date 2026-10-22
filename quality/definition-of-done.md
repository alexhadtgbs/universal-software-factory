# Definition of Done

A story is complete only when applicable conditions are met:
- [ ] Linked requirement and acceptance criteria are clear.
- [ ] Implementation stays within approved scope.
- [ ] Relevant tests are added or updated.
- [ ] Relevant automated checks were run and results reported accurately.
- [ ] Security and privacy implications were considered.
- [ ] Error paths and edge cases are handled.
- [ ] Documentation is updated where necessary.
- [ ] Code review is complete according to project policy.
- [ ] Traceability links are updated.
- [ ] Remaining limitations and risks are disclosed.

A release is ready only when required stories meet their completion criteria, critical quality gates pass, and outstanding risks are explicitly accepted by an authorized human.


## Documentation and delivery evidence
- [ ] Work item, requirements, and acceptance criteria are traceable.
- [ ] Material decisions and rationale are recorded in relevant PDR/ADR/TDRs.
- [ ] PR/commit, review, test results, and CI run are linked.
- [ ] User, security, privacy, accessibility, and operational impacts are assessed as applicable.
- [ ] Documentation, configuration, and runbooks are updated in the same change.
- [ ] Known gaps and follow-up work have an owner and disposition.
- [ ] Release/deployment and recovery implications are documented.


## Product QA and documentation acceptance
- [ ] User-appropriate documentation is complete for this change and current product version.
- [ ] Documentation examples, commands, links, and UI references are validated where practical.
- [ ] Critical documented procedures have been independently followed in a clean/reset environment where practical.
- [ ] Documentation validation report is linked; untested steps are explicitly Blocked/Not Verified.
- [ ] Requirements, implementation, tests, and docs are traceable.
- [ ] QA findings are fixed or formally dispositioned under release policy.


## Agentic delivery loop (when used)
- [ ] The job's spec cites the requirement IDs and governing decisions it implements.
- [ ] `build.md` records evidence for every acceptance criterion; unverified criteria are marked Not Verified.
- [ ] All four review lenses (security, code/QA, UX/UI, documentation) passed in the final round.
- [ ] `decision.md` is APPROVE, or a human approval is recorded for an escalated job.
- [ ] `scripts/validate_job.py` passes for the job folder.
