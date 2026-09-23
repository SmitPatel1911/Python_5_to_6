def playlist_songs(songs):
    
    if len(songs)==0:
        return

    print(songs[0])

    playlist_songs(songs[1:])


spotify_playlist =["Adhoora","Arz Kiya Hai","Vaaroon Vaaroon","Tera Naam Doon"]

playlist_songs(spotify_playlist)
