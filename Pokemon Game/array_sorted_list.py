"""
    Array-based implementation of SortedList ADT.
    Items to store should be of time ListItem.
"""

from referential_array import ArrayR
from sorted_list import *

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev, Graeme Gange and Antony Razzell'
__docformat__ = 'reStructuredText'

class ArraySortedList(SortedList[T]):
    """ SortedList ADT implemented with arrays. """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """ ArraySortedList object initialiser. """

        # first, calling the basic initialiser
        SortedList.__init__(self)

        # initialising the internal array
        size = max(self.MIN_CAPACITY, max_capacity)
        self.array = ArrayR(size)

    def reset(self):
        """ Reset the list. """
        SortedList.__init__(self)

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        return self.array[index]

    def __setitem__(self, index: int, item: ListItem) -> None:
        """ Magic method. Insert the item at a given position,
            if possible (!). Shift the following elements to the right.
        """
        if self.is_empty() or \
                (index == 0 and item.key <= self[index].key) or \
                (index == len(self) and self[index - 1].key <= item.key) or \
                (index > 0 and self[index - 1].key <= item.key <= self[index].key):

            if self.is_full():
                self._resize()

            self._shuffle_right(index)
            self.array[index] = item
        else:
            # the list isn't empty and the item's position is wrong wrt. its neighbourghs
            raise IndexError('Element should be inserted in sorted order')

    def __contains__(self, item: ListItem):
        """ Checks if value is in the list. """
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False

    def _shuffle_right(self, index: int) -> None:
        """ Shuffle items to the right up to a given position. """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def _shuffle_left(self, index: int) -> None:
        """ Shuffle items starting at a given position to the left. """
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

    def _resize(self) -> None:
        """ Resize the list. """
        # doubling the size of our list
        new_array = ArrayR(2 * len(self.array))

        # copying the contents
        for i in range(self.length):
            new_array[i] = self.array[i]

        # referring to the new array
        self.array = new_array

    def delete_at_index(self, index: int) -> ListItem:
        """ Delete item at a given position. """
        if index >= len(self):
            raise IndexError('No such index in the list')
        item = self.array[index]
        self.length -= 1
        self._shuffle_left(index)
        return item

    def index(self, item: ListItem) -> int:
        """ Find the position of a given item in the list. """
        pos = self._index_to_add(item)
        if pos < len(self) and self[pos] == item:
            return pos
        raise ValueError('item not in list')

    def is_full(self):
        """ Check if the list is full. """
        return len(self) >= len(self.array)

    def add(self, item: ListItem) -> None:
        """ Add new element to the list. """
        if self.is_full():
            self._resize()

        # find where to place it
        position = self._index_to_add(item)

        self[position] = item
        self.length += 1

    def _index_to_add(self, item: ListItem) -> int:
        """ Find the position where the new item should be placed. """
        low = 0
        high = len(self) - 1

        while low <= high:
            mid = (low + high) // 2
            if self[mid].key < item.key:
                low = mid + 1
            elif self[mid].key > item.key:
                high = mid - 1
            else:
                return mid

        return low

    def add_without_overwriting(self, item: ListItem) -> None:
        """
        This method is for adding a ListItem to the ArraySortedList in it's intended position

        Best time complexity: O(1)
        Worst time complexity: O(n) where N is the size of the ArraySortedList

        :param item: ListItem to be added
        """
        self.__setitem__(self._index_to_add(item), item)
        self.length += 1

    def get_last_item(self) -> ListItem:
        """
        This method is for popping the last ListItem in the list
        Best time complexity: O(1)
        Worst time complexity: O(1)

        :return ListItem: ListItem at the last index
        """
        item = self.__getitem__(len(self)-1)
        self.delete_at_index(len(self)-1)
        return item

    def add_last_index(self, item: ListItem) -> None:
        """
        This method is for adding a ListItem to the end of the list
        Best time complexity: O(1)
        Worst time complexity: O(1)

        :param item: ListItem to be added
        """
        if self.is_full():
            self._resize()

        self[len(self)] = item
        self.length += 1

    def add_first_index(self, item: ListItem) -> None:
        """
        This method is for adding a ListItem to the end of the list
        Best time complexity: O(n)
        Worst time complexity: O(n)
        where n is the size of the list

        :param item: ListItem to be added
        """
        if self.is_full():
            self._resize()

        self._shuffle_right(0)
        self.array[0] = item
        self.length += 1

    def __str__(self) -> str:
        """
        This method is for making a string of the list
        Best time complexity: O(n)
        Worst time complexity: O(n)
        where n is the size of the list

        :return: String created
        """
        string = ""
        for i in range(len(self)-1, -1, -1):
            if len(str(self.array[i]).lstrip("(")[:-4]) > 0:
                string += str(self.array[i]).lstrip("(")[:-4] + ", "    # Returns string without brackets and key
        string = string[:-2]    # Removes last comma of string
        return string
