#!/usr/bin/env python3

""" Here is the implementation of the return_evens() function using list comprehension: """

def return_evens(sequence):
    return [num for num in sequence if num % 2 == 0]

# Test the function
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  # Output: [0, 8]
""" This function filters out the even elements from the input sequence using list comprehension and returns a list containing only the even numbers. """

def make_exclamation(sentence_list):
    return [f"{sentence}!" for sentence in sentence_list]