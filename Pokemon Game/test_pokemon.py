"""
Testing File for Pokemon

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

import unittest

from tester_base import TesterBase
from pokemon import Squirtle, Charmander, Bulbasaur


class TestPokemonBase(TesterBase):

    def test_bulbasaur(self):
        p1 = Bulbasaur()

        # Test if Bulbasaur's properties correctly initialised
        try:
            self.assertEqual(str(p1), "Bulbasaur's HP = 9 and level = 1", msg="Bulbasaur not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(str(p1.get_defence()), "5", msg="Bulbasaur's defence not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(str(p1.get_speed()), '7', msg="Bulbasaur's speed not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_charmander(self):
        p1 = Charmander()

        # Test if Charmander's properties correctly initialised
        try:
            self.assertEqual(str(p1), "Charmander's HP = 7 and level = 1", msg="Charmander not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(str(p1.get_defence()), "4", msg="Charmander's defence not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_squirtle(self):
        p1 = Squirtle()

        # Test if Squirtle's properties correctly initialised
        try:
            self.assertEqual(str(p1), "Squirtle's HP = 8 and level = 1", msg="Squirtle not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(str(p1.get_speed()), "7", msg="Squirtle's speed not created correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_speed(self):
        # Test if the speed of Bulbasaur is set correctly
        p1 = Bulbasaur()
        try:
            self.assertEqual(p1.get_speed(), 7, msg="Bulbasaur's speed is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the speed of Charmander is set correctly
        p1 = Charmander()
        try:
            self.assertEqual(p1.get_speed(), 8, msg="Charmander's speed is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the speed of Squirtle is set correctly
        p1 = Squirtle()
        try:
            self.assertEqual(p1.get_speed(), 7, msg="Squirtle's speed is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_attack(self):
        # Test if the attack of Bulbasaur is set correctly
        p1 = Bulbasaur()
        try:
            self.assertEqual(p1.get_attack(), 5, msg="Bulbasaur's attack is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the attack of Charmander is set correctly
        p1 = Charmander()
        try:
            self.assertEqual(p1.get_attack(), 7, msg="Charmander's attack is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the attack of Squirtle is set correctly
        p1 = Squirtle()
        try:
            self.assertEqual(p1.get_attack(), 4, msg="Squirtle's attack is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_defence(self):
        # Test if the defence stat of Bulbasaur is set correctly
        p1 = Bulbasaur()
        try:
            self.assertEqual(p1.get_defence(), 5, msg="Bulbasaur's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the defence stat of Charmander is set correctly
        p1 = Charmander()
        try:
            self.assertEqual(p1.get_defence(), 4, msg="Charmander's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the defence stat of Squirtle is set correctly
        p1 = Squirtle()
        try:
            self.assertEqual(p1.get_defence(), 7, msg="Squirtle's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_calculate_damage(self):
        # Test if the calculate_damage method for Bulbasaur has been set up correctly
        p1 = Bulbasaur()
        p1.calculate_damage(9)
        try:
            self.assertEqual(p1.get_hp(), 5,
                             msg="Life after attack incorrect, Bulbasaur's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        p1 = Bulbasaur()
        p1.calculate_damage(11)
        try:
            self.assertEqual(p1.get_hp(), -2,
                             msg="Life after attack incorrect, Bulbasaur's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the calculate_damage method for Squirtle has been set up correctly
        p1 = Squirtle()
        p1.calculate_damage(9)
        try:
            self.assertEqual(p1.get_hp(), 4,
                             msg="Life after attack incorrect, Squirtle's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        p1 = Squirtle()
        p1.calculate_damage(4)
        try:
            self.assertEqual(p1.get_hp(), 6,
                             msg="Life after attack incorrect, Squirtle's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the calculate_damage method for Charmander has been set up correctly
        p1 = Charmander()
        p1.calculate_damage(5)
        try:
            self.assertEqual(p1.get_hp(), 2,
                             msg="Life after attack incorrect, Charmander's defence is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        p1 = Charmander()
        p1.calculate_damage(4)
        try:
            self.assertEqual(p1.get_hp(), 5, msg="Life after attack incorrect, Charmander's defence is set up "
                                                 "incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_name(self):
        # Test if the get_name method for Bulbasaur has been set up correctly
        p1 = Bulbasaur()
        try:
            self.assertEqual(p1.get_name(), "Bulbasaur", msg="Bulbasuar's name is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the get_name method for Squirtle has been set up correctly
        p1 = Squirtle()
        try:
            self.assertEqual(p1.get_name(), "Squirtle", msg="Squirtle's name is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the get_name method for Charmander has been set up correctly
        p1 = Charmander()
        try:
            self.assertEqual(p1.get_name(), "Charmander", msg="Charmander's name is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_effectiveness(self):
        # Test if the effectiveness method for Bulbasaur has been set up correctly
        p1 = Bulbasaur()
        try:
            self.assertEqual(p1.effectiveness("GRASS"), 1, msg="Bulbasuar's effectiveness is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the effectiveness method for Squirtle has been set up correctly
        p1 = Squirtle()
        try:
            self.assertEqual(p1.effectiveness("GRASS"), 0.5, msg="Squirtle's effectiveness is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the effectiveness method for Charmander has been set up correctly
        p1 = Charmander()
        try:
            self.assertEqual(p1.effectiveness("GRASS"), 2, msg="Charmander's effectiveness is set up incorrectly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_string(self):
        # Test if the string method for Bulbasaur has been set up correctly
        p1 = Bulbasaur()
        try:
            s = str(p1)
            if s != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

        # Test if the string method for Squirtle has been set up correctly
        p1 = Squirtle()
        try:
            s = str(p1)
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

        # Test if the string method for Charmander has been set up correctly
        p1 = Charmander()
        try:
            s = str(p1)
            if s != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
