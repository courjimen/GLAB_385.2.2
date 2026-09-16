# # Movie DB Dictionary Project

# Movie Dictionary
moviedb = {}


# - [ ] Add a new movie:
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


# - [ ] Edit a movie:
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

# - [ ] Delete a movie:
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
     
# - [ ] View all movies:
def show_all():
    print("⭐️ All movies in database ⭐️")
    print("===============")
    for movie in moviedb:
        print(f"Movie: {movie}")
        for key, value in moviedb[movie].items():
            print(f"{key}: {value}")
        print("===============")


# - [ ] Search movies:

# - [ ] Save and load data:

# - [ ] Error handling:

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
        print('Searching for movie')
    elif choice == '7':
        print('Saving data to file')
    elif choice == '8':
        print('Loading dat from file')
    else:
        print(" ❌ Invalid Option. Please try again.")
