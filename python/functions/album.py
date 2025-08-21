def make_album(artist_name, album_title, number_of_songs=None):
    """Dictionary to store the artist name and album title."""
    if number_of_songs:
        album = {
            'artist_name' : artist_name,
            'album_title' : album_title,
            'number_of_songs' :number_of_songs,
            }
    else:
        album = {
            'artist_name' : artist_name,
            'album_title' : album_title,
            }
    return album


my_album = make_album('davido', 'aye')
print(my_album)

his_album = make_album('wizkid', 'kese')
print(his_album)

your_album = make_album('adele', 21)
print(your_album)

sabinus_album = make_album('celine deon', 'goodbye', 25)
print(sabinus_album)
