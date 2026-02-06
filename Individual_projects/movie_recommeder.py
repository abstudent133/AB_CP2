#AB 1st Move Recommender
#Project Analysis
#access
#action
#get csv file
#convert each line into a dictionary
#put each dictionary in a list

#filters
#actions
#ask for which filters they want
#formate it into a list
#ask about what they are searching for for each filter chosen
#return that list

#genre search
#intake the requesed genre and the list of dictionaries
#actions
#search each dictionary genre
#if it does match the genre then add to the list of matches

#director search
#intake the requested genre and lit of dictionaries
#actions
#search each dictionary director
#add to list

#actors search
#intake the requested actor name and the list of dictionaries
#actions
#search each dictionary actors
#add to list

#length search
#intake more or less, length, and dictionary list
#action
#search each dictionary for length
#if length more or less than length
#add to list

#Pseudocode
#import csv
#movie_list is a list of all the dictionaries of all the movies
#try
    #open the file as movie
        #content is read movie file
        #remove the header from iteration
        #formate a way to add to the movie_list
        #for each line in the movie file
            #add that new formated dictionary to the movie list
#except
    #print a message that this site isn't working at the moment and apoligize for the inconvience

#search function
    #intake the catigory dictionary list
    #new_movie_list is an empty list
    #searching is asking the user which thing they want to search for(make sure to make it lowercase and remove whitespace)
    #for i in movie list:
        #if searching is in the searching catigory:
            #add this movie to the new_movie_list
        #else
            #coninue
    #return the netw_movie list


