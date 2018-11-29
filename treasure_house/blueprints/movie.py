# -*- coding: utf-8 -*-
"""
    :author: Guowei
    :电影
"""
from flask import Blueprint, request, current_app, render_template

from treasure_house.models import Movie
from flask_cors import CORS

movie_bp = Blueprint('movie', __name__)

CORS(movie_bp, supports_credentials=True)


@movie_bp.route('/movie')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Movie.query.order_by(Movie.year.desc()).paginate(
        page, per_page=current_app.config['TREASURE_HOUSE_MOVIE_PER_PAGE']
    )
    movies = pagination.items

    return render_template('movie/index.html', page=page, pagination=pagination, movies=movies)


@movie_bp.route('/movie/play/<int:movie_id>')
def play(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('movie/movie_play.html', movie=movie)
