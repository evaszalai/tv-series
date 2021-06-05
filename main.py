from flask import Flask, render_template, url_for, redirect, request
from data import queries
import math
from dotenv import load_dotenv
from util import json_response

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    return redirect('/shows/most-rated/1/rating/DESC')


@app.route('/show-trailer')
def show_trailer():
    if request.args.get('search') is not None:
        search_by = f"%{request.args.get('search')}%"
        shows = queries.get_shows_by_search(search_by)
        for show in shows:
            if show['trailer'] != 'No URL':
                show['trailer'] = f"https://www.youtube.com/embed/{convert_to_embed_url(show['trailer'])}"
    else:
        shows = None
    return render_template('show_trailer.html', shows=shows)


@app.route('/by_genre')
def list_by_genre():
    genres = []
    genres_list = queries.list_all_genres()
    for item in genres_list:
        genres.append(item['name'].lower())
    if request.args.get('search') is not None:
        genre = request.args.get('search')
        shows = queries.list_by_genre(genre)
    else:
        shows = None
        genre = None
    return render_template('list-by-genre.html', shows=shows, genres=genres, chosengenre=genre)


@app.route('/search')
def search_character():
    return render_template('search_characters.html')


@app.route('/search-ajax/<search_words>')
@json_response
def search_ajax(search_words):
    return queries.search_characters(search_words)


@app.route('/stars')
def stars_per_genre():
    genres = []
    genres_list = queries.list_all_genres()
    for item in genres_list:
        genres.append(item['name'].lower())
    genre = request.args.get('search')
    shows = queries.get_top_by_genre(genre)
    for show in shows:
        if show['rating'] is not None:
            show['rating'] = round(show['rating'])
        else:
            shows = None
    return render_template('stars.html', shows=shows, genres=genres, chosen_genre=genre)


@app.route('/actors')
def actors():
    actors_list = queries.get_actors_with_age()
    for actor in actors_list:
        if actor['age'] is not None:
            actor['age'] = int(actor['age'])
    return render_template('list_actors_with_age.html', actors=actors_list)


@app.route('/shows/most-rated')
def index_most_rated():
    return redirect('/shows/most-rated/1/rating/DESC')


@app.route('/shows')
def list_shows():
    return redirect('/shows/most-rated/1/rating/DESC')


@app.route('/years')
def list_years():
    options = [i for i in range(1970, 2018)]
    start = request.args.get('start')
    end = request.args.get('end')
    years = queries.shows_in_year(start, end)
    return render_template('list_years', years=years, options=options)


@app.route('/shows/most-rated/<page>/<order_by>/<order>')
def most_rated(page, order_by='rating', order='DESC'):
    shows_list = queries.most_rated(page, order_by=order_by, order=order)
    page_numbers = get_page_numbers()
    page_before = int(page) - 1
    page_after = int(page) + 1
    return render_template('most_rated.html', shows_list=shows_list, page_numbers=page_numbers, page=int(page), page_before=page_before, page_after=page_after, order_by=order_by, order=order)


@app.route('/show/<show_id>')
def display_show(show_id):
    show = queries.get_show(show_id)
    if show['runtime'] % 60 == 0:
        show['runtime'] = f"{show['runtime'] // 60}h"
    elif show['runtime'] > 60:
        show['runtime'] = f"{show['runtime'] // 60}h {show['runtime'] % 60}min"
    else:
        show['runtime'] = f"{show['runtime']}min"
    if show['trailer'] != 'No URL':
        show['trailer'] = convert_to_embed_url(show['trailer'])
    actors = queries.get_top_actors(show_id)
    seasons = queries.get_seasons(show_id)
    return render_template('display_show.html', show=show, actors=actors, seasons=seasons)


@app.route('/design')
def design():
    return render_template('design.html')


def convert_to_embed_url(url):
    query_string = url.split('?')[1]
    query_params = query_string.split('&')
    query_params = [item.split('=') for item in query_params]
    for param in query_params:
        if param[0] == 'v':
            video_id = param[1]
    return video_id


def get_page_numbers():
    all_shows = queries.get_shows()
    page_numbers = []
    page_num = 0
    show_num = 0
    for show in all_shows:
        show_num += 1
        if show_num % 15 == 1:
            page_num += 1
            page_numbers.append(page_num)
    return page_numbers


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
