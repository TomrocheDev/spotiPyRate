# SpotiPyRate

This automation program is focussed on scraping your playlist data from Spotify. This data will be used to download your 
tracks to a audio file on your computer. It also creates a file structure, so your tracks will be placed into the right
playlist directory. 

### Let me take you through the process
1. SpotiPyRate automatically logs into your account (the program requires your username and password. The can be 
provided in the script in main.py on line 8 and 9).
2. It will automatically prepare Spotify for scraping the data.
3. With the help of Selenium, SpotiPyRate scrapes your playlist data and stores that data into a data object.
4. This main data object will be used to search YouTube for the corresponding urls.
5. These urls are used with PyTube. With the help of this module, the urls are converted into a audio file. 
6. The audio files will be stored in a logical order, so you don't lose track of where they are stored.

### Why this project
Of course, this program is not build to get around a paid membership on Spotify. This program is mainly written to train
my skills in webscraping and working with dynamic data. I've never written a multipurpose program before, so this was a 
great excersize for me.