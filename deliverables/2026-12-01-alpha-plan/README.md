# Alpha plan — seminar, 2026-12-01

Deck for the 1 Dec 2026 seminar (09:10, room 313, building 96): about 10 minutes on the Alpha, followed by the oral exam on the ARD. Draft made on 22 Nov 2026; issue [#24](https://github.com/danielB464646/CoHendrix/issues/24) (S1-21).

- **Live deck (Claude artifact, private until shared):** <https://claude.ai/artifact/PU76uCpom4iCjAAXfMVzdq>. It exports to PowerPoint or PDF from its Share menu.
- **Source:** [`source/`](source/) holds the deck's files (`deck.json`, `deck.css`, one HTML file per slide) as of 22 Nov 2026, so changes can be reviewed in Git.
- **Exported file:** not added yet. Add `Co-Hendrix_Alpha_Plan.pptx` here after the final version is exported.

## Slides

1. Cover
2. Co-Hendrix in one minute: the LLM writes, our code decides what is applied
3. The Alpha flow (ARD 5.2) and its "done when" criteria
4. Alpha scope: in the Alpha vs later — to agree with the advisor
5. Architecture: one slice, one layer per member (ADR 0013, ADR 0016)
6. Initial GUI mock-up: lock a region on the track × bar grid
7. Initial GUI mock-up: check result, diff, accept / reject / export, and the blocked case
8. How we work: walking skeleton, then feature ownership (ADR 0014)
9. Where we are on 1 Dec
10. Main challenges and how we cope
11. Gantt, Semester A
12. Gantt, whole project
13. Changes the advisor asked for
14. Questions

## Open gaps

1. Slide 13: the advisor's requested changes from the previous meeting are not known yet.
2. Slide 9: what runs by the seminar is to be filled in on 30 Nov.
3. Slides 6–7 are mock-ups; replace them with screenshots once the upload screen and grid run (issues #19, #20).
4. The slides were not viewed rendered when drafted; check the layout before presenting.
5. ARD Table 7 and Chapter 5 still show the old calendar (issue #23); the deck follows [`docs/planning/development-plan.md`](../../docs/planning/development-plan.md).
