from pytube import YouTube, Search, exceptions


class Download:

    def __init__(self, search):
        self.search = search

    def get_youtube_url(self):
        search = Search(self.search).results[0]

        return search.watch_url

    @staticmethod
    def download_track(track_info, url, output_path):
        try:
            print(f'downloading: {track_info}')
            youtube = YouTube(url)
            audio_file = youtube.streams.filter(only_audio=True).first()
            audio_file.download(output_path=output_path)
            print('Download complete.')
        except exceptions.AgeRestrictedError as error:
            print(f'Download failed due to error: {error}')
