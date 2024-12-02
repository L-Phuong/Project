import requests
from bs4 import BeautifulSoup
import mysql.connector

# Step 1: Fetch and Parse HTML
url = "https://www.scrapingcourse.com/ecommerce/"  # Replace with your target URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Step 2: Extract Data (Example: Titles and Links)
    titles = [h2.text.strip() for h2 in soup.find_all("h2")]  # Replace with your specific selectors
    link = [a['href'] for a in soup.find_all("a", href=True)]
    x = 16
    links = []
    for i in range(1, 16):
        links.append(link[x])
        x += 2

    # Step 3: Connect to MySQL
    try:
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",  # Replace with your MySQL username
            password="271204",  # Replace with your MySQL password
            database="newschema"  # Replace with your database name
        )
        cursor = db_connection.cursor()

        # Step 4: Create Table if Not Exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                link TEXT
            )
        """)

        # Step 5: Insert Data into MySQL
        data_to_insert = [(titles[i], links[i]) for i in range(min(len(titles), len(links)))]
        insert_query = "INSERT INTO data (title, link) VALUES (%s, %s)"
        cursor.executemany(insert_query, data_to_insert)

        # Step 6: Commit and Close Connection
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
