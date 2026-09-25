def playlist_generator(songs):
    for song in songs:
        yield song


songs=["Shape of You","Blinding Lights","Perfect","Levitating","Believer"]

playlist=playlist_generator(songs)

for song in playlist:
    print("Now playing : ",song)
