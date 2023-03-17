"""
File that contains classes of Charmander, Squirtle and Bulbasaur which creates an object which is inherited from
the PokemonBase class.

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    """
    This class creates an object of type 'Charmander' which inherits from
    the PokemonBase class
    """

    def __init__(self):
        """
        This method is called when the class is instantiated and creates
        an object of the class and binds instance variables.

        :param speed: An integer of the Pokemon's speed
        :param attack: An integer of the Pokemon's attack_damage
        :param defence: An integer of the Pokemon's defence
        :param name: A string of the Pokemon's name
        :returns: None
        """
        PokemonBase.__init__(self, 7, "FIRE")
        self.attack = 6
        self.defence = 4
        self.speed = 7
        self.name = "Charmander"

    def get_attack(self) -> int:
        """
        Returns the pokemon attack which adds one for every level past level 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon attack value
        """
        return int(self.attack + self.level)

    def get_defence(self) -> int:
        """
        Returns the pokemon defence

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon defence value
        """
        return int(self.defence)

    def get_speed(self) -> int:
        """
        Returns the pokemon speed which adds one for every level past level 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon speed value
        """
        return int(self.speed + self.level)

    def get_name(self) -> str:
        """
        Returns the pokemon's name

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: string of pokemons name
        """
        return self.name

    def calculate_damage(self, attack: int) -> int:
        """
        Calculates the damage received by an incoming attack
        It has no return as the method takes off the damage done to the pokemon
        Takes attack value of opposing pokemon as an input

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param attack: int value of opposing pokemon attack value
        :return: None
        """
        if attack > self.defence:
            self.set_hp(self.get_hp() - attack)
        else:
            self.set_hp(self.get_hp() - attack // 2)

    def effectiveness(self, poke_class) -> int:
        """
        This method overrides the base class method and an integer of the multiplier damage is returned dependant on
        the opposing Pokemon's class

        Best time complexity: O(1)
        Worst time complexity: O(n) where n is the number of pokemon types

        :returns: An integer of the multiplier damage is returned.
        """
        if poke_class == "WATER":
            return 0.5
        elif poke_class == "FIRE":
            return 1
        elif poke_class == "GRASS":
            return 2
        else:
            return 1

    def __str__(self) -> str:
        """
        Returns a description of the pokemon's stats in string format

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: String of pokemon's statss
        """
        return "{}'s HP = {} and level = {}".format(self.name, int(self.hp), self.level)


class Bulbasaur(PokemonBase):
    """
    This class creates an object of type 'Bulbasaur' which inherits from
    the PokemonBase class
    """

    def __init__(self):
        """
        This method is called when the class is instantiated and creates
        an object of the class and binds instance variables.

        :param speed: An integer of the Pokemon's speed
        :param attack: An integer of the Pokemon's attack_damage
        :param defence: An integer of the Pokemon's defence
        :param name: A string of the Pokemon's name
        :returns: None
        """
        PokemonBase.__init__(self, 9, "GRASS")
        self.attack = 5
        self.defence = 5
        self.speed = 7
        self.name = "Bulbasaur"

    def get_attack(self) -> int:
        """
        Returns the pokemon attack

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon attack value
        """
        return int(self.attack)

    def get_defence(self) -> int:
        """
        Returns the pokemon defence which adds one for every level past level 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon defence value
        """
        return int(self.defence)

    def get_speed(self) -> int:
        """
        Returns the pokemon speed which adds half the pokemon's level to it

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon speed value
        """
        return int(self.speed + self.level // 2)

    def get_name(self) -> str:
        """
        Returns the pokemon's name

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: string of pokemons name
        """
        return self.name

    def calculate_damage(self, attack: int) -> int:
        """
        Calculates the damage received by an incoming attack
        It has no return as the method takes off the damage done to the pokemon
        Takes attack value of opposing pokemon as an input

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param attack: int value of opposing pokemon attack value
        :return: None
        """
        if attack > self.defence + 5:
            self.set_hp(self.get_hp() - attack)
        else:
            self.set_hp(self.get_hp() - attack // 2)

    def effectiveness(self, poke_class) -> int:
        """
        This method overrides the base class method and an integer of the multiplier damage is returned dependant on
        the opposing Pokemon's class

        Best time complexity: O(1)
        Worst time complexity: O(n) where n is the number of pokemon types

        :returns: An integer of the multiplier damage is returned.
        """
        if poke_class == "WATER":
            return 2
        elif poke_class == "FIRE":
            return 0.5
        elif poke_class == "GRASS":
            return 1
        else:
            return 1

    def __str__(self) -> str:
        """
        Returns a description of the pokemon's stats in string format

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: String of pokemon's statss
        """
        return "{}'s HP = {} and level = {}".format(self.name, int(self.hp), self.level)


class Squirtle(PokemonBase):
    """
    This class creates an object of type 'Squirtle' which inherits from
    the PokemonBase class
    """

    def __init__(self):
        """
        This method is called when the class is instantiated and creates
        an object of the class and binds instance variables.

        :param speed: An integer of the Pokemon's speed
        :param attack: An integer of the Pokemon's attack_damage
        :param defence: An integer of the Pokemon's defence
        :param name: A string of the Pokemon's name
        :returns: None
        """
        PokemonBase.__init__(self, 8, "WATER")
        self.attack = 4
        self.defence = 6
        self.speed = 7
        self.name = "Squirtle"

    def get_attack(self) -> int:
        """
        Returns the pokemon attack which adds half the pokemon's level to it

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon attack value
        """
        return int(self.attack + self.level // 2)

    def get_defence(self) -> int:
        """
        Returns the pokemon defence which adds one for every level past level 1

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon defence value
        """
        return int(self.defence + self.level)

    def get_speed(self) -> int:
        """
        Returns the pokemon speed

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: int of pokemon speed value
        """
        return int(self.speed)

    def get_name(self) -> str:
        """
        Returns the pokemon's name

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: string of pokemons name
        """
        return self.name

    def calculate_damage(self, attack: int) -> int:
        """
        Calculates the damage received by an incoming attack
        It has no return as the method takes off the damage done to the pokemon
        Takes attack value of opposing pokemon as an input

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param attack: int value of opposing pokemon attack value
        :return: None
        """
        if attack > self.defence * 2:
            self.set_hp(self.get_hp() - attack)
        else:
            self.set_hp(self.get_hp() - attack // 2)

    def effectiveness(self, poke_class) -> int:
        """
        This method overrides the base class method and an integer of the multiplier damage is returned dependant on
        the opposing Pokemon's class

        Best time complexity: O(1)
        Worst time complexity: O(n) where n is the number of pokemon types

        :returns: An integer of the multiplier damage is returned.
        """
        if poke_class == "WATER":
            return 1
        elif poke_class == "FIRE":
            return 2
        elif poke_class == "GRASS":
            return 0.5
        else:
            return 1

    def __str__(self) -> str:
        """
        Returns a description of the pokemon's stats in string format

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: String of pokemon's statss
        """
        return "{}'s HP = {} and level = {}".format(self.name, int(self.hp), self.level)
