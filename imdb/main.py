from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
csv_filename = 'imdb_movie_data.csv'

try:
    source = requests.get(url, headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    movies = soup.find_all('li', class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")
    with open(csv_filename, mode="w", newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        header = ['Rank', 'Name', 'Year', 'Rating', "Rating amount"]
        writer.writerow(header)
        for movie in movies:
            name = movie.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text.split(". ")[1]
            rank = movie.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text.split(". ")[0]
            year = movie.find('div', class_="sc-b189961a-7 feoqjK cli-title-metadata").span.text
            rating = movie.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container").span.text.split("(")[0]
            amount = movie.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container").span.text.split("(")[1]
            amount = amount[:-1]
            writer.writerow([rank, name, year, rating, amount])
except Exception as e:
    print(e)


