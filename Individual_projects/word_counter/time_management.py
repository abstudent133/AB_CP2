#Time Page
#Project Analysis

#time function
#parameters: none
#actions:
#take in the current time
#formate it
#return it

#Pseudocode

#import time
import time

#time_func
def time_func():
#parameters: none
    #current time is the current time using .localtime from the time library
    current_time = time.localtime()
    #formated time is strftime function from the time library
    #return formated time