import re


file= input("enter your file: ")
word= input("enter a word: ")
with open(file,"r") as file.txt:

    for line in file.txt:

        if re.search(word, line):

            print(line)


