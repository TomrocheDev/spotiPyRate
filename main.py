import resources
import os

# Install the following modules for this program to work:
# pip install selenium
# pip install pytube

SPOTIFY_USERNAME = os.environ['Spotify_username']
SPOTIFY_PASSWORD = os.environ['Spotify_password']


def main():
    # Prepare Spotify for gathering data
    spotify_preparation = resources.SpotifyPrepare(SPOTIFY_USERNAME, SPOTIFY_PASSWORD)
    driver = spotify_preparation.connect()
    spotify_preparation.login(driver)
    spotify_preparation.accept_cookies(driver)

    # Scrape data from playlists
    spotify_data_scraping = resources.DataScraping(driver)
    user_playlists = spotify_data_scraping.get_user_playlists()

    main_data = []
    for playlist in user_playlists:
        playlist_data = spotify_data_scraping.get_playlist_data(playlist)
        main_data.append(playlist_data)

    driver.quit()

    # Create download folder
    downloads_folder_path = 'downloaded_tracks'  # Enter your desired path here
    file_handling = resources.FileHandling(downloads_folder_path).create_folder()

    # Download playlist and create playlist folders
    for playlists in main_data:
        for title, tracks in playlists.items():
            playlist_folder_path = f'{downloads_folder_path}/{title}'
            resources.FileHandling(playlist_folder_path).create_folder()

            for track in tracks:
                query_string = f"{track['artist']} {track['title']} full song"
                download = resources.Download(query_string)
                youtube_url = download.get_youtube_url()
                download.download_track(query_string, youtube_url, playlist_folder_path)

    print('Downloading finished. Happy listening! ')


main()
