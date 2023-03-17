"""
File that contains the class PokeTeam which creates a team of Pokemon's chosen by the user

__author__ = "Ben 10"
__last_modified__ = "1.05.2022"
"""

from pokemon import *
from GlitchMon import *
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList
from sorted_list import ListItem
from typing import TypeVar, Generic

T = TypeVar('T')


class PokeTeam:
    """
    This class creates an PokeTeam which inherits the amount of each Pokemon chosen by the user
    """
    def __init__(self, name):
        """
        Constructor for the class, binds instance variables to given values and will be changed
        depending on the user's input

        :param name: None, can be changed into a string of the user's name
        :param team: None, can be changed into an array of chosen Pokemons
        :param battle_mode: None, can be changed into an integer of the selected battle mode
        :param limit: An integer of the highest amount of Pokemon available to be taken into a team
        :returns: None
        """
        self.name = name
        self.team = None  # Array
        self.limit = 6
        self.battle_mode = 0

    def __str__(self) -> str:
        """
        formats the team into a string

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return: The team and every pokemon in it in string format
        """
        return str(self.team)

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """
        This method prompts the user to input what pokemon they want in their team.
        They choose from the four pokemon that are:
        Charmander, Bulbasuar, Squirtle and MissingNo

        Best time complexity: O(1)
        Worst time complexity: O(n)

        Where 'n' is the number of times a user inputs an invalid team.

        :param battle_mode: the way a user wants their team arranged
        :param criterion: This criterion is for optimised battle mode
        :return: None
        """
        if battle_mode < 0 or battle_mode > 2:
            raise ValueError("Invalid battle mode. Try again")
        self.battle_mode = battle_mode
        print("Howdy Trainer! Choose your team as C B S")
        print("where C is the number of Charmanders")
        print("      B is the number of Bulbasaurs")
        print("      S is the number of Squirtles")
        print("      M is if you want a GlitchMon")

        team_order = input().split()  # Putting inputted string in to a list
        team_order = [int(value) for value in team_order]  # Turning strings in to type int
        charm = team_order[0]
        bulb = team_order[1]
        squir = team_order[2]
        missing = team_order[3]

        # this checks to make sure the team is only 6 and that there is max 1 MissingNo
        if sum(team_order) > self.limit or missing > 1:
            self.choose_team(battle_mode, criterion)
        else:
            self.assign_team(charm, bulb, squir, missing, criterion)

    def assign_team(self, charm: int, bulb: int, squir: int, missing: int, criterion: str) -> None:
        """
        This method is for creating the team after the user has been prompted to input what pokemon
        they want on their team. It creates the teams in a way specified by the battle mode

        Best time complexity: O(n)
        Worst time complexity: O(n)

        where 'n' in both cases is the largest number of any pokemon input

        :param charm: number of charmander's in the team
        :param bulb: number of bulbasuar's in the team
        :param squir: number of squirtle's in the team
        :param missing: number of MissingNo's in the team
        :param criterion: type of criterion used for the optimised battle
        :return: None
        """
        if self.battle_mode == 0:
            self.team = ArrayStack(self.limit)

            # Creating missing objects
            for i in range(missing):
                self.team.push(MissingNo())

            # Creating Squirtle objects
            for i in range(squir):
                self.team.push(Squirtle())

            # Creating Bulbasaur objects
            for i in range(bulb):
                self.team.push(Bulbasaur())

            # Creating Charmander objects
            for i in range(charm):
                self.team.push(Charmander())

        elif self.battle_mode == 1:
            self.team = CircularQueue(self.limit)

            # Creating Charmander objects
            for i in range(charm):
                self.team.append(Charmander())

            # Creating Bulbasaur objects
            for i in range(bulb):
                self.team.append(Bulbasaur())

            # Creating Squirtle objects
            for i in range(squir):
                self.team.append(Squirtle())

            # Creating Missing object
            for i in range(missing):
                self.team.append(MissingNo())

        elif self.battle_mode == 2:
            self.team = ArraySortedList(self.limit)
            # Creating Charmander objects
            for i in range(charm):
                self.team.add_without_overwriting(self.generate_list_item(Charmander(), criterion))

            # Creating Bulbasaur objects
            for i in range(bulb):
                self.team.add_without_overwriting(self.generate_list_item(Bulbasaur(), criterion))

            # Creating Squirtle objects
            for i in range(squir):
                self.team.add_without_overwriting(self.generate_list_item(Squirtle(), criterion))

            # Creating Missing object
            for i in range(missing):
                self.team.add_first_index(self.generate_list_item(MissingNo(), criterion))

    def generate_list_item(self, pokemon: T, criterion: str) -> ListItem:
        """
        This method creates and returns a ListItem that has a pokemon and a key
        which corresponds to its criterion.

        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param pokemon: the pokemon that will be stored in the listitem object
        :param criterion: the criterion that optimised battle will sort the list of items by
        :return: a listitem that can be stored in an ArraySortedList
        """
        if criterion == "hp":
            return ListItem(pokemon, pokemon.get_hp())
        elif criterion == "attack":
            return ListItem(pokemon, pokemon.get_attack())
        elif criterion == "defence":
            return ListItem(pokemon, pokemon.get_defence())
        elif criterion == "lvl":
            return ListItem(pokemon, pokemon.get_level())
        elif criterion == "speed":
            return ListItem(pokemon, pokemon.get_speed())
