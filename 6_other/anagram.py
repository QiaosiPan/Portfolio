"""
File: anagram.py
Name: QiaosiPan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        ####################
        # user type '-1' to quit the process
        if word == EXIT:
            print('Exit "Anagram Generator"')
            break
        # user input a word to start searching
        else:
            find_anagrams(word)
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    lst = []
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            lst.append(line)
    return lst


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    dict_lst = read_dictionary()        # store all words in file as a list
    anagrams = []
    print('Searching...')
    find_anagrams_helper(s, '', len(s), [], anagrams, dict_lst)
    print(len(anagrams), 'anagrams: ', anagrams)


def find_anagrams_helper(s, sub_s, length, index, anagrams, dictionary):
    # base case: store anagrams in a list & print it
    if len(sub_s) == length and sub_s not in anagrams and sub_s in dictionary:
        anagrams.append(sub_s)
        print('Find: ', sub_s)
        print('Searching...')
    else:
        for i in range(length):
            # index is used to avoid the same letters keep show up
            if i in index:
                pass
            else:
                # Choose
                index.append(i)
                sub_s += s[i]
                # Explore
                # check prefix first: as sub_s find the same prefix of any word in dict, start recursive
                if has_prefix(sub_s, dictionary):
                    find_anagrams_helper(s, sub_s, length, index, anagrams, dictionary)
                # if sub_s is not any prefix of word in dict, stop searching this set of sub_s
                else:
                    pass
                # un-Choose
                index.pop()
                sub_s = sub_s[:-1]


def has_prefix(sub_s, dictionary):
    """
    :param sub_s:
    :param dictionary:
    :return:
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
