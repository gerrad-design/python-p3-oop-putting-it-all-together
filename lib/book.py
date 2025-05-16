#!/usr/bin/env python3

class Book:
    def __init__(self, title=None, page_count=None):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self.page_count = page_count

        self.title = title

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    
        