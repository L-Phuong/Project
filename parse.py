import requests
from bs4 import BeautifulSoup
import mysql.connector

# Fetch và parse HTML
url = "https://www.scrapingcourse.com/ecommerce/"
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Trích xuất dữ liệu
    titles = [h2.text for h2 in soup.find_all("h2")]
    link = [a['href'] for a in soup.find_all("a", href=True)]
    x = 16
    links = []
    for i in range(1, 16):
        links.append(link[x])
        x += 2

    # Kết nối database
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="271204",
        database="newschema"
    )
    cursor = db_connection.cursor()

    # Tạo bảng
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            link TEXT
        )
    """)

    # Chuẩn bị dữ liệu để lưu
    data_to_insert = [(titles[i], links[i]) for i in range(min(len(titles), len(links)))]

    # Lưu vào bảng
    insert_query = "INSERT INTO scraped_data (title, link) VALUES (%s, %s)"
    cursor.executemany(insert_query, data_to_insert)

    # Commit và đóng kết nối
    db_connection.commit()
    cursor.close()
    db_connection.close()
    print("Dữ liệu đã được lưu thành công!")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
