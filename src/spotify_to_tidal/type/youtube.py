class YouTubeTrack:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def __str__(self):
        return f"{self.artist} - {self.title}"


class YouTubePlaylist:
    def __init__(self, tracks):
        self.tracks = tracks

    def __iter__(self):
        return iter(self.tracks)
