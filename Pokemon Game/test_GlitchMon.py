"""
Testing File for GlitchMon

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

import unittest

from tester_base import TesterBase
from GlitchMon import MissingNo


class TestPokemonBase(TesterBase):

    def test_missingno(self):
        p1 = MissingNo()

        # Test if MissingNo's properties correctly initialised
        try:
            self.assertEqual(str(p1), "MissingNo's HP = 8 and level = 1", msg="MissingNo not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(str(p1.get_speed()), "7", msg="MissingNo's speed not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_speed(self):

        # Test if the speed of MissingNo is set correctly
        p1 = MissingNo()
        try:
            self.assertEqual(p1.get_speed(), 7, msg="MissingNo's speed is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_attack(self):

        # Test if the attack of MissingNo is set correctly
        p1 = MissingNo()
        try:
            self.assertEqual(p1.get_attack(), 5, msg="MissingNo's attack is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_defence(self):

        # Test if the defence stat of MissingNo is set correctly
        p1 = MissingNo()
        try:
            self.assertEqual(p1.get_defence(), 5, msg="MissingNo's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_calculate_damage(self):

        # Test if the calculate_damage method for MissingNo has been set up correctly
        p1 = MissingNo()
        p1.calculate_damage(9)
        try:
            self.assertEqual(p1.get_hp(), 4,
                             msg="Life after attack incorrect, MissingNo's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        p1 = MissingNo()
        p1.calculate_damage(4)
        try:
            self.assertEqual(p1.get_hp(), 6,
                             msg="Life after attack incorrect, MissingNo's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_name(self):

        # Test if the get_name method for MissingNo has been set up correctly
        p1 = MissingNo()
        try:
            self.assertEqual(p1.get_name(), "MissingNo", msg="MissingNo's name is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_effectiveness(self):

        # Test if the effectiveness method for MissingNo has been set up correctly
        p1 = MissingNo()
        try:
            self.assertEqual(p1.effectiveness("GRASS"), 1, msg="MissingNo's effectiveness is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_string(self):

        # Test if the string method for MissingNo has been set up correctly
        p1 = MissingNo()
        try:
            s = str(p1)
            if s != "MissingNo's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
