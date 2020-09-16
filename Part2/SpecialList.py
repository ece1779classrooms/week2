# Question 3
# SpecialList is a class that has two instance variables value_list and size. value_list refers to a list,
# and size stores an integer representing the maximum number of items that can be stored in the list.


class SpecialList:
    # """A list that can hold a limited number of items."""

    def __init__(self, size: int) -> None:
        # """Initialize this special list to hold at most size items.

        # >>> L = SpecialList(10)
        # >>> L.size
        # 10
        # >>> L.value_list
        # []
        # """
        # # complete this code

    def push_value(self, new_value: object) -> None:
        # """Append new_value to this list, if there is enough space in the list
        # according to its maximum size. If there is insufficient space, new_value
        # should not be added to the list.

        # >>> L = SpecialList(2)
        # >>> L.push_value(3)
        # >>> L.push_value(4)
        # >>> L.push_value(5)
        # >>> L.value_list
        # [3, 4]
        # """
        # # complete this code

    def pop_most_recent_value(self) -> object:
        # """Return the value added most recently to value_list and remove it from
        # the list.

        # Precondition: len(self.value_list) != 0

        # >>> L = SpecialList(10)
        # >>> L.push_value(3)
        # >>> L.push_value(4)
        # >>> L.value_list
        # [3, 4]
        # >>> L.pop_most_recent_value()
        # 4
        # """
        # # complete this code

    def compare(self, other: "SpecialList") -> int:
        # """Return 0 if both SpecialList objects contain the same number
        # of items. Return 1 if self contains more items than other.
        # Return -1 if self contains fewer items than other.
        # """
        # # complete this code
