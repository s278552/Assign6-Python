#!/usr/bin/env python3

# Created by Andrew Du-frigstad
# Created on June 17th 2021
# This program uses lists to print a border and user string
# Using lists to print a border around user strings

# len(list_words[counter]) is returning len of list, not words in list


def string_format(user_char, user_string, list_words):

    long_char = -1
    counter = 0
    long_word = max(list_words, key=len)
    long_char = len(long_word)

    print("{}{}{}".format(user_char, user_char, user_char*long_char))
    # For loop until counter reaches number of items in list
    for counter in range(len(list_words)):
        # If statement to see if len of list word is same as long word
        if len(list_words[counter]) < len(long_word):
            # While to give small words spaces to match longest word
            while len(list_words[counter]) < len(long_word):
                # Adding spaces so that the left wall is made
                len(list_words[counter])+" "
                if len(list_words[counter]) == len(long_word):
                    break
            # Print the final version of the list word
            print(user_char, (list_words[counter]), user_char)
        counter = counter + 1

    print("{}{}{}".format(user_char, user_char, user_char*long_char))


def main():

    list_words = []
    # Get the user inputs
    user_char = input("input your border character: ")
    user_string = input("Input your text: ")
    # Split the user string into words
    user_words = user_string.split()
    # Put the words into the list
    list_words.append(user_words)
    # Call the string_format function
    string_format(user_char, user_string, list_words)


if __name__ == "__main__":

    main()
