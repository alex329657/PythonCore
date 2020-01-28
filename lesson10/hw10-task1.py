from termcolor import colored

"""
Available colors: 
    grey
    red
    green
    yellow
    blue
    magenta
    cyan
    white
"""


class Marker:
    """class for color marker"""

    def __init__(self, color):
        self.color = color
        self.value = 100
        print("It's a " + self.color + " marker filled to 100%")

    def print(self, text):
        for symbol in text:
            if self.value > 0:
                if symbol != " ":
                    self.value -= 0.5
                print(colored(symbol, self.color), end="")
            else:
                break
        print()
        print("Ink level is " + str(self.value))


class Newmarker(Marker):
    """class for color refillable marker"""

    def refill(self, fill_value):
        self.value += fill_value
        print("Marker refilled to " + str(self.value))


def main():

    str = input("Input string: ")
    color_simple = input("Input color of simple marker: ")
    color_refillable = input("Input color of refillable marker: ")
    refill_level = int(input("Input level of refill in percents: "))

    simple_marker = Marker(color_simple)
    while simple_marker.value > 0:
        simple_marker.print(str)

    refillable_marker = Newmarker(color_refillable)

    while refillable_marker.value > 0:
        refillable_marker.print(str)
    refillable_marker.refill(refill_level)
    while refillable_marker.value > 0:
        refillable_marker.print(str)


if __name__ == "__main__":
    main()
