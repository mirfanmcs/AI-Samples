import json
import os
import re
import uuid
from pathlib import Path

from agent_framework import tool
from pydantic import Field
from typing_extensions import Annotated


@tool(approval_mode="never_require")
def calculate_delivery_risk(
    complexity: Annotated[
        int,
        Field(ge=1, le=5, description="Solution complexity from 1 to 5."),
    ],
    external_dependencies: Annotated[
        int,
        Field(ge=0, le=10, description="Number of external dependencies."),
    ],
    unfamiliar_technologies: Annotated[
        int,
        Field(ge=0, le=10, description="Number of unfamiliar technologies."),
    ],
    deadline_pressure: Annotated[
        int,
        Field(ge=1, le=5, description="Deadline pressure from 1 to 5."),
    ],
) -> str:
    """Calculate a deterministic software-delivery risk score."""
    score = min(
        100,
        complexity * 10
        + external_dependencies * 3
        + unfamiliar_technologies * 4
        + deadline_pressure * 7,
    )
    if score >= 70:
        band = "high"
    elif score >= 40:
        band = "medium"
    else:
        band = "low"

    return json.dumps(
        {
            "score": score,
            "band": band,
            "factors": {
                "complexity": complexity,
                "external_dependencies": external_dependencies,
                "unfamiliar_technologies": unfamiliar_technologies,
                "deadline_pressure": deadline_pressure,
            },
        }
    )


@tool(approval_mode="never_require")
def save_project_brief(
    project_name: Annotated[
        str,
        Field(min_length=1, description="Name of the software project."),
    ],
    objective: Annotated[
        str,
        Field(min_length=1, description="Business objective for the project."),
    ],
    delivery_plan: Annotated[
        str,
        Field(
            min_length=1,
            description="Markdown delivery plan with milestones and risks.",
        ),
    ],
) -> str:
    """Save a project delivery brief as a Markdown artifact."""
    safe_name = re.sub(r"[^a-z0-9]+", "-", project_name.lower()).strip("-")
    if not safe_name:
        safe_name = "project"

    artifact_id = uuid.uuid4().hex[:8]
    file_name = f"{safe_name}-{artifact_id}.md"
    output_dir = Path(
        os.getenv("HARNESS_ARTIFACTS_DIR", "/tmp/harness-artifacts")
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / file_name
    file_path.write_text(
        (
            f"# {project_name}\n\n"
            f"## Objective\n\n{objective}\n\n"
            f"## Delivery plan\n\n{delivery_plan}\n"
        ),
        encoding="utf-8",
    )
    return json.dumps(
        {
            "message": f"Project brief saved as {file_name}.",
            "path": str(file_path),
        }
    )
