from .matching import Matching
from .people import Mentee
from .people import Mentor


class MentorMentee:

    def __init__(self, mentees=None, mentors=None):

        self._matching = None
        self.blocking_pairs = None

        self.mentees = mentees
        self.mentors = mentors

        super().__init__()
        self._check_inputs()
        
    @property
    def matching(self):
        return self._matching

    @matching.getter
    def matching(self):
        return self._matching

    @classmethod
    def create_from_dictionaries(
        cls, mentee_prefs, mentor_prefs, capacities
    ):
        mentees, mentors = _make_players(
            mentee_prefs, mentor_prefs, capacities
        )
        game = cls(mentees, mentors)

        return game

    def solve(self):
        self._matching = Matching(
            mentor_mentee(self.mentors)
        )
        return self.matching

    def check_validity(self):
        self._check_mentee_matching()
        self._check_mentor_capacity()
        self._check_mentor_matching()

        return True

    def check_stability(self):
        blocking_pairs = []
        for mentee in self.mentees:
            for mentor in self.mentors:
                if (
                    _check_mutual_preference(mentee, mentor)
                    and _check_mentee_unhappy(mentee, mentor)
                    and _check_mentor_unhappy(mentee, mentor)
                ):
                    blocking_pairs.append((mentee, mentor))

        self.blocking_pairs = blocking_pairs
        return not any(blocking_pairs)

    def _check_mentee_matching(self):
        errors = []
        for mentee in self.mentees:
            if (
                mentee.matching is not None
                and mentee.matching not in mentee.prefs
            ):
                errors.append(
                    ValueError(
                        f"{mentee} is matched to {mentee.matching} but "
                        "they do not appear in their preference list: "
                        f"{mentee.prefs}."
                    )
                )

        if errors:
            raise Exception(*errors)

        return True

    def _check_mentor_capacity(self):
        errors = []
        for mentor in self.mentors:
            if len(mentor.matching) > mentor.capacity:
                errors.append(
                    ValueError(
                        f"{mentor} is matched to {mentor.matching} which "
                        f"is over their capacity of {mentor.capacity}."
                    )
                )

        if errors:
            raise Exception(*errors)

        return True

    def _check_mentor_matching(self):
        errors = []
        for mentor in self.mentors:
            for mentee in mentor.matching:
                if mentee not in mentor.prefs:
                    errors.append(
                        ValueError(
                            f"{mentor} has {mentee} in their matching but "
                            "they do not appear in their preference list: "
                            f"{mentor.prefs}."
                        )
                    )

        if errors:
            raise Exception(*errors)

        return True

    def _check_inputs(self):
        self._check_mentee_prefs()
        self._check_mentor_prefs()

    def _check_mentee_prefs(self):
        errors = []
        for mentee in self.mentees:
            if not set(mentee.prefs).issubset(set(self.mentors)):
                errors.append(
                    ValueError(
                        f"{mentee} has ranked a non-mentor: "
                        f"{set(mentee.prefs)} != {set(self.mentors)}"
                    )
                )

        if errors:
            raise Exception(*errors)

        return True

    def _check_mentor_prefs(self):
        errors = []
        for mentor in self.mentors:
            mentees_that_ranked = [
                res for res in self.mentees if mentor in res.prefs
            ]
            if set(mentor.prefs) != set(mentees_that_ranked):
                errors.append(
                    ValueError(
                        f"{mentor} has not ranked all the mentees that "
                        f"ranked it: {set(mentor.prefs)} != "
                        f"{set(mentees_that_ranked)}."
                    )
                )

            if errors:
                raise Exception(*errors)
                
        return True


def _check_mutual_preference(mentee, mentor):
    return mentee in mentor.prefs and mentor in mentee.prefs


def _check_mentee_unhappy(mentee, mentor):
    return mentee.matching is None or mentee.prefers(
        mentor, mentee.matching
    )


def _check_mentor_unhappy(mentee, mentor):
    return len(mentor.matching) < mentor.capacity or any(
        [mentor.prefers(mentee, match) for match in mentor.matching]
    )


def unmatch_pair(mentee, mentor):
    mentee.unmatch()
    mentor.unmatch(mentee)


def mentor_mentee(mentors):
    free_mentors = mentors[:]
    while free_mentors:

        mentor = free_mentors.pop()
        mentee = mentor.get_favourite()

        if mentee.matching:
            curr_match = mentee.matching
            unmatch_pair(mentee, curr_match)
            if curr_match not in free_mentors:
                free_mentors.append(curr_match)

        match_pair(mentee, mentor)
        if len(mentor.matching) < mentor.capacity and [
            res for res in mentor.prefs if res not in mentor.matching
        ]:
            free_mentors.append(mentor)

        successors = mentee.get_successors()
        for successor in successors:
            delete_pair(mentee, successor)
            if (
                not [
                    res
                    for res in successor.prefs
                    if res not in successor.matching
                ]
                and successor in free_mentors
            ):
                free_mentors.remove(successor)

    return {r: r.matching for r in mentors}


def _make_players(mentee_prefs, mentor_prefs, capacities):
    mentee_dict, mentor_dict = _make_instances(
        mentee_prefs, mentor_prefs, capacities
    )

    for mentee_name, mentee in mentee_dict.items():
        prefs = [mentor_dict[name] for name in mentee_prefs[mentee_name]]
        mentee.set_prefs(prefs)

    mentees = list(mentee_dict.values())

    for mentor_name, mentor in mentor_dict.items():
        prefs = [mentee_dict[name] for name in mentor_prefs[mentor_name]]
        mentees_that_ranked = [res for res in mentees if mentor in res.prefs]
        unranked_mentees = list(set(mentees_that_ranked) - set(prefs))
        prefs = prefs + unranked_mentees
        random_mentees = list(set(prefs)-set(mentees_that_ranked))
        prefs = [x for x in prefs if x not in random_mentees]

        mentor.set_prefs(prefs)
 
    mentors = list(mentor_dict.values())

    return mentees, mentors


def _make_instances(mentee_prefs, mentor_prefs, capacities):
    mentee_dict, mentor_dict = {}, {}
    for mentee_name in mentee_prefs:
        mentee = Mentee(name=mentee_name)
        mentee_dict[mentee_name] = mentee
    for mentor_name in mentor_prefs:
        capacity = capacities[mentor_name]
        mentor = Mentor(name=mentor_name, capacity=capacity)
        mentor_dict[mentor_name] = mentor

    return mentee_dict, mentor_dict

def delete_pair(player, successor):
    player.forget(successor)
    successor.forget(player)


def match_pair(suitor, reviewer):
    suitor.match(reviewer)
    reviewer.match(suitor)