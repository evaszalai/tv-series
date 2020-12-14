from psycopg2 import sql
from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def most_rated(page, order_by='rating', order='DESC'):
    elem_per_page = 15
    offset = (int(page) - 1) * elem_per_page + 1
    query = """SELECT 
    shows.id, 
    title, 
    TO_CHAR(year, 'yyyy') AS year, 
    runtime, 
    ROUND(rating, 1) AS rating, 
    STRING_AGG(name, ', ') AS genres, 
    COALESCE(trailer, 'No URL') AS trailer, 
    COALESCE(homepage, 'No URL') AS homepage 
    FROM shows 
    LEFT JOIN show_genres sg on shows.id = sg.show_id 
    LEFT JOIN genres g on g.id = sg.genre_id 
    GROUP BY shows.id 
    ORDER BY %(by_)s %(order)s 
    OFFSET %(offset)s 
    LIMIT %(elem_per_page)s""" % {'by_': order_by, 'order': order, 'offset': offset, 'elem_per_page': elem_per_page}
    return data_manager.execute_select(query)


def get_show(show_id):
    query = """SELECT
    title,
    runtime,
    ROUND(rating, 1) AS rating,
    STRING_AGG(DISTINCT g.name, ', ') AS genres,
    overview,
    COALESCE(trailer, 'No URL') AS trailer
    FROM shows
    INNER JOIN show_genres sg on shows.id = sg.show_id
    INNER JOIN genres g on g.id = sg.genre_id
    WHERE shows.id = %(show_id)s
    GROUP BY title, runtime, rating, overview, trailer""" % {'show_id': show_id}
    return data_manager.execute_select(query, fetchall=False)


def get_top_actors(show_id):
    query = """SELECT
    actors.id, 
    actors.name AS actor, 
    COUNT(DISTINCT character_name) AS roles
    FROM actors
    FULL JOIN show_characters sc on actors.id = sc.actor_id
    LEFT JOIN shows s on sc.show_id = s.id
    WHERE s.id = %(show_id)s
    GROUP BY actors.id, actors.name
    ORDER BY roles
    LIMIT 3""" % {'show_id': show_id}
    return data_manager.execute_select(query)


def get_seasons(show_id):
    query = """SELECT
    season_number,
    title, 
    overview
    FROM seasons
    WHERE show_id = %(show_id)s
    ORDER BY season_number
    """ % {'show_id': show_id}
    return data_manager.execute_select(query)


def get_genres():
    query = "SELECT * FROM genres"
    return data_manager.execute_select(query)


def get_show_episodes_by_genre(genre_id):
    query = """SELECT s.title, COUNT(DISTINCT s2.id) AS number_of_seasons, COUNT(e.id) AS number_of_episodes, genres.id
FROM genres
LEFT JOIN show_genres sg on genres.id = sg.genre_id
LEFT JOIN shows s on s.id = sg.show_id
LEFT JOIN seasons s2 on s.id = s2.show_id
LEFT JOIN episodes e on s2.id = e.season_id
WHERE genres.id = %(genre_id)s
GROUP BY s.title, genres.id
HAVING COUNT(e.id) > 19
ORDER BY number_of_episodes
LIMIT 50"""
    params = {'genre_id': genre_id}
    return data_manager.execute_select(query, params)
