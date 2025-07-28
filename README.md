# Project Title
Playlist Scraper

# Project Description 
"Playlist Scraper" is a python script that uses Selenium to extract album information (album name, artist name, ratings...) from the website: https://www.albumoftheyear.org/releases/this-week/

# Features 
* Extracts album details: artist, album name, user and critic ratings
* Saves extracted data in CSV
* Handles pagination
* Rotates user-agents and uses random to mimic human like behaviour

# Tools and Libraries
* Python 3.11
* Selenium
* undetected-chromedriver
* random
* time
* csv

# How to Run the Code
1. Make sure you have Python 3.11 installed
2. Then install these libraries:
   ```pip install selenium undetected-chromedriver```
3. Run the script using
   ```python album_scraper.py```
4. The extracted data will be saved to the file named "playlist_song.csv"

# Background
It all started with curiosity about how websites work. One day I wanted to make a list and write down all my Spotify songs, their artists and genre. After realising it will take me forever to do this, I started to look for faster and simpler methods. Didn't take me long to learn about web scraping. Now I can extract tons of data just writing several lines of code. 

# Notes
This is a practice project, not real Spotify scraping code. Only for learning purposes and not intended for real-world data extraction

# Contact
If you have any questions or feedback, feel free to open an issue or reach out via GitHub
