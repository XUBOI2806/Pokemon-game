"""
Testing File for Battle

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

import unittest

from tester_base import TesterBase, captured_output
from battle import Battle

class TestTask3(TesterBase):

    def test_set_mode_battle(self):
        try:
            c = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1 0\n0 2 1 0") as (inp, out, err):
                result = c.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Brock"
        except AssertionError:
            self.verificationErrors.append(f"Brock should win: {result}.")
        try:
            assert str(c.team1) == "Bulbasaur's HP = 8 and level = 2, Bulbasaur's HP = 9 and level = 1, Squirtle's " \
                                   "HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(c.team1)}")

    def test_rotating_mode_battle(self):
        try:
            c = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 0 0 0\n0 1 0 0") as (inp, out, err):
                result = c.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Brock should win: {result}.")
        try:
            assert str(c.team1) == "Charmander's HP = 7 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(c.team1)}")

    def test_optimised_mode_battle(self):
        from battle import Battle

        try:
            b = Battle("Cynthia", "Steven")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1 0\n0 2 1 0") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            # Gen IV supremacy >:D
            assert result == "Cynthia"
        except AssertionError:
            self.verificationErrors.append(f"Cynthia should win: {result}.")
        try:
            assert str(b.team1) == "Bulbasaur's HP = 6 and level = 1, Bulbasaur's HP = 5 and level = 2, Squirtle's HP = 2 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)
