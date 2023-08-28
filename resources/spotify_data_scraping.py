from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DataScraping:

    def __init__(self, driver):
        self.driver = driver

    def get_user_playlists(self):
        user_playlists = self.driver.find_elements(By.CLASS_NAME, 'hIehTT')

        return user_playlists

    def get_playlist_data(self, playlist):
        playlist.click()

        WebDriverWait(self.driver, 5)\
            .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'gvLrgQXBFVW6m9MscfFA')))
        playlist_title = self.driver.find_element(By.CLASS_NAME, 'dYGhLW').text
        playlist_container = self.driver.\
            find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/'
                                   'section/div[2]/div[3]/div[1]/div[2]/div[2]')
        tracks_in_playlist = playlist_container.find_elements(By.CLASS_NAME, 'gvLrgQXBFVW6m9MscfFA')
        playlist_object = {playlist_title: []}

        for track in tracks_in_playlist:
            track_object = {
                'title': track.find_element(By.CLASS_NAME, 'fZDcWX').text,
                'artist': track.find_element(By.CLASS_NAME, 'bDHxRN').text,
                'image': track.find_element(By.TAG_NAME, 'img').get_attribute('src')
            }

            playlist_object[playlist_title].append(track_object)

        return playlist_object
