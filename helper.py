import os
import json
import random
import math

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]

    return total / len(numbers)

def read_file(path):
    file = open(path)
    data = file.read()
    return data


class ItemProcessor:
    def process(self, items):
        result = []
        for i in range(0, len(items), 1):
            if items[i] > 0:

                result.append(items[i])

        return result