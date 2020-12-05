from flask import Flask, render_template, url_for, redirect
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/shows/most-rated')
def index_most_rated():
    return redirect('/shows/most-rated/1/rating/True')


@app.route('/shows/most-rated/<page>/<order_by>/<reverse>')
def most_rated(page, order_by='rating', reverse=True):
    shows_list = queries.most_rated(page, order_by=order_by, reverse=reverse)
    page_numbers = get_page_numbers()
    page_before = int(page) - 1
    page_after = int(page) + 1
    return render_template('most_rated.html', shows_list=shows_list, page_numbers=page_numbers, page=int(page), page_before=page_before, page_after=page_after, order_by=order_by, reverse=reverse)


@app.route('/show/<show_id>')
def display_show(show_id):
    return render_template('display_show.html', show=show)


@app.route('/design')
def design():
    return render_template('design.html')


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
    app.run(debug=False)


if __name__ == '__main__':
    main()
