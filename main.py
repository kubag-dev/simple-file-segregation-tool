from config.settings import Settings


class Main:
    def __init__(self):
        pass

    def _initialize_settings(self) -> None:
        self.settings = Settings().load_environment_as_variable()

    def main(self):
        self._initialize_settings()


Main().main()
