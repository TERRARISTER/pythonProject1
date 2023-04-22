import sqlite3
from bs4 import BeautifulSoup
import datetime

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS weather(date_time TEXT, temperature REAL)''')
url = 'https://ua.sinoptik.ua/погода-львів'
if response.status_code == 200:
   html = response.content

else:
   response = requests.get(url)
   print('Не вдалося отримати сторінку')
from bs4 import BeautifulSoup


soup = BeautifulSoup(html, 'html.parser')

today_weather = soup.find('div', {'class': 'weatherToday'}).find('div', {'class': 'temperature'}).text

today_temperature = int(today_weather.split('°')[0])


print(f"Температура сьогодні: {today_temperature}°C")

temperature = today_temperature

date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


conn = sqlite3.connect('weather.db')

conn.execute("INSERT INTO weather VALUES (?, ?)", (date_time, temperature))

c = conn.cursor()
#Тут для температурі нужен BeautifulSoup
cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
cur.execute("INSERT INTO first_table (name) VALUES ('John');")
cur.execute("SELECT rowid, name FROM first_table WHERE rowid=2;")
cur.execute("UPDATE first_table SET name='Floppa' WHERE rowid=2;");
connection.commit()

connection.commit()
res = cur.fetchall()
print(res)
connection.close()