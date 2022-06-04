import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://rat:ratrat@localhost:5432/postgres')
connection = engine.connect()

x = connection.execute("""
SELECT genre_name, COUNT(genre.id = perf_genre.id)
FROM genre
JOIN perf_genre ON genre.id = perf_genre.genre_id
GROUP BY genre.id
ORDER BY COUNT(genre.id = perf_genre.genre_id)""").fetchall()

print(x)

x = connection.execute("""
SELECT album_name, COUNT(album.id = track.album_id)
FROM album
JOIN track ON album.id = track.album_id
WHERE album.rel_date
BETWEEN 2000 AND 2020
GROUP BY album.id 
ORDER BY COUNT(album.id = track.album_id)""").fetchall()

print(x)

x = connection.execute("""
SELECT album_name, AVG(track.track_length)
FROM album, track
WHERE album.id = track.album_id
GROUP BY album.id""").fetchall()

print(x)

x = connection.execute("""
SELECT perf_name
FROM performer
JOIN perf_album ON performer.id = perf_album.perf_id
JOIN album ON perf_album.album_id = album.id
WHERE rel_date != 2018 AND perf_name NOT IN (SELECT perf_name
FROM performer
JOIN perf_album ON performer.id = perf_album.perf_id
JOIN album ON perf_album.album_id = album.id
GROUP BY perf_name
HAVING COUNT(rel_date) > 1
LIMIT 1)
""").fetchall()

print(x)

x = connection.execute("""
SELECT coll_name
FROM collection
JOIN track_collection ON collection.id = track_collection.coll_id
JOIN track ON track_collection.track_id = track.id
JOIN album ON track.album_id = album.id
JOIN perf_album ON album.id = perf_album.album_id
JOIN performer ON perf_album.perf_id = performer.id
WHERE perf_name = 'bat'""").fetchall()

print(x)

x = connection.execute("""
SELECT album_name
FROM album
JOIN perf_album ON album.id = perf_album.album_id
JOIN performer ON perf_album.perf_id = performer.id
JOIN perf_genre ON performer.id = perf_genre.perf_id
JOIN genre ON perf_genre.genre_id = genre_id
GROUP BY album_name""").fetchall()

print(x)

x = connection.execute("""
SELECT track_name
FROM track
LEFT JOIN track_collection ON track.id = track_collection.track_id
WHERE track.id NOT IN (SELECT track_id FROM track_collection)
GROUP BY track_name""").fetchall()

print(x)

x = connection.execute("""
SELECT perf_name
FROM performer
JOIN perf_album ON performer.id = perf_album.perf_id
JOIN album ON perf_album.album_id = album.id
JOIN track ON album.id = track.album_id
WHERE track_length = (
SELECT MIN(track_length) FROM track)
""").fetchall()

print(x)

x = connection.execute("""
SELECT album_name
FROM album
JOIN track ON album.id = track.album_id
GROUP BY album_name
HAVING COUNT(track.id) = (
SELECT COUNT(album_name)
FROM album
JOIN track ON album.id = track.album_id
GROUP BY album_name
LIMIT 1)
""").fetchall()

print(x)
