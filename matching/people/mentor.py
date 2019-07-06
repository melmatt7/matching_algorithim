from .mentee import Mentee

class Mentor(Mentee):
   
    def __init__(self, name, capacity):

        super().__init__(name)
        self.capacity = capacity
        self.matching = []

    def get_favourite(self):
        for mentee in self.prefs:
            if mentee not in self.matching:
                return mentee

        return None

    def match(self, mentee):
        self.matching.append(mentee)
        self.matching.sort(key=self.prefs.index)

    def unmatch(self, mentee):
        matching = self.matching[:]
        matching.remove(mentee)
        self.matching = matching

    def get_worst_match(self):
        return self.matching[-1]

    def get_successors(self):
        idx = self.prefs.index(self.get_worst_match())
        return self.prefs[idx + 1 :]
