"""
the Python debugger enabales us to Debug the python code
while to script is actually been executing
"""

import pdb 

my_list = [5, 2, 1] 

pdb.set_trace()

"""
the pdb console opens up after the python interpreter is executed
and the pdb console shows which line you are and whats about to be 
printed next 

you can also call and see all your variables 

hitting n will continue to the next line  

to prevent pdb to come up line after line ... to continue it
like a normal execute hit c 


once code is ready to hit production , remove the pdb code and commit

YOU can also use it in one line , conventional way of using pdb

import pdb ; pdb.set_trace()

"""

