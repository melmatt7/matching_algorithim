# Class to represent the Mentee
from logging import warning

class Mentee:
    """
    Parameters:
        name : `object`
            The mentee id
    Attributes:
        prefs : `list`
            A list of `Mentee` instances in order of the Mentee's preferences.
            Defaults to `None` and is updated using the `set_prefs` method.
        pref_names : `list`
            A list of the Mentor ids in `prefs`. Updates with `prefs`.
        matching : `Mentee` or `None`
            The current match of the mentee. `None` if not currently matched.
    """
    def __init__(self, name):

        self.name = name
        self.prefs = None
        self.pref_names = None
        self.matching = None

    def __repr__(self):

        return str(self.name)

    def set_prefs(self, mentees):
        self.prefs = mentees
        self.pref_names = [mentee.name for mentee in mentees]

    def get_favourite(self):
        return self.prefs[0]

    def match(self, other):
        self.matching = other

    def unmatch(self):
        self.matching = None

    def forget(self, other):
        prefs = self.prefs[:]
        try:
            prefs.remove(other)
        except ValueError:
            raise ValueError(f"Mentee {other} has put mentor {self.name} multiple times in their preferences, remove redundant preferences before continuing")

        self.prefs = prefs

    def get_successors(self):
        try:
            idx = self.prefs.index(self.matching)
        except ValueError:
            raise ValueError(f"Mentor {self.matching} has put mentee {self.name} multiple times in their preferences, remove redundant preferences before continuing") from None
        
        return self.prefs[idx + 1 :]

    def prefers(self, mentee, other):
        prefs = self.pref_names
        return prefs.index(mentee.name) < prefs.index(other.name)
