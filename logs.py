import psycopg2

DB_NAME="news"

# what are the most popular three articles of all time?
query_1="""select articles.title, count (*) as views
    from articles join log on articles.slug =
    (regexp_split_to_array(path, E'/article/')) [2]
    where path != '/' group by
    (regexp_split_to_array(path, E'/article/')) [2],
    articles.title order by views desc limit 3;"""

# Who are the most popular article authors of all time?
query_2="""select authors.name,
    count(articles.author) as views
    from articles, log, authors where log.path =
    concat( E'/article/',articles.slug)
    and articles.author = authors.id group by authors.name
    order by views desc;"""

# On which days did more than 1% of requests lead to errors
query_3="""select Date,Total,Error,
    (Error::float*100)/total::float as percent
    from (select time::timestamp::date as Date,
    count(status) as Total, sum(case when status =
    '404 NOT FOUND' then 1 else 0 end) as Error
    from log group by time::timestamp::date) as result
    where (Error::float*100)/Total::float > 1.0
    order by Percent desc;"""

# Fetch tables from the database.
# Connect to the database news
def connect():
    return psycopg2.connect("dbname=news")

def popular_article(query_1):
    """Prints most popular three articles of all time"""
    # Connect to the database
    db=connect()
    # Query command
    c=db.cursor()
    # Objects that runs the queries and results
    c.execute(query_1)
    # Command to fetch the results
    result=c.fetchall()
    print "\nPopular Articles:\n"
    for i in range(0,len(result),1):
        print "\""+result[i][0]+"\" - "+str(
            result[i][1])+" views"
    # Close the connection
    db.close()

def popular_authors(query_2):
    """Prints most popular article authors of all time"""
    db=connect()
    c=db.cursor()
    c.execute(query_2)
    result=c.fetchall()
    print "\nPopular Authors:\n"
    for i in range(0,len(result), 1):
        print "\""+result[i][0]+"\" - "+str(
            result[i][1])+" views"
    db.close()

def log_status(query_3):
    """Print days on which more than 1% of requests lead to errors"""
    db=connect()
    c=db.cursor()
    c.execute(query_3)
    result=c.fetchall()
    print "\nDays with more than 1% of errors:\n"
    for i in range(0,len(result),1):
        print str(
            result[i][0])+" - "+str(
            round(result[i][3], 2))+"% errors"
    db.close()

if __name__ == '__main__':

    print popular_article(query_1)
    print popular_authors(query_2)
    print log_status(query_3)
