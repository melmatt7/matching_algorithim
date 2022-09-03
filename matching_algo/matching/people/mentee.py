# Class to represent the Mentee

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
        prefs.remove(other)
        self.prefs = prefs

    def get_successors(self):
        # print(self.matching)
        idx = self.prefs.index(self.matching)
        return self.prefs[idx + 1 :]

    def prefers(self, mentee, other):
        prefs = self.pref_names
        return prefs.index(mentee.name) < prefs.index(other.name)
