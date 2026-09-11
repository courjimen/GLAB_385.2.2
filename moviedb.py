# # Movie DB Dictionary Project

# Movie Dictionary
moviedb = {}
# - [ ] Add a new movie: 
def add_movie():
      # grabbed user data and saved into variables
      print("Adding a movie 🍿")
      title = input('Enter movie title: ')
      year = input('Enter movie year: ')
      genre = input('Enter movie genre: ')
      director = input('Enter movie director: ')
      actors = input('Enter the actor names(comma separated): ')

      # Used data to create a movie in the db
      moviedb[title] = {
            'year': year,
            'genre': genre,
            'director': director,
            'actors': actors.split(",")
      }

      print(f'Success 🎉: {title} added!' )

# - [ ] Edit a movie: 

# - [ ] Delete a movie: 

# - [ ] View all movies:
def show_all():
      print('⭐️ All movies in database ⭐️')
      print('===============')
      for movie in moviedb:
        print(f"Movie: {movie}")
        for key, value in moviedb[movie].items():
            print(f"{key}: {value}")
        print('===============')
# - [ ] Search movies: 

# - [ ] Save and load data: 

# - [ ] Error handling: 

# - [ ] Data validation: 
while True:
    print('==== 🎬 Movie Database MGMT System 🎬 ====')
    print('1. Exit')
    print('2. Add Movie')
    print('3. Show All Movies')

    choice = input('What do you want to do? ')

    if choice == '1':
            print('Goodbye 👋🏾. Comeback soon!')
            break
    elif choice == '2':
          add_movie()
    elif choice == '3':
          show_all()
    else: 
          print(' ❌ Invalid Option. Please try again.')