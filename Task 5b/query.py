import psycopg2

connection = psycopg2.connect(user = "postgres",
                             # password = "NEW_PASSWORD",
                              host = "localhost",
                              port = 5432,
                              database = "db")
                              
cursor = connection.cursor()
cursor.execute("""SELECT actor.ACTOR_ID,FIRST_NAME,LAST_NAME,TITLE,DESCRIPTION,RELEASE_YEAR \
    FROM film \
        INNER JOIN film_actor on film.film_id = film_actor.film_id\
        INNER JOIN actor on film_actor.actor_id = actor.actor_id; """)
rows = cursor.fetchmany(10)
for row in rows:
    print("ACTOR_ID:   ", row[0])
    print("FIRST_NAME:   ", row[1])
    print("LAST_NAME:    ", row[2])
    print("TITLE:   ", row[3])
    print("DESCRIPTION:   ", row[4])
    print("RELEASE_YEAR:   ", row[5], "\n")
 
 
