# Question 4
# DO NOT USE THE WORD input ANYWHERE!

# We provide class Rectangle and starter code for class RectangleCollection.

# Complete class RectangleCollection, which has one list instance variable, rectangles,
# that should initially refer to an empty list. Write a method add_rectangle that takes a Rectangle as a parameter and appends it to the rectangles list.
# Write a method get_same_area_rects that takes a number as a parameter and returns a list of all Rectangles from the rectangles list that have that area.


from typing import List


class Rectangle:
    """ A rectangle with a width and height. """

    def __init__(self, w: int, h: int) -> None:
        # """Create a new rectangle of width w and height h.

        # >>> r = Rectangle(1, 2)
        # >>> r.width
        # 1
        # >>> r.height
        # 2
        # """

        self.width = w
        self.height = h

    def get_area(self) -> int:
        # """Return the area of this rectangle.

        # >>> r = Rectangle(10, 20)
        # >>> r.get_area()
        # 200
        # """

        return self.width * self.height


class RectangleCollection:

    def __init__(self) -> None:
        # """
        # >>> rc = RectangleCollection()
        # >>> rc.rectangles
        # []
        # """
