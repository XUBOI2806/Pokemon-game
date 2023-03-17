"""
Testing File for Pokemon_base

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

import unittest

from tester_base import TesterBase
from pokemon_base import PokemonBase


class TestPokemonBase(TesterBase):

    def test_get_hp(self):
        p1 = PokemonBase(4, "FIRE")
        try:
            self.assertEqual(p1.get_hp(), 4, msg="get_hp method incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_set_hp(self):
        p1 = PokemonBase(4, "FIRE")
        try:
            p1.set_hp(4)
            self.assertEqual(p1.get_hp(), 4, msg="set_hp method incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_level(self):
        p1 = PokemonBase(4, "FIRE")
        try:
            self.assertEqual(p1.get_level(), 1, msg="get_level method incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_set_level(self):
        p1 = PokemonBase(4, "FIRE")
        try:
            p1.set_level(4)
            self.assertEqual(p1.get_level(), 4, msg="set_level method incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_poke_class(self):
        p1 = PokemonBase(4, "FIRE")
        try:
            self.assertEqual(p1.get_poke_class(), "FIRE", msg="get_poke_class method incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_level_up(self):
        p1 = PokemonBase(4, "FIRE")
        try:
            p1.level_up()
            self.assertEqual(p1.get_level(), 2, msg="level_up method incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_is_fainted(self):
        p1 = PokemonBase(0, "FIRE")
        try:
            self.assertEqual(p1.is_fainted(), True, msg="is_fainted method incorrect")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
