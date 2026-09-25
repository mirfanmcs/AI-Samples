import json
import os
import uuid
from pathlib import Path

from agent_framework import tool
from pydantic import Field
from typing_extensions import Annotated


@tool(approval_mode="never_require")
def submit_support_ticket(
    email_address: Annotated[
        str,
        Field(description="Email address of the person reporting the issue."),
    ],
    description: Annotated[
        str,
        Field(description="Complete description of the technical issue."),
    ],
) -> str:
    """Create a support ticket file in the hosted agent's writable directory."""
    ticket_number = uuid.uuid4().hex[:6]
    file_name = f"ticket-{ticket_number}.txt"
    output_dir = Path(os.getenv("TICKET_OUTPUT_DIR", "/tmp/support-tickets"))
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / file_name
    file_path.write_text(
        (
            f"Support ticket: {ticket_number}\n"
            f"Submitted by: {email_address}\n"
            f"Description:\n{description}"
        ),
        encoding="utf-8",
    )
    return json.dumps(
        {
            "message": (
                f"Support ticket {ticket_number} submitted. "
                f"The ticket file is saved as {file_name}"
            )
        }
    )
