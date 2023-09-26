"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        if frequencies.get(str(i)):
            frequencies[str(i)] += 1
        else:
            frequencies[str(i)] = 1
    # Your code goes here
    return frequencies