import pandas as pd
import requests
import bs4

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/78.0.3904.97 YaBrowser/19.12.0.358 Yowser/2.5 Safari/537.36'
}
url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=HEADERS)
soup = bs4.BeautifulSoup(response.text, 'lxml')
movies_info = soup('div', attrs={'class': 'movie-hover-info'}, limit=10)

film_info = []
for info in movies_info:
    div_element = info.select_one('div:nth-child(2)')
    name = div_element['title']
    film_type = div_element(string=True)[-1].strip()
    release_date = info.select_one('div:last-child')(string=True)[-1].strip()
    film_info.append((name, film_type, release_date))

film_data = pd.DataFrame(data=film_info,
                         columns=('电影名称', '影片类型', '上映日期'))
film_data.to_csv('film.csv', encoding='utf-8', index=False)
