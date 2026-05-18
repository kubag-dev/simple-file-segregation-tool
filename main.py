from config.settings import Settings


class Main:
    def __init__(self):
        pass

    def _initialize_settings(self) -> None:
        self.settings = Settings().load_environment_as_variable()

    def _ensure_output_directories_exist(
        self, *, output_structure: None = None
    ) -> None:
        pass

    def _remove_created_output_directories(
        self, *, created_output_structure: None = None
    ) -> None:
        pass

    def main(self):
        # module responsible for preparing .env file
        # todo: create when implementing typer

        self._initialize_settings()

        created_output_structure = self._ensure_output_directories_exist()
        if self.settings.get(
            "DEBUG"
        ):  # todo: <- use constants here, create some helper function
            self._remove_created_output_directories(
                created_output_structure=created_output_structure
            )


Main().main()
