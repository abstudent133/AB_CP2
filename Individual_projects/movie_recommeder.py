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
import csv
#movie_list is a list of all the dictionaries of all the movies
#try
try:
    #open the file as movie
    with open("Individual_projects/Movies list - Sheet1 (1).csv", "r") as movies:
        #content is read movie filecontent = csv.reader(csv_file)
        content = csv.reader(movies)
        #remove the header from iteration
        header = next(content)
        movie_list = []
        working = True
        #formate a way to add to the movie_list
        #for each line in the movie file
        for line in content:
            #add that new formated dictionary to the movie list
            movie_list.append({header[0]: line[0], header[1]: line[1], header[2]: line[2], header[3]: line[3], header[4]: line[4], header[5]: line[5]})
#except
except FileNotFoundError:
    #print a message that this site isn't working at the moment and apoligize for the inconvience
    working = False
    print("Sorry for the incovienece, but this site isn't working at the moment. It will be repaired as soon as possible.")

#search function
def search(movie_list, catigory):
    #intake the catigory dictionary list
    #new_movie_list is an empty list
    new_movies = []
    #searching is asking the user which thing they want to search for(make sure to make it lowercase and remove whitespace)
    searching = input(f"What is is you are searching for in {catigory} catigory: ").lower()
    #for i in movie list:
    for movie in movie_list:
        #if searching is in the searching catigory:
        if catigory in movie and searching in movie[catigory].lower():
            #add this movie to the new_movie_list
            new_movies.append(movie)
    #return the new_movie list
    return new_movies

#length search function
def length(movie_list):
    #intake the movie list
    #new_movie_list is an empty list
    new_movies = []
    #reference is ask user about the length as a reference point
    reference = int(input("What is your point of reference for the time filter: "))
    #more_less is asking the user if they want a movie to be more or less than the reference point
    more_less = input("Would you like to have movies longer(1) or shorter(2) than your point of reference. Please input the number of your choice here: ")
    #if more_less is more
    if more_less == "1":
        #for movie in movie_list:
        for movie in movie_list:
            #if length in movie is more than reference:
            if int(movie["Length (min)"]) > reference:
                #add movie to new_movie_list
                new_movies.append(movie)
    #elif more_less is less
    elif more_less == "2":
        #for movie in movie_list:
        for movie in movie_list:
            #if length in movie is less than reference:
            if int(movie["Length (min)"]) < reference:
                #add movie to new_movie list
                new_movies.append(movie)
    #return new movie list
    return new_movies

#formating function
def formating(movie_list):
    #intake movie list
    #formated is an empty string
    formated = f"Movie Recommendations for You:\n"
    #for movie in movie list:
    for movie in movie_list:
        #for key in movie.keys():
        for key in movie.keys():
            #format it and add it to the formated list
            formated += f"{key}: {movie[key]}\n"
        formated += "\n"
    #return  formated
    return formated

#main function
def main(movie_list):
    original_movies = movie_list.copy()
    #intake the movie_list
    #while true
    while True:
        movie_list = original_movies.copy()
        #display all filter options
        print("Your filter options are:\n" \
        "1. Director\n" \
        "2. Genre\n" \
        "3. Actor\n" \
        "4. Length\n" \
        "You can pick as many as you want.")
        #nums is asking the user which filters they want based on corrisponding numbers and to put a space between each
        nums = input("Input your filter choices here: ")
        #if "1" in nums:
        if "1" in nums:
            #movie_list = search(movie_list, director) 
            movie_list = search(movie_list, "Director")
        #if "2" in nums:
        if "2" in nums:
            #movie_list = search(movie_list, genre)
            movie_list = search(movie_list, "Genre")
        #if "3" in nums:
        if "3" in nums:
            #movie_list = search(movie_list, actor)
            movie_list = search(movie_list, "Notable Actors")
        #if "4" in nums:
        if "4" in nums:
            #movie_list = length(movie_list)
            movie_list = length(movie_list)
        #if none of the numbers were in nums then
        if "1" not in nums and "2" not in nums and "3" not in nums and "4" not in nums:
            #tell user that that was an invalid input
            print("Sorry that was an invalid input.")
        #print(format(movie_list)) 
        if movie_list != []:
            print(formating(movie_list))
        else:
            print("Sorry, there are no movies that fit these filters.")
        #quit = ask user if they would like to quit
        quit_choice = input("Would you like to quit? If you would like to quit put 1 and if you wouldn't then put 2: ")
        #if yes then break
        if quit_choice == "1":
            break
        #else continue
        else:
            continue
    
if working == True:
    main(movie_list)







