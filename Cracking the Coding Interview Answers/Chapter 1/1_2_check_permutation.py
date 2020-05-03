# -----------------------------------------------------------
# Python3 implementation
# Cracking the Coding Interview
# 1.2 Check Permutation
# Question: Given two strings, write a method to decide if
# one is a permutation of the other e.g. cat ==> tac
# -----------------------------------------------------------
import unittest
# -----------------------------------------------------------

# -----------------------------------------------------------
# Approach 1 - Using Hashtable
# -----------------------------------------------------------

def check_permutation_using_hashtable(my_string1, my_string2):
    # Create a dictionary with Keys() = characters, Values() = number of times it occurred in both strings
    # For String 1: Populate Values for each Key in the dictionary
    # For String 2: Remove Values for each key in the dictionary
    # If all Values in the dictionary are 0 at the end, then we have a permutation

    my_dict = {}
    # Quick check. If length of each string are not equal, then it is not a permutation.
    if len(my_string1) != len(my_string2):
        return False

    # Iterate string 1 populating key/values
    for letter in my_string1:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
        # print("round1 {}".format(my_dict.items()))

    # Iterate string 2 populating the same dictionary key/values
    for letter in my_string2:
        if letter in my_dict:
            my_dict[letter] -= 1
        else:
            my_dict[letter] = 1
        # print("round2 {}".format(my_dict.items()))

    # If Values are > 0 then the strings are not permutations of each other
    for key, value in my_dict.items():
        if value > 0:
            return False
        else:
            return True

# -----------------------------------------------------------
# Approach 2 - Using No Additional Datastructures 
# -----------------------------------------------------------
        
def check_permutation_using_count(my_string1, my_string2):
    is_true = False
    for letter in my_string1:
        if my_string1.count(letter) == my_string2.count(letter):
            is_true = True
        else:
            is_true = False
    if is_true == True:
        return True
    else:
        return False

# -----------------------------------------------------------
# Unit Tests
# -----------------------------------------------------------

class Test(unittest.TestCase):
    # permutation_string = "hannaha"
    # non_permutation_string = "no permutation"
    permutation_string = "hannah"
    non_permutation_string = "non permutation"

    def test_check_permutation_using_hashtable(self):
        self.assertTrue(check_permutation_using_hashtable(Test.permutation_string, Test.permutation_string), True)
        self.assertFalse(check_permutation_using_hashtable(Test.permutation_string, Test.non_permutation_string), False)

    def test_check_permutation_using_count(self):
        self.assertTrue(check_permutation_using_count(Test.permutation_string, Test.permutation_string), True)
        self.assertFalse(check_permutation_using_count(Test.permutation_string, Test.non_permutation_string), False)

if __name__ == "__main__":
    unittest.main()
