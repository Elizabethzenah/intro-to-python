class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        result = (22 / 7 * self.radius ** 2 * 2 + 2 * 22 / 7 * self.height * self.radius)
        print(f"Area is : {result}")

    def volume(self):
        result = 22 / 7 * self.radius ** 2 * self.height
        print(f"Volume is : {result}")

    def print_details(self):
        print(f"Radius is {self.radius} and Height is {self.height}")
