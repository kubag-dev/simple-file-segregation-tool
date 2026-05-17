from config.validators.interface import SettingsValidatorInterface


class BooleanSettingsValidator(SettingsValidatorInterface):
    def __init__(self, *, debug: bool):
        self.debug = debug

    def validate(self) -> None:
        if self.debug not in {True, False}:
            pass
