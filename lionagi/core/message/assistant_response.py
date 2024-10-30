from typing import Any

from .message import MessageRole, RoledMessage


class AssistantResponse(RoledMessage):
    """
    Represents a response generated by an assistant.

    Inherits from `RoledMessage` and provides attributes specific to assistant responses.

    Attributes:
        assistant_response (Any): The content of the assistant's response.
        sender (str): The sender of the response.
        recipient (str): The recipient of the response.
    """

    def __init__(
        self,
        assistant_response: Any = None,
        sender: str | None = None,
        recipient: str | None = None,
        **kwargs,
    ):
        """
        Initializes the AssistantResponse.

        Args:
            assistant_response (Any, optional): The content of the assistant's response.
            sender (str, optional): The sender of the response.
            recipient (str, optional): The recipient of the response.
            **kwargs: Additional keyword arguments to be passed to the parent class.
        """

        super().__init__(
            role=MessageRole.ASSISTANT,
            sender=sender or "N/A",
            content={"assistant_response": assistant_response["content"]},
            recipient=recipient,
            **kwargs,
        )

    def clone(self, **kwargs):
        """
        Creates a copy of the current AssistantResponse object with optional additional arguments.

        This method clones the current object, preserving its content.
        It also retains the original metadata, while allowing
        for the addition of new attributes through keyword arguments.

        Args:
            **kwargs: Optional keyword arguments to be included in the cloned object.

        Returns:
            AssistantResponse: A new instance of the object with the same content and additional keyword arguments.
        """
        import json

        content = json.dumps(self.content["assistant_response"])
        content = {"content": json.loads(content)}
        response_copy = AssistantResponse(assistant_response=content, **kwargs)
        response_copy.metadata["origin_ln_id"] = self.ln_id
        return response_copy

    @property
    def chat_msg(self) -> dict | None:
        """Return message in chat representation."""
        try:
            return self._check_chat_msg()
        except:
            return None

    def _check_chat_msg(self):
        text_msg = super()._check_chat_msg()
        return text_msg

    @property
    def response(self):
        """Return the assistant response content."""
        return self.content["assistant_response"]
