songs=["Shape Of You","Blinding Lights","Levitating","Senorita","Perfect"]

with open("playlist.txt","w") as file:
    for song in songs:
        file.write(song+"\n")

print("Songs saved to playlist.txt")
