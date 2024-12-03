import requests
from bs4 import BeautifulSoup
import mysql.connector

# Fetch and Parse HTML
url = "https://www.scrapingcourse.com/ecommerce/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    #Extract Data
    titles = [h2.text.strip() for h2 in soup.find_all("h2")]
    image = [img['scr'] for img in soup.find_all("img", scr=True)]
    print(titles)
    print(len(titles))
    print(image)
    print(len(image))

    #Connect to MySQL
    try:
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="271204",
            database="newschema"
        )
        cursor = db_connection.cursor()

        #Create Table if Not Exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                link TEXT
            )
        """)

        #Insert Data into MySQL
        data_to_insert = [(titles[i], image[i]) for i in range(min(len(titles), len(image)))]
        insert_query = "INSERT INTO data (title, link) VALUES (%s, %s)"
        cursor.executemany(insert_query, data_to_insert)

        #Commit and Close Connection
        db_connection.commit()
        print("Data imported successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
