import os
import requests
from bs4 import BeautifulSoup
import mysql.connector

TARGET_URL = "https://www.scrapingcourse.com/ecommerce/"
SAVE_FOLDER = "images"
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "271204",
    "database": "newschema"
}

os.makedirs(SAVE_FOLDER, exist_ok=True)

response = requests.get(TARGET_URL)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    image_tags = soup.find_all("img")
    if not image_tags:
        print("No images found!")
    else:
        db_connection = mysql.connector.connect(**DB_CONFIG)
        cursor = db_connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                path TEXT,
                url TEXT
            )
        """)

        for img in image_tags:
            img_url = img.get("src")
            if not img_url:
                continue

            if not img_url.startswith("http"):
                img_url = requests.compat.urljoin(TARGET_URL, img_url)

            try:
                img_data = requests.get(img_url).content
                img_name = os.path.basename(img_url)
                save_path = os.path.join(SAVE_FOLDER, img_name)

                with open(save_path, "wb") as img_file:
                    img_file.write(img_data)

                cursor.execute(
                    "INSERT INTO images (name, path, url) VALUES (%s, %s, %s)",
                    (img_name, save_path, img_url)
                )

                print(f"Saved {img_name} and stored metadata in the database.")

            except Exception as e:
                print(f"Failed to process {img_url}: {e}")

        db_connection.commit()
        cursor.close()
        db_connection.close()
        print("All images processed successfully!")

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
