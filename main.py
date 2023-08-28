import resources
import os

# Install the following modules for this program to work:
# pip install selenium


def main():
    spotify_username = os.environ['Spotify_username']
    spotify_password = os.environ['Spotify_password']

    # Prepare Spotify for gathering data
    spotify_preparation = resources.SpotifyPrepare(spotify_username, spotify_password)
    driver = spotify_preparation.connect()
    spotify_preparation.login(driver)
    spotify_preparation.accept_cookies(driver)


main()
