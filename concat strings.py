Hi# -*- coding: utf-8 -*-
"""
Write Python code that prompts for a word until the user enters an empty word. 
i.e., gives a carriage return immediately at the prompt 
The code outputs a string containing all the words entered, in the order they were entered, separated by spaces 
It makes things easy if you also have a space before the first word 
Example execution
Enter a word: Good
 
Enter a word: students
 
Enter a word: work
 
Enter a word: hard
 
Enter a word: 
 Good students work hard
 
Use a while loop 
Note that the empty string (but not a string of whitespace) counts as False and so provides a way to exit the loop

"""
inp = "initialize"
final = ""
while(inp):
    inp = input("Enter a word: ")
    final=final+" "+inp
    
print(final)
