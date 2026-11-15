# ARD reference material

Course material for writing the ARD. It is not Co-Hendrix requirements; use it for structure and grading only.

| File | What it is |
| --- | --- |
| [`ard-template.pdf`](ard-template.pdf) | Course ARD template (rev. 21 Oct 2018). Defines the required chapters. |
| [`ard-grading-template.docx`](ard-grading-template.docx) | ARD grading sheet with section weights. |
| [`example-ard-m2m-video-streaming.pdf`](example-ard-m2m-video-streaming.pdf) | Past example ARD: "M2M Wise Video Streaming" (36 pages). |
| [`example-ard-email-data-leakage.pdf`](example-ard-email-data-leakage.pdf) | Past example ARD: "Preventing Data Leakage via E-mail" (54 pages). |

## Required chapters (from the template)

1. Introduction: 1.1 Problem domain · 1.2 Context (block diagram, our system as one block) · 1.3 Vision · 1.4 Stakeholders · 1.5 Software context (inputs, functionality, processing, outputs)
2. Usage scenarios: 2.1 User profiles / actors · 2.2 Use cases · 2.3 Special usage considerations
3. Functional requirements (hierarchical taxonomy; use-case or sequence diagrams allowed)
4. Non-functional requirements, quantified: 4.1 Implementation constraints (performance, reliability, safety & security, portability, usability, availability) · 4.2 Platform constraints · 4.2.1 SE project constraints (demo, inputs, simulation) · 4.3 Special restrictions & limitations
5. Risk assessment & plan for the proof of concept
6. Appendices: I/O formats, similar products, background, glossary

The template also asks the team to propose additional or more general functionality beyond what the customer stated. Prototype / v1.0 / future scoping is decided after the ARD is accepted.

## Grading weights

| Section | Weight | Grader note |
| --- | --- | --- |
| Introduction (goals, problem domain, vision) | 15% | 5 points for vision, stakeholders, and context (overall system architecture) |
| Usage scenarios and use cases | 20% | |
| Functional requirements | 20% | |
| Non-functional requirements | 10% | |
| Risk assessment & plan for the proof of concept | 20% | 10 points each |
| Document quality | 5% | Numbered figures referenced in text, headings, fonts |
| ARD presentation | 10% | |

## Notes on the examples

- Both examples put use cases after the non-functional requirements and add a "System interfaces" section (hardware, software, events) under the introduction.
- Neither example has a risk / proof-of-concept chapter. That chapter is 20% of the grade, so the examples are no guide for it.
- The m2m example writes each use case as primary actor, description, stakeholders and interests, preconditions, postconditions, main success scenario, and alternative flows, with a numbered sequence diagram per use case.
