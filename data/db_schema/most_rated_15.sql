SELECT shows.id,
       title,
       TO_CHAR(year, 'yyyy') AS year,
       runtime, ROUND(rating, 1) AS rating,
       STRING_AGG(name, ',') AS genres,
       COALESCE(trailer, 'No URL') AS trailer,
       COALESCE(homepage, 'No URL') AS homepage
FROM shows
    LEFT JOIN show_genres sg on shows.id = sg.show_id
    LEFT JOIN genres g on g.id = sg.genre_id
GROUP BY shows.id
ORDER BY rating DESC
LIMIT 15;