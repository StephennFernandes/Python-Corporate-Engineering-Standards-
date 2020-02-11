import logging 



    logging.info("you wont see this")
    logging.warn("ERROR! code ")

"""
If you want to log into a specific file 
consistent way to log
"""

logging.basicConfig(filename='app.log', level=logging.DEBUG)

"""
You can put the .log file in whichever directory 
you want to log the file 

the level specifies the level of logging 

There are 6 levels of Logging:
    
    # CRITICAL   ( to catch errors thats are very crtical )
    
    # ERROR  ( when things go wrong .. to catch the error )
    
    # WARNING  ( to remember any exception , or other imp warnings )
    
    # INFO  ( anything that need to monitor)
    
    # DEBUG  ( debug information )
    
    # NOTSET  ( not used often )

"""
logging.info('{} : {} : {}'.format(var1, var2, var3))

"""
Similarly you can log other logs in the .log file 
and cat the file to check logs 
you can also run specific sed or linux regex cmds 
to see only specific Logs if you have a junk of logs


you can also add Date-time formats , and System user name in the logs
to create a more spohicticated system logs for applications

"""


