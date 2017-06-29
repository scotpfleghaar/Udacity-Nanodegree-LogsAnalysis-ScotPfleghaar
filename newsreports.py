#!/usr/bin/python3
import psycopg2


#  What are the most popular three articles of all time?
mostPopularArticles = ("What are the most popular three articles of all time?")
firstQuery = (
    "SELECT articles.title, "
    "       Count(*) AS articleviews "
    "FROM   articles, "
    "       log "
    "WHERE  log.path = Concat('/article/', articles.slug) "
    "GROUP  BY articles.title "
    "ORDER  BY articleviews DESC "
    "LIMIT  3; ")  # Change number if you would like more popular articles


#  Who are the most popular article authors of all time?
mostPopularAuthors = ("Who are the most popular article authors of all time?")
secondQuery = (
    "SELECT authors.name, "
    "       Count(*) AS articleviews "
    "FROM   articles "
    "       INNER JOIN authors "
    "                ON articles.author = authors.id, "
    "       log "
    "WHERE  log.path = Concat('/article/', articles.slug) "
    "GROUP  BY authors.name "
    "ORDER  BY articleviews DESC ")


#  On which days did more than 1% of requests lead to errors?
httpErrors = ("On which days did more than 1% of requests lead to errors?")
#  This query looks at the total http requests at the log time, than divides
#  by the amount of 404 errors that occured at the log time.
#  Next, it displays that percentage with date when equal or greater than 1%
thirdQuery = (
    "SELECT date, "
    "       Round(100.0 * totalerrors / totalrequests, 2) AS percent "
    "FROM   (SELECT time::date AS date, "
    "               Count(*) AS totalrequests, "
    "              sum(case when status = '404 NOT FOUND' then 1 else 0 end) "
    "                 as totalerrors "
    "        FROM   log "
    "               GROUP  BY date) AS foo "
    "WHERE  Round(100.0 * totalerrors / totalrequests, 2) >= 1 "
    "ORDER BY percent DESC; ")


def getResults(query):
    """Return Query Results Where Parameter is Specified Query"""
    #  Tells psycopg2 which database we are talking about
    db = psycopg2.connect(database="news")
    #  Curser is a local variable commonly use in sql/python connections
    curser = db.cursor()
    #  Please refer to https://dev.mysql.com/doc/connector-python/en/
    #  for more information about how this block of code works
    curser.execute(query)
    i = curser.fetchall()
    db.close()
    return i



def printResults(queryResults):
    """Prints Query Results"""
    print (queryResults[1])
    #  This is a for loop that enumerates through the array to the
    #  next item so that we don't recreate a function for each query
    for index, results in enumerate(queryResults[0]):
        print (
            index+1, "-", results[0],
            ', ',
            str(results[1]), " views")


def printError(queryResults):
    """Prints Query Results For httpErrors Query"""
    print (queryResults[1])
    #  For loop created for the httpErrors array
    for results in queryResults[0]:
        print (
            results[0], "-",
            str(results[1]) + "% errors")


#  I was unable to find a way to combine the following two sections
#  storing the query results in a variable
x = getResults(firstQuery), mostPopularArticles
y = getResults(secondQuery), mostPopularAuthors
z = getResults(thirdQuery), httpErrors

#  printing the query results to console for display
printResults(x)
printResults(y)
printError(z)
