"""
File that contains class of GlitchMon which creates an object which is inherited from the PokemonBase class.

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""
import math
import random

from pokemon_base import PokemonBase


class GlitchMon(PokemonBase):
    """
    This Class is for creating GlitchMon a child of the pokemon_base
    The difference here is that the GlitchMon can use a superpower
    """
    def __init__(self):
        """
        This constructor doesn't take in anything but sets all GlitchMon's
        to have 8 hp
        """
        PokemonBase.__init__(self, 8, "")

    def increase_hp(self, hp: int) -> None:
        """
        This method is used to increase the GlitchMon's health
        It is used in the superpower method below is only used
        to increase hp by 1
        Doesn't have an output but instead accesses the objects health
        and increases it

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :type hp: int
        :return: None
        """

        self.set_hp(self.hp + hp)

    def superpower(self) -> None:
        """
        This method is used to replace an incoming attack with
        one of the three options
        - increasing health by 1 using the method above
        - increasing the level by 1
        - increasing health and level by 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: None
        """
        rand = random.randint(1, 3)
        if rand == 1:
            self.increase_hp(1)
        elif rand == 2:
            self.increase_hp(1)
            self.set_level(self.level + 1)
        elif rand == 3:
            self.set_level(self.level + 1)

class MissingNo(GlitchMon):
    """
    This Class is for creating a MissingNo child to GlitchMon
    This has the base stats average to all the other pokemon

    Math.floor is used to round down any fractions in the average
    The calculate_damage randomises between the three ways the damage
    is calculated for the other base pokemon.
    """
    def __init__(self):
        """
        This constructor doesn't take in any variables
        Sets the MissingNo as a GlitchMon
        Sets the base values of it's attack speed and defence and the
        average of all the other three pokemon
        """
        GlitchMon.__init__(self)
        self.attack = math.floor((6 + self.level + 5 + (4 + self.level // 2)) / 3)
        self.defence = math.floor((4 + 5 + 6 + self.level) / 3)
        self.speed = math.floor((7 + 7 + self.level + 7 + self.level // 2) / 3)
        self.name = "MissingNo"

    def get_attack(self) -> int:
        """
        Returns the MissingNo attack which adds one for every level past level 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int
        """
        return self.attack + self.level - 1

    def get_defence(self) -> int:
        """
        Returns the MissingNo defence which adds one for every level past level 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int
        """
        return self.defence - 1 + self.level

    def get_speed(self) -> int:
        """
        Returns the MissingNo speed which adds one for every level past level 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int
        """
        return self.speed - 1 + self.level

    def get_name(self) -> str:
        """
        Returns the MissingNo name

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: str
        """
        return self.name

    def calculate_damage(self, attack: int) -> None:
        """
        This method is used to calculate the damage of an incoming attack
        It randomly selects between the three different defences of
        Charmander, Squirtle and Bulbasuar.
        It has no return as the method takes off the damage done to the
        MissingNo.

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param attack: int
        :return: None
        """
        rand = random.randint(1, 3)
        if rand == 1:
            if attack > self.defence * 2:
                self.set_hp(self.get_hp() - attack)
            else:
                self.set_hp(self.get_hp() - attack // 2)
        elif rand == 2:
            if attack > self.defence + 5:
                self.set_hp(self.get_hp() - attack)
            else:
                self.set_hp(self.get_hp() - attack // 2)
        elif rand == 3:
            if attack > self.defence:
                self.set_hp(self.get_hp() - attack)
            else:
                self.set_hp(self.get_hp() - attack // 2)

    def effectiveness(self, poke_class) -> int:
        """
        This method returns the effectiveness modifier that is 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return int: 1
        """
        return 1

    def __str__(self) -> str:
        """
        This returns the MissingNo is a str format with all stats displayed

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: str format of the MissingNo and all its attributes
        """
        return "{}'s HP = {} and level = {}".format(self.name, self.hp, self.level)
