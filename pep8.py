"""
Using PEP8 Standards helps working with teams easily 
also it helps in Debugging code more convinient 

"""




import sys
import random 
"""
By convention all the imports must be in top 
most area 
also dont , coma multiple imports in a single line 

"""

"""
gernerally function names and variables names 
are most conventionally underscore words and
each word seperated by an underscore 

@example

def one_two(self):
    return my_word


classes always have first letter capitalization .
"""
def foo_bar(arg1, arg2, arg3, arg4):  
    return arg1, arg2, arg3, arg4
    # there should be a space btw comas and operators


# there shoudl be 2 Blank lines between top level function ..ie which are wwithout a class 
def bar(*args):
    return 2+2


# there should be two classes and other methods or funcs
class Treehouse:  
    def one(self):
        return 1 

# there shoudl be a blank line btw  2 func inside a class 
    def two(self):
        return 2

"""
Another rule is keep Decent tabs btw 

"""


"""
Arguments that are quite longer 
need to be broken down into multiple lines 

"""
 a, b, c, d = foo_bar(
     "a long string", 
     "antoher argument", 
     "yet another long String", 
     "okay just another string")

"""
Single letter variables names creates huge issues
in large application Code bases 

"""

alpha_str, beta_str, gama_str, delta_str = foo_bar(
    "a long string", 
     "antoher argument", 
     "yet another long String", 
     "okay just another string")


variable_name = "a example str"  #inline comments  shoud have 2 spaces from code 