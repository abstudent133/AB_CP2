#Time Page
#Project Analysis

#time function
#parameters: none
#actions:
#take in the current time
#formate it
#return it

#Pseudocode

#import datetime
from datetime import datetime

#time function
#parameters: none
def time_func():
    #now is the time it is now
    now = datetime.now() 
    #formatted time is the time in the correct formate
    formatted_time = now.strftime("%B %d, %Y at %I:%M %p")
    #return formatted time
    return formatted_time