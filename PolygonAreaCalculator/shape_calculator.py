class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        """
        Returns area (width * height)
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Returns perimeter (2 * width + 2 * height)
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """
        Returns diagonal ((width ** 2 + height ** 2) ** .5)
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """
        Returns a string that represents the shape using lines of "*".
        The number of lines should be equal to the height and the number
        of "*" in each line should be equal to the width. There should be a new
        line (\n) at the end of each line. If the width or height is larger than 50,
         this should return the string: "Too big for picture.".
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        """
        Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        """
        try:
            inside_with = self.width // shape.width
            inside_height = self.height // shape.height
            return inside_with * inside_height
        except ZeroDivisionError:
            return -1

    def __str__(self) -> str:
        """
        If an instance of a Rectangle is represented as a string, it should look like:
        Rectangle(width=5, height=10)
        """
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """
    The Square class should be a subclass of Rectangle. When a Square object is created,
    a single side length is passed in.
    The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
    The Square class should be able to access the Rectangle class methods but should also contain a set_side method.
    """

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def __str__(self) -> str:
        """
        If an instance of a Square is represented as a string, it should look like: Square(side=9)
        """
        return f"Square(side={self.height})"
