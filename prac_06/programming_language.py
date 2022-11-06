"""CP1404/CP5632 Practical - Programming language exercise."""


class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, name="", typing="Static", reflection="No", year=""):
        """Initialise a Car instance."""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        pass
