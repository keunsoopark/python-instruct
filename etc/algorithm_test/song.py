# Linked data structure


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.played = None

    def next_song(self, song):
        self.next = song
        self.played = True

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        songs = set()
        next_song = self.next
        while next_song:
            if next_song in songs:
                return True
            songs.add(next_song)
            next_song = next_song.next
        return False

        # try:
        #     songs = set()
        #     next_song = self.next
        #     while True:
        #         if next_song in songs:
        #             return True
        #         songs.add(next_song)
        #         next_song = next_song.next
        # except AttributeError as e:
        #     print(e)
        #     return False


if __name__ == "__main__":
    first = Song("Hello")
    second = Song("Eye of the tiger")
    third = Song("dd")

    first.next_song(second)
    second.next_song(third)

    print(first.is_repeating_playlist())
