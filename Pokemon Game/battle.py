"""
File that contains the class battle which calculates the winner of two teams

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

import random

from poke_team import PokeTeam

"""
This class is 
"""
class Battle:
    """
    This class contains methods which allow the determination of a winner from
    selection of two teams in queue formation.
    """
    def __init__(self, trainer_one_name: str, trainer_two_name: str):
        """
        Constructor to create a battle

        :param trainer_one_name: String of first trainer name
        :param trainer_two_name: String of second trainer name
        """
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    def set_mode_battle(self) -> str:
        """
        Asks user for input for team order, and battle mode is set to 0
        Sets up player's team where a pokemon fights until it faints

        Best time complexity: O(1) where n is 1, the number of pokemon in a given team
        Worst time complexity: O(n) where n is the number of pokemon in a given team

        :return: String of player's name who wins the battle
        """
        self.battle_mode = 0
        self.team1.choose_team(self.battle_mode)
        self.team2.choose_team(self.battle_mode)
        while len(self.team1.team) != 0 and len(self.team2.team) != 0:
            p1 = self.team1.team.pop()
            p2 = self.team2.team.pop()
            self.battle_phase(p1, p2)
            if not p2.is_fainted() and not p1.is_fainted():
                self.team2.team.push(p2)
                self.team1.team.push(p1)
            else:
                if p1.is_fainted() and p2.is_fainted():
                    break
                elif p2.is_fainted():
                    p1.level_up()
                    self.team1.team.push(p1)
                elif p1.is_fainted():
                    p2.level_up()
                    self.team2.team.push(p2)

        if len(self.team1.team) == 0 and len(self.team2.team) == 0:
            return "Draw"
        elif len(self.team1.team) == 0:
            return self.team2.name
        else:
            return self.team1.name

    def rotating_mode_battle(self) -> str:
        """
        Asks user for input for team order, and battle mode is set to 1
        Sets up battle in which every winning pokemon returns to the back of the team

        Best time complexity: O(1) when the number of pokemon in each team is 1
        Worst time complexity: O(n) when the number of pokemon in each team is n

        :return: String of winner player's name
        """
        self.battle_mode = 1
        self.team1.choose_team(self.battle_mode)
        self.team2.choose_team(self.battle_mode)
        while len(self.team1.team) != 0 and len(self.team2.team) != 0:
            p1 = self.team1.team.serve()
            p2 = self.team2.team.serve()
            self.battle_phase(p1, p2)
            if not p2.is_fainted() and not p1.is_fainted():
                self.team2.team.append(p2)
                self.team1.team.append(p1)
            else:
                if p1.is_fainted() and p2.is_fainted():
                    break
                elif p2.is_fainted():
                    p1.level_up()
                    self.team1.team.append(p1)
                elif p1.is_fainted():
                    p2.level_up()
                    self.team2.team.append(p2)

        if len(self.team1.team) == 0 and len(self.team2.team) == 0:
            return "Draw"
        elif len(self.team1.team) == 0:
            return self.team2.name
        else:
            return self.team1.name

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        Asks user for input for team order, and battle mode is set to 2
        Sets up player's team ordered by a given criterion

        Best time complexity: O(1) where n is 1, the number of pokemon in a given team
        Worst time complexity: O(n) where n is the number of pokemon in a given team

        :param criterion_team1: the criterion that team1 will be sorted by
        :param criterion_team2: the criterion that team2 will be sorted by
        :return: String of player's name who wins the battle
        """
        self.battle_mode = 2
        self.team1.choose_team(self.battle_mode, criterion_team1)
        self.team2.choose_team(self.battle_mode, criterion_team2)

        while len(self.team1.team) != 0 and len(self.team2.team) != 0:
            p1_ListItem = self.team1.team.get_last_item()
            p1 = p1_ListItem.get_value()
            p2_ListItem = self.team2.team.get_last_item()
            p2 = p2_ListItem.get_value()

            self.battle_phase(p1, p2)
            if not p2.is_fainted() and not p1.is_fainted():
                if self.team1.generate_list_item(p1, criterion_team1).get_key() == p1_ListItem.get_key():
                    self.team1.team.add_last_index(self.team1.generate_list_item(p1, criterion_team1))
                else:
                    self.team1.team.add_without_overwriting(self.team1.generate_list_item(p1, criterion_team1))

                if self.team2.generate_list_item(p2, criterion_team2).get_key() == p2_ListItem.get_key():
                    self.team2.team.add_last_index(self.team2.generate_list_item(p2, criterion_team2))
                else:
                    self.team2.team.add_without_overwriting(self.team2.generate_list_item(p2, criterion_team2))
            else:
                if p1.is_fainted() and p2.is_fainted():
                    break
                elif p2.is_fainted():
                    p1.level_up()
                    self.team1.team.add_without_overwriting(self.team1.generate_list_item(p1, criterion_team1))
                elif p1.is_fainted():
                    p2.level_up()
                    self.team2.team.add_without_overwriting(self.team2.generate_list_item(p2, criterion_team2))

        if len(self.team1.team) == 0 and len(self.team2.team) == 0:
            return "Draw"
        elif len(self.team1.team) == 0:
            return self.team2.name
        else:
            return self.team1.name

    def battle_phase(self, p1, p2) -> None:
        """
        Determines the outcome of a given battle between two pokemon depending on the speed of each pokemon

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param p1: pokemon 1
        :param p2: pokemon 2
        :return: None
        """
        if p1.get_speed() == p2.get_speed():
            self.attack_phase(p1, p2)
            self.attack_phase(p2, p1)
            if not p1.is_fainted() and not p2.is_fainted():
                p2.hp -= 1
                p1.hp -= 1
        elif p1.get_speed() > p2.get_speed():
            self.attack_phase(p1, p2)
            if not p2.is_fainted():
                self.attack_phase(p2, p1)
                if not p1.is_fainted():
                    p2.hp -= 1
                    p1.hp -= 1
        elif p1.get_speed() < p2.get_speed():
            self.attack_phase(p2, p1)
            if not p1.is_fainted():
                self.attack_phase(p1, p2)
                if not p2.is_fainted():
                    p2.hp -= 1
                    p1.hp -= 1

    def attack_phase(self, attacker, defender) -> None:
        """
        This method is the single attack phase of a Pokemon, where the Pokemon's attack is
        retrieved and the attack is multiplied by the multiplier damage. The final damage
        value is then inputted into the method.

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :type attacker: Pokemon
        :type defender: Pokemon
        :return: None
        """
        rand = random.randint(1, 4)
        # This if statement replaces the attack with the superpower if the pokemon is missing
        # With 25% chance of activating
        if defender.get_name() == "MissingNo" and rand == 1:
            defender.superpower()
        else:
            attack = attacker.get_attack()
            multiplier_dmg = attacker.effectiveness(defender.get_poke_class())
            damage = attack * multiplier_dmg
            defender.calculate_damage(damage)
