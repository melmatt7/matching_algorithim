from .people.mentee import Mentee


class Matching(dict):
    def __init__(self, dictionary=None):

        self.__data = {}
        if dictionary is not None:
            self.__data.update(dictionary)

        super().__init__(self.__data)

    def __repr__(self):

        return repr(self.__data)

    def __getitem__(self, mentee):

        return self.__data[mentee]

    def __setitem__(self, mentee, new_match):

        if mentee not in self.__data.keys():
            raise ValueError(f"{mentee} is not a key in this matching.")

        if isinstance(new_match, Mentee):
            new_match.matching = mentee
            mentee.matching = new_match

        elif new_match is None:
            mentee.matching = new_match

        elif isinstance(new_match, (list, tuple)) and all(
            [isinstance(new, Mentee) for new in new_match]
        ):
            mentee.matching = new_match
            for new in new_match:
                new.matching = mentee

        else:
            raise ValueError(f"{new_match} is not a valid match.")

        self.__data[mentee] = new_match

    def keys(self):

        return self.__data.keys()

    def values(self):

        return self.__data.values()
