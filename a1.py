# Justin Orial
# October 18, 2019
# This is a playlist generator that can add songs, remove songs, sort the
# playlist by artist or title alphabetically, and filter the playlist using any
# filter they want,
# e.g, take out any pop songs or remove all songs by Smash Mouth

def create_playlist():
    # initializing an empty list variable and three parameters for a song.
    # The parameters will then be put into a tuple. So each song is in the form
    # of a tuple and the playlist will be a list of tuples.
    new_playlist = []
    title = ''
    artist = ''
    genre = ''

    # This loop runs until 'stop' is input for name. It asks the user for the
    # title, artist, and genre. It then makes a tuple of those three strings
    # and appends it to the list.
    while True:
        title = input('What is the title of the song? (type stop when you are '
                      'done adding songs)')

        if title.lower() == 'stop':
            break

        artist = input('Who is the artist of the song?')
        genre = input('What is the genre of the song?')
        song = (title, artist, genre)
        new_playlist.append(song)

    return new_playlist


def add_song(added_playlist):
    # Asks the user for one new song and its information
    title = input('What is the title of the song you want to add?')
    artist = input('Who is the artist of the song you want to add?')
    genre = input('What is the genre of the song you want to add?')
    song = (title, artist, genre)

    # Appends the new song to the playlist.
    added_playlist.append(song)
    return added_playlist


def remove_song(removed_playlist):
    # Asks the user for one song already in the playlist
    title = input('What is the title of the song you want to remove?'
                  '(Case sensitive)')
    artist = input('Who is the artist of the song you want to remove?'
                   '(Case sensitive)')
    genre = input('What is the genre of the song you want to remove?'
                  '(Case sensitive)')
    song = (title, artist, genre)

    # This if statement is just to account for if the user inputs a song that
    # is not in the playlist
    if song in removed_playlist:
        removed_playlist.remove(song)
    else:
        print('That song is not in your playlist. Please check for any typos.')

    return removed_playlist


def sort(sorted_playlist):
    sorted_entry = int(input('What would you like to sort by? (Please type the'
                         ' number)\n1. Title\n2. Artist\n3. Genre\n'))
    # sorting a list using the method our lab group came up with
    # nested for loops checking the whole list, starting with the first element
    for i in range(len(sorted_playlist)):
        # checking the remaining elements of the list
        lowest_index = i
        for j in range(i + 1, len(sorted_playlist)):
            # the second index is to sort by the user chosen parameter.
            if sorted_playlist[j][sorted_entry - 1] < \
                    sorted_playlist[lowest_index][sorted_entry - 1]:
                temp = sorted_playlist[lowest_index]
                sorted_playlist[lowest_index] = sorted_playlist[j]
                sorted_playlist[j] = temp

    return sorted_playlist


def filter(filtered_playlist):
    # will use a new playlist to append the filtered songs to
    new_filtered_playlist = []
    # asking the user what they want to filter and what kind of filter it
    # will be
    actual_filter = input('What title, artist, or genre do you want filtered?'
                          '(This is case sensitive)')
    filtered_entry_type = input('What kind of filter? (Please type the number)'
                                '\n1. Keep only these songs with this filter\n'
                                '2. Remove all songs with this filter\n')

    # Depending on what the user decides, this if/else statement either appends
    # every song with the filter or every song without the filter to the new
    # list. It then returns the new list and updates playlist in main.
    if filtered_entry_type == '1':
        for song in filtered_playlist:
            if actual_filter in song:
                new_filtered_playlist.append(song)
    elif filtered_entry_type == '2':
        for song in filtered_playlist:
            if actual_filter not in song:
                new_filtered_playlist.append(song)

    return new_filtered_playlist


if __name__ == "__main__":
    # First the playlist variable (which is a list) will be assigned the
    # function create_playlist() as that function returns a completed playlist
    # the user created. I will print out the playlist for them.
    playlist = create_playlist()

    print("Your playlist is: \n", playlist)

    # This is a while loop that keeps running until the user says they are
    # done updating their playlist. If they are not done, it will ask them how
    # they want to update the playlist. Depending on what the user chooses,
    # the playlist variable will be assigned the function that updates it.
    while True:
        entry = input('What would you like to do? (Please type the number of '
                      'the action)\n1. Add Song\n2. Remove Song\n3. '
                      'Sort Alphabetically\n4. Filter\n5. Done!\n')

        if entry == '5':
            break
        elif entry == '1':
            playlist = add_song(playlist)
            print("Your current playlist is: \n", playlist)
        elif entry == '2':
            playlist = remove_song(playlist)
            print("Your current playlist is: \n", playlist)
        elif entry == '3':
            playlist = sort(playlist)
            print("Your current playlist is: \n", playlist)
        elif entry == '4':
            playlist = filter(playlist)
            print("Your current playlist is: \n", playlist)

    # Prints the final updated playlist
    print("Your final playlist is: \n", playlist)









































