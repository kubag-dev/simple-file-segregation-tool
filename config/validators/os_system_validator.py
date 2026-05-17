from config.exceptions.unrecognized_os_system_exception import (
    UnrecognizedOsSystemException,
)
from config.values.settings_values import SettingsValues


class OsSystemValidator:
    def __init__(self, *, os_system: SettingsValues.OsSystem) -> None:
        self.os_system = os_system

    def validate(self) -> None:
        try:
            SettingsValues.OsSystem(self.os_system)
        except ValueError:
            raise UnrecognizedOsSystemException()
