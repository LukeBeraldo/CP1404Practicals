"""CP1404/CP5632 Practical - Guitar class example."""
CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Guitar class that stores details of guitar"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string on guitar object attributes"""
        return f"{self.name} {self.year} : {self.cost}"

    def get_age(self):
        """Returns how old guitar object is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if guitar is 50 or more years old"""
        if self.get_age() >= VINTAGE_AGE:
            return True
        else:
            return False

