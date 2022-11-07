"""CP1404/CP5632 Practical - Guitar class example."""


class Guitar:
    """SOMETING WONG"""

    def __init__(self, name="", year=0, cost=0.0):
        """"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string on guitar object attributes"""
        return f"{self.name} {self.year} : {self.cost}"

    def get_age(self):
        """Returns how old guitar object is in years"""
        return

    def is_vintage(self):
        """Returns True if guitar is 50 or more years old"""
        return
