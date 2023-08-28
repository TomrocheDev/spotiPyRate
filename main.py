import resources
import os

# Install the following modules for this program to work:
# pip install selenium

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


main()
