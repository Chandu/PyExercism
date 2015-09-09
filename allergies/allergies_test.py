import unittest

from allergies import Allergies


class AllergiesTests(unittest.TestCase):

    def test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_is_allergic_to_eggs(self):
        self.assertTrue(Allergies(1).is_allergic_to('eggs'))

    def test_has_the_right_allergies(self):
        allergies = Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))
        self.assertTrue(allergies.is_allergic_to('shellfish'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_no_allergies_at_all(self):
        self.assertListEqual([], Allergies(0).list)

    def test_allergic_to_just_peanuts(self):
        self.assertListEqual(['peanuts'], Allergies(2).list)

    def test_allergic_to_everything(self):
        allergies_list = ('eggs peanuts shellfish strawberries tomatoes '
                          'chocolate pollen cats').split()
        allergies_list.sort()
        self.assertListEqual(allergies_list, Allergies(255).list)

    def test_ignore_non_allergen_score_parts(self):
        self.assertListEqual(['eggs'], Allergies(257).list)


if __name__ == '__main__':
    unittest.main()
