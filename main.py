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


@app.route('/shows/most-rated')
def most_rated():
    shows_list = queries.most_rated()
    return render_template('most_rated.html', shows_list=shows_list)


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
