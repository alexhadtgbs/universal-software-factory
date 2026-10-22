# Workflow: UX/UI Design and Validation

## Purpose
Create a coherent, accessible, and differentiated user experience grounded in user needs and platform conventions.

## Inputs
- Product brief, PRD, user groups, jobs-to-be-done, and success measures
- Product form-factor decision and platform constraints
- Brand/product context, design system if any, accessibility and privacy requirements
- Engineering constraints and security-sensitive workflows

## 1. Understand before designing
- Clarify target users, context of use, primary tasks, pain points, and desired outcomes.
- Review existing research, analytics, support feedback, and comparable interaction patterns where relevant.
- Distinguish verified evidence, stakeholder assumptions, and open questions.
- If evidence is thin, propose low-cost research or mark assumptions for validation.

## 2. Define the experience
- Map the highest-value user journeys and critical task flows.
- Define information architecture, navigation, content hierarchy, and primary actions.
- Identify critical, frequent, and high-risk interactions.
- Set measurable usability and accessibility acceptance criteria.
- Establish design principles and product personality before detailed visual styling.

## 3. Establish the dependable baseline
- Follow the chosen platform's conventions and applicable accessibility guidance.
- Reuse a coherent design system or create a minimal one with tokens and reusable components.
- Specify semantics, labels, focus order, keyboard behavior, feedback, error handling, and recovery.
- Cover empty, loading, success, warning, error, permission-denied, and offline states where relevant.

## 4. Explore purposeful innovation
- Generate at least one alternative concept for a high-value journey when scope permits.
- For each novel element, document the user problem it solves, expected benefit, risks, accessibility impact, and implementation cost.
- Prefer progressive disclosure and user control over complexity, surprise, or hidden gestures.
- Do not invent unconventional controls solely to make the UI look different.
- Prototype the promising concept and compare it with the conventional baseline.

## 5. Validate with evidence
- Run task-based usability checks on representative workflows.
- Include keyboard and assistive-technology checks for critical flows where practical.
- Test readability, contrast, text scaling, focus, feedback, and recovery from mistakes.
- Record task success, confusion, errors, user confidence, and unresolved issues.
- Use automated accessibility tools as one input, not as the sole accessibility sign-off.

## 6. Iterate and hand off
- Update the design based on findings and record meaningful changes.
- Provide engineering-ready specifications for components, states, responsive behavior, content, motion, and accessibility.
- Collaborate with engineers on feasibility and with Security/Privacy reviewers on sensitive interactions.
- Link designs and acceptance criteria to PRD requirements and implementation tasks.

## 7. Review after implementation
- Compare the implemented experience with the approved design and acceptance criteria.
- Test on target platforms, window sizes, input methods, and assistive technologies as appropriate.
- Track deviations, defects, and follow-up work.
- Revisit designs using real usage evidence when available.

## Outputs
- Task flows and information architecture appropriate to scope
- Design principles and component/token guidance
- Prototype or screen specifications
- Accessibility and interaction-state notes
- Usability findings, decisions, and open questions
- Design acceptance criteria linked to requirements

## Exit criteria
- Core tasks and success criteria are defined.
- Major design decisions reflect user needs and platform context.
- Accessibility and non-happy-path states are addressed.
- Novel interactions have a stated user benefit and appropriate validation plan.
- Engineering handoff and outstanding risks are clear.
