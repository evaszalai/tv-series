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


def get_longest_shows():
    query = """SELECT shows.id, shows.title, (runtime * COUNT(e.id)) AS total_runtime
        FROM shows
        LEFT JOIN seasons s on shows.id = s.show_id
        LEFT JOIN episodes e on s.id = e.season_id
        GROUP BY shows.id
        ORDER BY total_runtime DESC
        LIMIT 10"""
    return data_manager.execute_select(query)


def get_actors_in_longest(longest_shows):
    query = """SELECT shows.id, COALESCE(a.name, '') AS name
        FROM shows
        FULL JOIN show_characters sc on shows.id = sc.show_id
        FULL JOIN actors a on a.id = sc.actor_id
        WHERE shows.id IN %(longest_shows)s
        ORDER BY a.name"""
    params = {'longest_shows': longest_shows}
    return data_manager.execute_select(query, params)
