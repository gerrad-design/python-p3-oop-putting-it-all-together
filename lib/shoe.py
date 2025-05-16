#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand=None, size=None):
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self.size = size

        self.brand = brand
        self.condition = None

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
