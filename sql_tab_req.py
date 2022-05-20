import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://rat:ratrat@localhost:5432/postgres')
connection = engine.connect()

x = connection.execute("""SELECT album_name, rel_date FROM album WHERE rel_date = 2018""").fetchall()

print(x)

x = connection.execute("""SELECT track_name, track_length FROM track ORDER BY track_length""").fetchall()
print(x[-1])

x = connection.execute("""SELECT track_name FROM track WHERE track_length >= 500""").fetchall()
print(x)

x = connection.execute("""SELECT coll_name, rel_date FROM collection WHERE rel_date >= 2018 AND
rel_date <= 2020""").fetchall()

print(x)

x = connection.execute("""SELECT perf_name FROM performer WHERE perf_name NOT IN (' ') """).fetchall()

print(x)

x = connection.execute("""SELECT track_name FROM track WHERE track_name LIKE '%%my%%'""").fetchall()

print(x)
