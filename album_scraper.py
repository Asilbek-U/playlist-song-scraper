import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random
import csv

start_time = time.time()

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:109.0) Gecko/20100101 Firefox/117.0"
]

options = uc.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1800")
options.add_argument(f"user-agent={random.choice(user_agents)}")
# options.add_argument("--headless") ### Otional


driver = uc.Chrome(options=options)

datas = []
for x in range(1,11):
    print(f"Scraping page {x}")
    url = f"https://www.albumoftheyear.org/releases/this-week/{x}/"

    driver.get(url)
    time.sleep(random.uniform(1.5, 3.5))

    albums = driver.find_elements(By.CSS_SELECTOR, "div.albumBlock")

    for album in albums:
        artist = album.find_element(By.CLASS_NAME, "artistTitle").text.strip()
        album_name = album.find_element(By.CLASS_NAME, "albumTitle").text.strip()
        
        rating_elements = album.find_elements(By.CLASS_NAME, "ratingRow")

        critic_overall_rating = "N/A"
        critic_rated_num = "N/A"
        user_overall_rating = "N/A"
        user_rated_num = "N/A"
        for rating_element in rating_elements: 
            if "critic score" in rating_element.text:
                critic_overall_rating = rating_element.find_element(By.CLASS_NAME, "rating").text
                rated_by_elements = rating_element.find_elements(By.CLASS_NAME, "ratingText")
                critic_rated_num = rated_by_elements[1].text.strip().replace("(", "").replace(")", "")
                continue

            if "user score" in rating_element.text:
                user_overall_rating = rating_element.find_element(By.CLASS_NAME, "rating").text
                rated_by_elements = rating_element.find_elements(By.CLASS_NAME, "ratingText")
                user_rated_num = rated_by_elements[1].text.strip().replace("(", "").replace(")", "")
                continue

        datas.append([artist, album_name, critic_overall_rating, critic_rated_num, user_overall_rating, user_rated_num])

driver.quit()

end_time = time.time()
duration = end_time - start_time
minutes = int(duration // 60)
seconds = int(duration % 60)
print(f"Scraping took {minutes} minute(s) {seconds} second(s)")

with open("playlist_song.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Artist", "Album", "Crtics Rating (%)", "Num of Crtics Reviewed", "User Rating (%)", "Num of Users Reviewed"])

    writer.writerows(datas)


