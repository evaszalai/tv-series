# Codecool TV series

## Story

Codecool is famous about its great community and one of the reasons for this is
the time spent well together - for instance with watching TV shows! That's why
there is a need for a great website where all Codecoolers can find his/her
favorite series.

The base design has been already made by the Codecool marketing team, there is also a database that is ready (thanks to
[trakt.tv](https://trakt.tv/)). My task was to present these data in an enjoyable way using my knowledge of SQL (Postgres), Python (Flask) with the Jinja template engine, HTML5, CSS3 and finally add some Javascript-action on each feature. 

To run it, you need to start a Postgres database and setup with the following environment variables: 'MY_PSQL_DBNAME', 'MY_PSQL_USER', 'MY_PSQL_HOST', 'MY_PSQL_PASSWORD'. After that you can fill it with data from the sql files in the data folder of the project. 

The page was created as a group of exercises preparing to close my studies in the web module – each exercise is available on separate pages using the Options button in the top right corner. The options are:

– List all shows with data in a sortable table

– List shows by genre

– List years of your selection with the average rating of all shows released that year

– List top 10 rated shows of selected genre

– Search for show character names and get the actor who played it

– List all actors from most to least active ones with their age

– See the 10 most active actors of all

– Search for trailers

![Alt text](/static/assets/Screenshot.png)


