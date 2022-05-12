
# This program lets the user insert/edit/delete a list of movies that is stored into a text file.

def main():
    
    # Sets variables to their datatype
    count = 1
    movie_list = []
    
    print('Hello! Welcome to my favorite movies collection.')
    print()
    
    # Open file for reading
    with open('dvd.txt', 'r') as read_file:
        # Read the lines and assign to variable
        fileContents = read_file.readlines()
        # Run for loop to only select the indexes after before \n with [:-1]
        for line in fileContents:
            current_place = line[:-1]
            movie_list.append(current_place)
            print(f'{count}.' + ' ' + line)
            count += 1
            
    # Make flag for while loop        
    keep_going = True
    while keep_going:

        # Instructions for the user to choose from
        print('Press a to add a dvd.\n')
        print('Press c to choose a dvd.\n')
        print('Press u to update the collection.\n')
        print('Press d to delete a dvd.\n')
        user_input = input()

        # a = adding a movie. Simply appending the user input to the list
        if user_input == 'a':
            print('What would you like to add?\n')
            add_dvd = input().lower()
            movie_list.append(add_dvd)            

        # c = choose a movie to watch. Finding the index of the inputed movie title and making sure it's in the list.
        if user_input == 'c':
            print('Pick a movie to watch:')
            movie_picked = input().lower()
            # Try and except: for ValueErrors
            try:
                movie_to_watch = movie_list.index(movie_picked)
                movie = movie_list[movie_to_watch]
                print(f'{movie} is a good movie!!')
                print()
                break
            except ValueError:
                print('Movie not in collection!')
                print()
                continue

        # Update the list. Find index again and replace user input with indexed element
        if user_input == 'u':
            print('Which movie would you like to update?')
            existing_movie = input().lower()
            print('Enter a new movie or updated title:')
            new_movie = input().lower()
            movie_index = movie_list.index(existing_movie)
            movie_list[movie_index] = new_movie

        # Delete movie item. use remove method to delete the movie the user selected from the list
        if user_input == 'd':
            print('Which movie would you like to delete?')
            selected_move = input().lower()
            movie_list.remove(selected_move)

        # Open file for writing. Updating the text document with writelines method
        with open('dvd.txt', 'w') as write_file:
            count = 0
            write_file.writelines(dvd + '\n' for dvd in movie_list)

        print()
        # Print element from list
        for element in movie_list:
            print(' - ' + element)
            
        # Keep going?
        print()
        print('Do you want to keep_going? [y for yes, n for no]')
        keep_going = input().lower()
        if keep_going == 'n':
            print('Movies in list:')
            print()
            break

    # Print out movies with a '-' infront
    for element in movie_list:
            print(' - ' + element)
            
    print()
    print(f'Movie File closed with {len(movie_list)} movies.')

# Call main
if __name__ == '__main__':
    main()
