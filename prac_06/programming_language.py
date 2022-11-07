"""CP1404/CP5632 Practical - Programming language exercise."""


class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, name="", typing="Static", reflection=False, year=""):
        """Initialise a Car instance."""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """ """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Will return True if the language is dynamically typed else False"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
