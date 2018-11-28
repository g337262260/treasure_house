# -*- coding: utf-8 -*-
"""
    :author: Guowei
    :抓取网络数据，存到本地

"""

from treasure_house.extensions import db
from treasure_house.models import Movie
import requests

URL = 'https://hydramovies.com/api-v2/?source=http://hydramovies.com/api-v2/current-Movie-Data.csv&movie_year='
YEAR = 2018


def requestUrl(year):
    print('连接网络，Year=' + year)
    r = requests.get(URL + year)
    r_js = r.json()
    return r_js


def saveData():
    data = requestUrl(str(YEAR))
    print('获取到数据')
    for key, value in data.items():
        print('key=' + str(key) + '-----value=' + str(value))
        movie = Movie(
            movie_id=key,
            title=value['Title'],
            fulltitle=value['fulltitle'],
            year=value['movie_year'],
            categories=value['Categories'],
            summary=value['summary'],
            image_url=value['ImageURL'],
            imdb_id=value['imdb_id'],
            imdb_rating=value['imdb_rating'],
            runtime=value['runtime'],
            language=value['language'],
            ytid=value['ytid']
        )
        db.session.add(movie)
        db.session.commit()
        print('添加电影：'+value['Title'])



if __name__ == '__main__':
    saveData()
