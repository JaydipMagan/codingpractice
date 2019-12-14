# Find longest word in dictionary that is a subsequence of a given string
# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
#
# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.
#
# Note: D can appear in any format (list, hash table, prefix tree, etc.
#
# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"
#
# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
#
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
#
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

import collections #to create default dictionary
import copy #to create a deepcopy of the dictionary

#function returns longest word from given words that is a subset of the given string
# time complexity o(s+ w*c) = o(w*c) assuming deep copy takes o(1)
# space o(2d) = o(d)  d = size of string since dictionary will store indexes of each character. 2d since we have to make a deep copy for each word
def longestWordSubsquenceOfString(string,words):
    letter_dict = collections.defaultdict(list)

    #get dictionary where each character stores which indexes it occurs in the string
    # o(s)  s = size of string
    for i in range(0,len(string)):
        letter_dict[string[i]].append(i)

    current_largest_word = "" # keep track of largest word

    #o(w)  w = amount of words in list
    for word in words:
        temp_dict = copy.deepcopy(letter_dict) # make a deep copy instead of shallow copy
        current_index = 0 # keep track of index
        list_compared_index = [] # list of indexes that are compared
        #o(c)  c = amount of characters in word
        for character in word:
            #if character is not in string then word can't be subset
            if character not in temp_dict:
                break
            # check if the character isn't used up
            if len(temp_dict[character])!=0:
                list_of_indexes = temp_dict[character]# gets the list of indexes for the character
                first_index = list_of_indexes[0]
                if first_index >= current_index: #check if the index is greater this tells the program the character appears after the previous one
                    list_compared_index.append(first_index) # add character to list
                    temp_dict[character].remove(first_index) # remove so it can't be used again for comparison
                    current_index = first_index # update the index to compare
                else:
                    # index of the character is less than this means the sequence is broken
                    break
        # check if size of the word is same as amount of indexes compared and if word is the new largest word
        if len(list_compared_index) == len(word) and len(word)>len(current_largest_word):
            current_largest_word = word

    return current_largest_word

print("largest word subset of string is "+longestWordSubsquenceOfString("abppplee", ["able", "ale", "apple", "bale", "kangaroo"]))
