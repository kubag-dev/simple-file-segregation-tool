class RequiredEnvNotProvided(Exception):
    def __init__(self, *, required_env: str) -> None:
        self.details = f"{required_env} is not provided"
