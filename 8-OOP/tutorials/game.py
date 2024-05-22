"""
Colour, X, Y & Z coordinates for the geometric centre of the shape. 
Dimensions of the 2D cross-section through the horizontal plane of the centre of the 3D shape and return the area and perimeter. 
Return the 3D surface area, volume, and surface count.
"""


class Object:
    def __init__(colour, x, y, z):
        self.colour = colour
        self.x = X
        self.y = y
        self.z = z


def main():
    object = get_object()
    print(f"{object.colour}")


def get_object():
    colour = input("Colour: ")
    x = input("X: ")
    y = input("Y: ")
    z = input("Z: ")
    object = Object(colour, x, y, z)
    return object


if __name__ == "__main__":
    main()
