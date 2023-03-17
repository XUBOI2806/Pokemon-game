"""
File that contains methods which is contained in the abstract class called PokemonBase.

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """
    This class is an abstract class for Pokemons. The class contains
    methods to instantiate base attributes and will be inherited by child
    class.
    """

    def __init__(self, hp: int, poke_class: str) -> None:
        """
        Constructor for the class, binds instance variables to
        given values

        :param hp: An integer of the Pokemon's health
        :param poke_class: A string of the Pokemon's class
        :returns: None
        """
        self.hp = hp
        self.level = 1
        self.poke_class = poke_class

    def set_hp(self, hp: int) -> None:
        """
        Sets hp of pokemon

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param hp: int of new hp
        :return: None
        """
        self.hp = hp

    def set_level(self, level: int) -> None:
        """
        Sets level of pokemon

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param level: int of new level
        :return: None
        """
        self.level = int(level)

    def get_hp(self) -> int:
        """
        Returns hp of pokemon

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: An int of the Pokemon's hp
        """
        return int(self.hp)

    def get_level(self) -> int:
        """
        Returns level of pokemon

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: A int of the Pokemon's level
        """
        if self.level < 0:
            raise ValueError
        return int(self.level)

    def get_poke_class(self) -> str:
        """
        Returns poke type of pokemon

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: A string og the pokemon class
        """
        if self.poke_class not in ["GRASS", "FIRE", "WATER"]:
            raise TypeError
        return self.poke_class

    def get_attack(self) -> int:
        """
        Abstract Class
        Returns the pokemon attack which adds one for every level
        """
        pass

    def get_defence(self) -> int:
        """
        Abstract Class
        Returns the pokemon defence which adds one for every level
        """
        pass

    def get_speed(self) -> int:
        """
        Abstract Class
        Returns the pokemon speed which adds one for every level
        """
        pass

    def calculate_damage(self, attack: int) -> None:
        """
        Abstract Class
        Calculates the damage received by an incoming attack
        It has no return as the method takes off the damage done to the pokemon
        Takes attack value of opposing pokemon as an input

        :param attack: int value of opposing pokemon attack value
        :return: None
        """
        if attack < 0:
            return ValueError
        pass

    def get_name(self) -> str:
        """
        Returns the pokemon's name

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: string of pokemons name
        """
        return self.name

    def effectiveness(self, poke_class) -> int:
        """
        Abstract Class
        This method overrides the base class method and an integer of the multiplier damage is returned dependant on
        the opposing Pokemon's class
        """
        pass

    def is_fainted(self) -> bool:
        """
        Checks if a pokemon has fainted or not

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: boolean value whether pokemon is fainted
        """
        if self.hp > 0:
            return False
        else:
            return True

    def level_up(self) -> None:
        """
        Increases level of pokemon by 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: None
        """
        self.level += 1

    def __str__(self) -> str:
        """
        Returns a description of the pokemon's stats in string format

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: String of pokemon's stats
        """
        return "{}'s HP = {} and level = {}".format(self.name, self.hp, self.level)
