# #1
# #Write a program that prompts the user to enter a file name, reads the contents
# #of the file and prints it to the screen
#
# newprogram = raw_input("Enter a file name. ")
# file_handle = open(newprogram, 'r')
# contents = file_handle.read()
# file_handle.close()
# print(contents)
#
# ############################################################################
# ############################################################################
#
# #2
# #Write a program that prompts the user to enter a file name, then prompts the
# #user to enter the contents of the file, and then saves the content to the file.
#
# newfile = input("Enter another file name. ")
# dacontents = input("Ok, now give me the contents of the file. ")
# file_handle = open(newfile, 'w')
# file_handle.write(dacontents)
# file_handle.close()
#
# ############################################################################
# ############################################################################
#
# #3
# #Write a program that prompts the user to enter a file name, then prints the
# #letter histogram and the word histogram of the contents of the file.
#
# newfile1 = raw_input("Enter another file name. ")
# file_handle = open(newfile1, 'r')
# contents = file_handle.read()
# def letter_histogram(word):
#     char_count = {}
#     for char in word:
#         if char not in char_count:
#             char_count[char] = 1
#         else:
#             char_count[char] += 1
#     return char_count
# print(letter_histogram(contents))
#
# def word_histogram(sentence):
#     word_count = {}
#     word_list = sentence.split(" ")
#     for words in word_list:
#         if words not in word_count:
#             word_count[words] = 1
#         else:
#             word_count[words] += 1
#     return word_count
# print(word_histogram(contents))
# file_handle.close()

############################################################################
############################################################################

#4
#Write program that takes a JSON file name as input and plots the X,Y data.
#Exchange JSON data with others to test your program more thoroughly.
import json
from matplotlib import pyplot as plt

with open('testplotpoints.py', 'r') as file_handle:
    testplotpoints = json.load(file_handle)

plt.plot(testplotpoints)
plt.show()
#not complete. Still need to finish this problem
