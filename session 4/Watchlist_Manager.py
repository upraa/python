
movie = []

while True:
    print('''
    ====== Watchlist Manager ======
    1. Add Movie
    2. Remove Movie
    3. Sort Movie
    4. Show Movies
    5. Exit
    ''')


    choice = int(input("Enter your option: "))

    if choice == 1:
        movie_Name = input("Enter movie Name: ")
        movie_year = int(input("Enter year of movie: "))
        movie_topic = input("Enter movie topic: ")
        movie.append((movie_Name, movie_year , movie_topic))
        print("Movie added successfully!")

    elif choice == 2:
        movie_remove = input("Enter movie Name to remove: ")

        for item in movie:
            if item[0] == movie_remove:
                movie.remove(item)
                print("movie removed successfully!")
                break
        else:
            print("movie not found!")

    elif choice == 3:
        movie.sort()
        
        print("Movies sorted successfully!")
    elif choice == 4:
        for item in movie:
            print(item)
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
