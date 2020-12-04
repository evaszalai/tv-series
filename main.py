from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/shows/most-rated/<page>')
def most_rated(page):
    shows_list = queries.most_rated(page)
    all_shows = queries.get_shows()
    page_numbers = []
    page_num = 0
    show_num = 0
    for show in all_shows:
        show_num += 1
        if show_num % 15 == 1:
            page_num += 1
            page_numbers.append(page_num)
    return render_template('most_rated.html', shows_list=shows_list, page_numbers=page_numbers, page=int(page))


@app.route('/show/<show_id>')
def display_show(show_id):
    return render_template('display_show.html', show=show)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
