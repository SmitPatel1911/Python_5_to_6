def get_song_duration_per_minute(total_duration, number_of_songs):
    try:
        average_duration=total_duration/number_of_songs
        return average_duration
    except ZeroDivisionError as e:
        return "Cannot calculate: the playlist has 0 songs."
    finally:
        print("Calculation completed.")


print(get_song_duration_per_minute(180, 30))
print(get_song_duration_per_minute(180, 0))
