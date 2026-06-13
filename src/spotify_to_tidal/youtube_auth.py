from adapters.youtube import YouTubePlaylist, YouTubeTrack


def open_youtube_session(youtube_tracks):
    tracks = [
        YouTubeTrack(t["artist"], t["title"])
        for t in youtube_tracks
    ]

    return YouTubePlaylist(tracks)
