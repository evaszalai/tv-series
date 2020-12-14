from flask import Flask, render_template, url_for, redirect, request
from data import queries
import math
from dotenv import load_dotenv
from util import json_response

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    seasons = queries.get_highest_season_number()
    return render_template('index.html', shows=shows, seasons=seasons)


@app.route('/shows/most-rated')
def index_most_rated():
    return redirect('/shows/most-rated/1/rating/DESC')


@app.route('/shows')
def list_shows():
    return redirect('/shows/most-rated/1/rating/DESC')


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
