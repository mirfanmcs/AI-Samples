from semantic_kernel.functions import kernel_function
from typing import Annotated

# Create a Plugin for the email functionality
# Note: The function simulates sending an email by printing it to the console. In a real application, you’d use an SMTP service or similar to actually send the email!
class EmailPlugin:
    """A Plugin to simulate email functionality."""
    
    @kernel_function(description="Sends an email.")
    def send_email(self,
                   to: Annotated[str, "Who to send the email to"],
                   subject: Annotated[str, "The subject of the email."],
                   body: Annotated[str, "The text body of the email."]):
        print("\nTo:", to)
        print("Subject:", subject)
        print(body, "\n")
