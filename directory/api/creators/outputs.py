from pathlib import Path


class Outputs:
    DIR_TREE = {
        "output": {
            "images": {},
            "executables": {},
            "archives": {},
            "movies": {},
            "texts": {},
        }
    }

    def execute(self, *, dir_map=None) -> None:
        """
        First iteration with hardcoded relational directories,
        will make variable with map creation later on.
        todo: implement directory tree creation and use it here
        """
        if not dir_map:
            dir_map = self.DIR_TREE

        for parent, children in dir_map.items():
            path = Path("./") / parent
            path.mkdir(parents=True, exist_ok=True)

            if isinstance(children, dict):
                self.execute(dir_map=children)
