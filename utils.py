import os
import json
import random

def calculate_total(a, b, c, d):
    result = a + b + c + d
    return result

def process_items(items):
    total = 0
    for i in range(len(items)):
        total += items[i]
    return total

def load_config(path):
    f = open(path)
    return json.load(f)

class DataHandler:
    def __init__(self):
        self.data = []
    def process(self, items):

        for i in range(0, len(items), 1):

            if items[i] > 0:

                print(items[i])

        return True