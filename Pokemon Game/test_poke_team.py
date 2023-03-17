"""
Testing File for Poke_team

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

import unittest

from tester_base import TesterBase, captured_output
from poke_team import PokeTeam


class TestPokemonBase(TesterBase):

    def test_battle_mode_0(self):
        try:
            team = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
            assert "is if you want a GlitchMon" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = " \
                                "8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_battle_mode_1(self):
        try:
            team = PokeTeam("Brock")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(1, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
            assert "is if you want a GlitchMon" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = " \
                                "8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_battle_mode_2_lvl(self):
        try:
            team = PokeTeam("Misty")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(2, "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
            assert "is if you want a GlitchMon" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = " \
                                "8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_battle_mode_2_hp(self):
        try:
            team = PokeTeam("Misty")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(2, "hp")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
            assert "is if you want a GlitchMon" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Charmander's HP = " \
                                "7 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_battle_mode_2_attack(self):
        try:
            team = PokeTeam("Misty")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(2, "attack")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
            assert "is if you want a GlitchMon" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = " \
                                "8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_battle_mode_2_defence(self):
        try:
            team = PokeTeam("Misty")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(2, "defence")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
            assert "is if you want a GlitchMon" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Squirtle's HP = 8 and level = 1, Bulbasaur's HP = 9 and level = 1, Charmander's HP = " \
                                "7 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_battle_mode_2_speed(self):
        try:
            team = PokeTeam("Misty")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(2, "speed")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
            assert "is if you want a GlitchMon" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = " \
                                "8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
