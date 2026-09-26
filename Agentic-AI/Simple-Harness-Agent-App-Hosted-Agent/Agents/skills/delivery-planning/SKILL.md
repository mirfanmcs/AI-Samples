---
name: delivery-planning
description: Create an evidence-based software delivery brief with milestones, current documentation, risk scoring, and mitigations. Use for project planning, implementation planning, architecture delivery, or technology adoption requests.
---

## Workflow

1. Restate the objective, constraints, and assumptions.
2. Create Harness todos for discovery, design, implementation, validation, and
   rollout.
3. Use Context7 MCP for current documentation when the plan depends on a
   named library or framework.
4. Write intermediate notes to the Harness workspace when the request requires
   comparison or synthesis.
5. Ask the DeliveryRiskAnalyst background agent to review substantial plans.
6. Call `calculate_delivery_risk` using explicit values derived from the plan.
7. Produce a final brief with:
   - objective and scope;
   - assumptions;
   - architecture or implementation approach;
   - ordered milestones and acceptance checks;
   - dependencies;
   - risk score, band, and mitigations;
   - documentation sources.
8. Call `save_project_brief` only when the user asks to persist the result.

Do not invent documentation findings or report that a file exists unless a
tool confirms it.
