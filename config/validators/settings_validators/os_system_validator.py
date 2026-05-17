from config.exceptions import UnrecognizedOsSystemException
from config.validators.interface import SettingsValidatorInterface
from config.values.settings_values import SettingsValues


class OsSystemValidator(SettingsValidatorInterface):
    def __init__(self, *, os_system: SettingsValues.OsSystem) -> None:
        self.os_system = os_system

    def validate(self) -> None:
        try:
            SettingsValues.OsSystem(self.os_system)
        except ValueError:
            raise UnrecognizedOsSystemException()
