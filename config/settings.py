from typing import Any

from dotenv import dotenv_values

from config import constants
from config import validators


class Settings:
    def __init__(self):
        pass

    def load_environment_as_variable(self) -> dict[str, Any]:
        settings = {**dotenv_values(constants.ENV_PATH)}
        validators.MainSettingsValidator(settings=settings).validate()
        return settings
