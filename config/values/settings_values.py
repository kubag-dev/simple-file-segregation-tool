from enum import Enum


class SettingsValues:
    class OsSystem(str, Enum):
        POSIX = "posix"
        NT = "nt"
