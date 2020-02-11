"""
A doc string is a documentation added at the begining of a code 
to document what that specific class or Function is doing

"""

def does_something(arg):
    if isinstance(arg, (int , float)):
        return arg + 10
    
    elif isinstance(arg, str, int):
        return str + 3
    else:
        raise typeError("docs_something takes only int str or float")

"""
Suppose this code was given in 
the form of a library 

it should be able to clearly explain without looking into the lib code 

"""


def doc_str_func(arg):
    """ takes one argument and passes back
        response based on the input type"""
    pass

"""
How doc String works 
when you import the code 
and use the help() function with help(doc_string.doc_str_func)
it will respond the doc string ... 
giving explaination on the func 

"""
