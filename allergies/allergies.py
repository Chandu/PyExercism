
class Allergies:
    def __init__(self, score):
        self.__allergies_map = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }
        self.__score = score

    def is_allergic_to(self, score_input=""):
        lower_input = score_input.lower()
        score = self.__allergies_map[lower_input]
        return score | self.__score == self.__score

    @property
    def list(self):
        to_return = []
        for key, value in self.__allergies_map.iteritems():
            if self.is_allergic_to(key.lower()):
                to_return.append(key.lower())
        to_return.sort()
        return to_return
