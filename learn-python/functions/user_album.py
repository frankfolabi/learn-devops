def make_album(artist_name, album_title):
    """Dictionary to store the artist name and album title."""
    
    album = {}

    album['artist_name'] = artist_name
    album['album_title'] = album_title

    return album

while True:
    print("\n(Enter 'q' to quit this program)\n")

    artist_name = input("Who is the artist? ")
    if artist_name == 'q':
        break

    album_title = input("What is the album name? ") 
    if album_title == 'q':
        break

    created_album = make_album(artist_name,album_title)
    print(created_album)
