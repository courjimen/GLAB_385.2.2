# Movie DB Dictionary Project
import json
# Movie Dictionary
moviedb = {}

# - [ ] ADD NEW MOVIE:
def add_movie():
    # grabbed user data and saved into variables
    print("Adding a movie 🍿")
    title = input("Enter movie title: ")
    year = input("Enter movie year: ")
    genre = input("Enter movie genre: ")
    director = input("Enter movie director: ")
    actors = input("Enter the actor names(comma separated): ")

    # Used data to create a movie in the db
    moviedb[title] = {
        "year": year,
        "genre": genre,
        "director": director,
        "actors": actors.split(","),
    }

    print(f"Success 🎉: {title} added!")


# - [ ] EDIT A MOVIE:
def edit_movie():
    #Ask user what movie to edit
    title = input('Enter the movie title you want to update: ')
    try:
        # find movie to edit
        if title not in moviedb:
            # if can't find movie
            raise KeyError(f'{title} not found in database.')
        # show current info
        print(f'Current info for {title}')
        print(moviedb[title])

        # collect updated info from user
        year = input("Enter movie year (or press enter to keep current value(s)): ")
        genre = input("Enter movie genre (or press enter to keep current value(s)): ")
        director = input("Enter movie director (or press enter to keep current value(s)): ")
        actors = input("Enter the actor names(comma separated) (or press enter to keep current value(s)): ")

        #update with new info
        if year:
            moviedb[title]['year'] = year
        if genre:
            moviedb[title]['genre'] = genre
        if director:
            moviedb[title]['director'] = director
        if actors:
            moviedb[title]['actors'] = actors.split(",")

        print(f'{title} has been updated.')
    except Exception as e:
        print(f'❌ Error: {e}')

# - [ ] DELETE A MOVIE:
# declare delete movie function
def delete_movie():
    # ask user for input to get movie deletion
    title = input('What movie do you want to delete? ')
    # error handle if movie doesnt exist
    try:
       #if movie doesnt exist
       if title not in moviedb:
            raise KeyError(f'{title} not found in database.')

       del moviedb[title]

       print(f'Successfully deleted {title} from database ✅')
    except Exception as e:
        print(f'❌ Error: {e}')
     
# - [ ] VIEW ALL MOVIES:
def show_all():
    print("⭐️ All movies in database ⭐️")
    print("===============")
    for movie in moviedb:
        print(f"Movie: {movie}")
        for key, value in moviedb[movie].items():
            print(f"{key}: {value}")
        print("===============")


# - [ ] SEARCH MOVIES:
# define a search funct
def search_movies():
    #Prompted user for search criteria
    print('🔎 Search Movies in DB')
    criteria = input('Enter search criteria: ')
    matches = [] #stores saved data into array

    # loop through my db to find matches
    for movie, info in moviedb.items():
        #use control flow statement w/membership operator to find matches
        if criteria in movie or criteria in info['director'] or criteria in info['actors'] or criteria in info['genre']:
            matches.append(movie) # add title to list of found movies

        # if movie(s) found
        if matches:
            print(' ✅ Matches Found:')
            for movie in matches:
                print(f'{movie}: {moviedb[movie]}')
        # else no movies found
        else:
            print(' ❌ No matches found.')

# - [ ] save_data - put db into a file
def save_data():
    #ask file name to create
    filename = input('Enter the filename to save to: ')
    #open file, mode is write "w"
    with open(f'data/{filename}.json', 'w') as f:
        #dump data into external file
        json.dump(moviedb, f)
    print('🎉 Success, data saved.')

# - [ ] Load data - pull prev db file into this program
# define load_data func
def load_data():
    #ask user where to import file from
    location = input('Enter the name of import file: ')
    #try to open the file
    with open(f'data/{location}.json', 'r') as f:
        #save file content to temp database in app
        data = json.load(f)
        global moviedb
        moviedb = data
    #print success message
    print('✅ Successfully loaded your file!')

# - [ ] Data validation:
# save_data - put db to a file
# load_data - pull previous db file into this program
while True:
    print("==== 🎬 Movie Database MGMT System 🎬 ====")
    print("1. Exit")
    print("2. Add Movie")
    print("3. Show All Movies")
    print("4. Edit Existing Movie")
    print("5. Delete a Movie")
    print("6. Search a Movie")
    print("7. Save data to a file")
    print("8. Load data from a file")

    choice = input("What do you want to do? ")

    if choice == "1":
        print("Goodbye 👋🏾. Comeback soon!")
        break
    elif choice == "2":
        add_movie()
    elif choice == "3":
        show_all()
    elif choice == "4":
        edit_movie()
    elif choice == "5":
        delete_movie()
    elif choice == '6':
        search_movies()
    elif choice == '7':
        save_data()
    elif choice == '8':
        print('Loading dat from file')
    else:
        print(" ❌ Invalid Option. Please try again.")
