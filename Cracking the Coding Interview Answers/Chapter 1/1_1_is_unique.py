# -----------------------------------------------------------
# Python3 implementation
# Cracking the Coding Interview Book
# 1.1 Is Unique
# Question: Implement an algorithm to determine if a string
# has all unique characters. What if you cannot use additional
# data structures?
# -----------------------------------------------------------
import unittest
# -----------------------------------------------------------

# Approach 1: Using a hashtable
# -----------------------------------------------------------
def normalize_str(my_string):
    my_string = my_string.replace(" ", "")
    return my_string.lower()

def is_unique_using_hashtable(my_string):
    # Iterate through the string, populate the dictionary where Keys() = each unique letter, and Values() = the frequency of each letter
    my_dict = {}
    for char in my_string:
        if char in my_dict.keys():
            return False
        else:
            my_dict[char] = 1
    return True

# -----------------------------------------------------------
# Approach 2: Using no additional data structures
# -----------------------------------------------------------
def is_unique_no_additional_datastructure(my_string):
    # If there are multiple occurrences of a letter in the string, the string is not unique.
    # Iterate through my_string. If there are multiple occurrences of a letter in my_string, increment the counter

    my_string_normalized = normalize_str(my_string)
    counter = 0
    for letter in my_string_normalized:
        if my_string_normalized.count(letter) > 1:
            counter += 1
        else:
            continue
    # After iterating the string, check the counter to see if it is greater than 0.
    if counter > 0:
        return False
    else:
        return True

# -----------------------------------------------------------
# Unit Tests
# -----------------------------------------------------------

class Test(unittest.TestCase):
    unique_string = "asDf"
    non_unique_string = "non unique"

    def test_normalize_str(self):
        self.assertTrue(normalize_str(Test.unique_string), "asdf")
        self.assertTrue(normalize_str(Test.non_unique_string), "nonunique")

    def test_is_unique_using_hashtable(self):
        self.assertTrue(is_unique_using_hashtable(Test.unique_string), True)
        self.assertFalse(is_unique_using_hashtable(Test.non_unique_string), False)

    def test_is_unique_no_addditional_datastructure(self):
        self.assertTrue(is_unique_no_additional_datastructure(Test.unique_string), True)
        self.assertFalse(is_unique_no_additional_datastructure(Test.non_unique_string), False)

if __name__ == "__main__":
    unittest.main()
