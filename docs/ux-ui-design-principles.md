# USF UX/UI Design Principles

## Purpose
Create experiences that are useful, understandable, accessible, coherent, distinctive, and enjoyable. Industry conventions provide a reliable foundation; originality should improve the experience rather than make it unfamiliar for its own sake.

## 1. Start with people and outcomes
- Understand target users, their goals, context, skill levels, constraints, assistive technology, and environment.
- Separate observed evidence from assumptions. Do not invent user research or present personas as validated facts.
- Define the user problem and success measures before committing to visual concepts.
- Prioritize frequent, consequential, and frustrating tasks before decorative details.
- Include error recovery, onboarding, empty states, loading, offline/failure conditions, and destructive actions in the design.

## 2. Use established patterns deliberately
- Follow platform conventions and accessibility guidance for the chosen product form factor.
- Reuse familiar interaction patterns when they improve discoverability, predictability, accessibility, or task completion.
- Depart from convention only for a clear user benefit; explain the trade-off and validate the alternative.
- Do not blindly copy a competitor or apply a design system intended for a different platform.
- Use semantic structure, clear labels, consistent navigation, recognizable controls, and meaningful feedback.

## 3. Accessibility and inclusive design by default
- Treat accessibility as a requirement, not a polish phase.
- Design for keyboard and alternative input, screen readers, text scaling, sufficient contrast, reduced motion, focus visibility, and understandable errors.
- Do not convey status through color alone.
- Avoid inaccessible custom controls when native or proven accessible controls meet the need.
- Use WCAG 2.2 AA as a practical web baseline where applicable, plus the selected platform's own accessibility guidance and applicable legal requirements. WCAG is not a substitute for platform-specific testing.
- Test critical flows with assistive technology where practical; automated checks alone are insufficient.

## 4. Make visual design coherent and intentional
- Establish a small set of design principles and a clear visual hierarchy.
- Use design tokens for color, typography, spacing, radii, elevation, and motion where appropriate.
- Prefer consistent rhythm, readable typography, meaningful whitespace, and purposeful contrast over decoration.
- Make important actions, status, and next steps easy to find.
- Use imagery, illustration, animation, and visual effects only when they support comprehension, feedback, or product identity.
- Respect user settings and platform expectations for appearance and motion.

## 5. Innovate with purpose
- Begin with a dependable, usable baseline, then explore at least one genuinely differentiated concept for important user journeys when scope permits.
- Identify the intended benefit of each novel interaction: fewer steps, better understanding, greater confidence, more control, better creative expression, or a more memorable experience.
- Compare conventional and novel approaches; state who benefits, who might struggle, and what evidence would decide between them.
- Prefer progressive disclosure: keep common tasks clear and reveal advanced capabilities when relevant.
- Use prototypes to test interaction ideas before committing to expensive implementation.
- Do not equate novelty with quality. A visually striking design that obscures actions, breaks accessibility, or increases error rates is not an improvement.

## 6. Use evidence and iteration
- Combine available user research, product analytics, support feedback, usability tests, expert review, and technical constraints.
- When direct research is unavailable, label hypotheses and propose the cheapest useful validation.
- Test representative tasks with users or suitable proxies; observe completion, errors, hesitation, confidence, and comprehension.
- Use A/B tests only when appropriate and ethically designed; small qualitative tests may be more informative early on.
- Record findings and update designs. Do not treat stakeholder preference as user evidence.

## 7. Design the full state space
For every key screen or component, consider:
- default and alternate states;
- loading, empty, success, warning, and error states;
- disabled, permission-denied, and offline states where relevant;
- long content, localization, text scaling, and small/large windows or viewports;
- keyboard focus, hover, pressed, selected, and validation states;
- undo, cancellation, confirmation, and recovery from mistakes.

## 8. Collaborate with engineering, product, and security
- Work with the Product Manager to clarify goals, priorities, and acceptance criteria.
- Work with engineers early to assess feasibility, native platform behavior, responsiveness, performance, and maintainability.
- Work with accessibility and security reviewers on sensitive workflows, permission prompts, authentication, privacy choices, and error messaging.
- Minimize collection and display of personal data; do not expose secrets in UI, screenshots, analytics, or error messages.
- Make permissions and consequential actions understandable; avoid manipulative patterns, deceptive consent, or dark patterns.
- Document design decisions when they affect scope, platform behavior, architecture, or major user workflows.

## 9. Define success
Select project-specific measures. Possible measures include:
- task completion and time on task;
- error and abandonment rates;
- learnability and successful first use;
- user confidence and comprehension;
- accessibility findings and assistive-technology task success;
- satisfaction, retention, and support burden;
- performance and perceived responsiveness.

Set a baseline or explain when it is unavailable. Avoid optimizing a single metric in ways that harm user trust, accessibility, or long-term value.

## 10. Design deliverables
Deliver only the artifacts useful for the project, which may include:
- user research summary and assumptions;
- journeys, task flows, and information architecture;
- low- and high-fidelity prototypes;
- design principles and tokens;
- screen/component specifications and interaction states;
- accessibility notes;
- usability findings and changes made;
- design handoff and acceptance criteria.

## Decision rule
Use familiar patterns as the default when they serve users well. Innovate when there is a clear problem-specific opportunity, preserve accessibility and user control, and validate the new approach. The goal is not to choose between best practices and creativity, but to combine a dependable foundation with purposeful differentiation.
