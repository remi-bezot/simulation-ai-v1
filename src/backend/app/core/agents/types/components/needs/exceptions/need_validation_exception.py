from typing import Optional


class NeedValidationException(Exception):
    """Exception personnalisée pour les erreurs de validation des besoins"""

    def __init__(
        self, message: str, need_id: Optional[str] = None, value: Optional[float] = None
    ):
        super().__init__(message)
        self.need_id = need_id
        self.value = value

    def __str__(self):
        base_message = super().__str__()
        if self.need_id is not None and self.value is not None:
            return f"{base_message} (Need ID: {self.need_id}, Value: {self.value})"
        return base_message
