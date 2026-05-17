from typing import Protocol


class SettingsValidatorInterface(Protocol):
    def validate(self) -> None: ...
