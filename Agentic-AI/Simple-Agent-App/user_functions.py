import json
import uuid
from pathlib import Path
from typing import Any, Callable, Set


PROJECT_ROOT = Path(__file__).resolve().parent


def submit_support_ticket(email_address: str, description: str) -> str:
    """Create a local support-ticket file from the supplied contact and issue."""
    ticket_number = uuid.uuid4().hex[:6]
    file_name = f"ticket-{ticket_number}.txt"
    file_path = PROJECT_ROOT / file_name
    ticket_text = (
        f"Support ticket: {ticket_number}\n"
        f"Submitted by: {email_address}\n"
        f"Description:\n{description}"
    )
    file_path.write_text(ticket_text, encoding="utf-8")

    return json.dumps(
        {
            "message": (
                f"Support ticket {ticket_number} submitted. "
                f"The ticket file is saved as {file_name}"
            )
        }
    )


user_functions: Set[Callable[..., Any]] = {submit_support_ticket}
