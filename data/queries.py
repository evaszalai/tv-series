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


def get_busiest_actors():
    query = """SELECT
    actors.id, name, COUNT(DISTINCT sc.id) AS roles
    FROM actors
    LEFT JOIN show_characters sc on actors.id = sc.actor_id
    GROUP BY actors.id, name
    ORDER BY roles DESC
    LIMIT 10"""
    return data_manager.execute_select(query)


def shows_in_year(start, end):
    query = """SELECT 
    TO_CHAR(year, 'yyyy') AS year, 
    ROUND(AVG(rating), 1) AS rating, 
    COUNT(id) AS number
    FROM shows
    WHERE CAST(TO_CHAR(year, 'yyyy') AS INT) BETWEEN %(start)s AND %(end)s
    GROUP BY year
    ORDER BY year 
    """
    params = {'start': start, 'end': end}
    return data_manager.execute_select(query, params)


def get_shows_by_search(search_by):
    query = """
    SELECT title, year, ROUND(rating, 1) AS rating, COALESCE(trailer, 'No URL') AS trailer
        FROM shows
        WHERE title ILIKE %(search_by)s
        ORDER BY title
    """
    params = {'search_by': search_by}
    return data_manager.execute_select(query, params)


def list_by_genre(genre):
    query = """SELECT title, COUNT(sc.id) AS characters
FROM shows
RIGHT JOIN show_genres sg on shows.id = sg.show_id
RIGHT JOIN genres g on g.id = sg.genre_id
FULL JOIN show_characters sc on shows.id = sc.show_id
WHERE g.name ILIKE %(genre)s
GROUP BY title
ORDER BY title
     """
    params = {'genre': genre}
    return data_manager.execute_select(query, params)


def list_all_genres():
    return data_manager.execute_select("SELECT name FROM GENRES")


def search_characters(words):
    query = """SELECT character_name, s.title AS title, a.name AS name
FROM show_characters
LEFT JOIN actors a on a.id = show_characters.actor_id
LEFT OUTER JOIN shows s on s.id = show_characters.show_id
WHERE character_name ILIKE %(words)s
    """
    params = {"words": words}
    return data_manager.execute_select(query, params)


def get_top_by_genre(genre):
    query = """SELECT
    shows.title, year, rating
    FROM shows
    Full Join show_genres sg on shows.id = sg.show_id
    FULL JOIN genres g on g.id = sg.genre_id
    WHERE g.name ILIKE %(genre)s
    ORDER BY rating DESC
    LIMIT 10
    """
    params = {'genre': genre}
    return data_manager.execute_select(query, params)


def get_actors_with_age():
    query = """SELECT a.name,
       EXTRACT(YEAR FROM AGE(COALESCE(a.death, current_date), a.birthday)) AS age,
       COUNT(sc.id) AS number_of_shows,
       CASE
WHEN a.death IS NULL THEN 'alive'
ELSE 'dead'
END AS alive
FROM actors a
LEFT JOIN show_characters sc on a.id = sc.actor_id
GROUP BY a.name, age, a.death
ORDER BY number_of_shows DESC
    """
    return data_manager.execute_select(query)