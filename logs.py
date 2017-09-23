#!/usr/bin/env python
import os
import sys
import psycopg2

DB_NAME = "news"

# what are the most popular three articles of all time?
query_1 = """SELECT articles.title, agglog.asviews
    FROM articles join (SELECT path,
    COUNT(*) AS views
    FROM log GROUP BY path)
    AS agglog on articles.slug = (regexp_split_to_array (
    path, E'/article/')) [2]
    WHERE path != '/' ORDER BY agglog.asviews DESC limit 3;"""

# Who are the most popular article authors of all time?
query_2 = """SELECT authors.name,
    COUNT(articles.author) AS views
    FROM articles, log, authors WHERE log.path =
    concat( E'/article/',articles.slug)
    and articles.author = authors.id GROUP BY authors.name
    ORDER BY views DESC;"""

# On which days did more than 1% of requests lead to errors
query_3 = """SELECT Date,Total,Error,
    (Error::float*100)/total::float AS percent
    FROM (SELECT time::timestamp::date AS Date,
    COUNT(status) AS Total, sum(case when status =
    '404 NOT FOUND' then 1 else 0 end) AS Error
    FROM log GROUP BY time::timestamp::date) AS result
    WHERE (Error::float*100)/Total::float > 1.0
    ORDER BY Percent DESC;"""

# Fetch tables from the database.
# Connect to the database news


def connect():
    return psycopg2.connect("dbname=news")


def popular_article(query_1):
    """Prints most popular three articles of all time"""
    # Connect to the database
    db = connect()
    # Query command
    c = db.cursor()
    # Objects that runs the queries and results
    c.execute(query_1)
    # Command to fetch the results
    result = c.fetchall()
    print "\nPopular Articles:\n"
    for row in result:
        print "\""+row[0]+"\" - "+str(row[1])+" views"
    # Close the connection
    db.close()


def popular_authors(query_2):
    """Prints most popular article authors of all time"""
    db = connect()
    c = db.cursor()
    c.execute(query_2)
    result = c.fetchall()
    print "\nPopular Authors:\n"
    for i in range(0, len(result), 1):
        print "\""+result[i][0]+"\" - "+str(result[i][1])+" views"
    db.close()


def log_status(query_3):
    """Print days on which more than 1% of requests lead to errors"""
    db = connect()
    c = db.cursor()
    c.execute(query_3)
    result = c.fetchall()
    print "\nDays with more than 1% of errors:\n"
    for i in range(0, len(result), 1):
        print str(result[i][0])+" - "+str(round(result[i][3], 2))+"% errors"
    db.close()


if __name__ == '__main__':
    popular_article(query_1)
    popular_authors(query_2)
    log_status(query_3)
