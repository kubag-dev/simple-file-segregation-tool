from typing import Any

from config import constants
from config import exceptions
from config.validators import settings_validators
from config.validators.interface import SettingsValidatorInterface
from config.values.settings_values import SettingsValues


class MainSettingsValidator(SettingsValidatorInterface):
    def __init__(self, settings: dict[str, Any]) -> None:
        self.settings = settings

    def _convert_str_to_bool(self, *, value: str) -> bool:
        if value == "True":
            return True
        elif value == "False":
            return False
        else:
            raise

    def validate(self) -> None:
        debug = self.settings.get("debug", "False")

        os_system = self.settings.get(constants.OS_SYSTEM)
        if not os_system:
            raise exceptions.RequiredEnvNotProvided(required_env=constants.OS_SYSTEM)
        settings_validators.OsSystemValidator(
            os_system=SettingsValues.OsSystem(os_system)
        ).validate()
