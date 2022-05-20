import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://rat:ratrat@localhost:5432/postgres')
connection = engine.connect()

connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(1, 'rat', 'ratman')""")
connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(2, 'bat', 'batman')""")
connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(3, 'cat', 'catman')""")
connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(4, 'dog', 'dogman')""")
connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(5, 'cow', 'cowman')""")
connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(6, 'fox', 'foxman')""")
connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(7, 'owl', 'owlman')""")
connection.execute("""INSERT INTO performer(id, perf_name, nik_name) VALUES(8, 'cod', 'codman')""")
#
connection.execute("""INSERT INTO genre(id, genre_name) VALUES(1, 'metal')""")
connection.execute("""INSERT INTO genre(id, genre_name) VALUES(2, 'heavy_metal')""")
connection.execute("""INSERT INTO genre(id, genre_name) VALUES(3, 'super_heavy_metal')""")
connection.execute("""INSERT INTO genre(id, genre_name) VALUES(4, 'death_metal')""")
connection.execute("""INSERT INTO genre(id, genre_name) VALUES(5, 'super_death_metal')""")

connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(1, 'rats', '2018')""")
connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(2, 'bats', '2010')""")
connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(3, 'cats', '2011')""")
connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(4, 'bogs', '2000')""")
connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(5, 'cows', '2051')""")
connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(6, 'foxes', '2018')""")
connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(7, 'owls', '2030')""")
connection.execute("""INSERT INTO album(id, album_name, rel_date) VALUES(8, 'cods', '2000')""")

connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(1, 'my rat', 1, 222)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(2, 'his rat', 1, 333)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(3, 'my bat', 2, 444)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(4, 'his bat', 2, 555)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(5, 'my cat', 3, 666)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(6, 'his cat', 3, 777)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(7, 'my dog', 4, 888)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(8, 'his dog', 4, 999)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(9, 'my cow', 4, 525)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(10, 'his cow', 5, 252)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(11, 'my fox', 5, 424)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(12, 'his fox', 6, 323)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(13, 'my owl', 6, 462)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(14, 'his owl', 7, 151)""")
connection.execute("""INSERT INTO track(id, track_name, album_id, track_length) VALUES(15, 'my cod', 7, 515)""")

connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(1, 'ratcoll', '2000')""")
connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(2, 'batcoll', '2022')""")
connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(3, 'catcoll', '2011')""")
connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(4, 'dogcoll', '2018')""")
connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(5, 'cowcoll', '2019')""")
connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(6, 'foxcoll', '2020')""")
connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(7, 'owlcoll', '2014')""")
connection.execute("""INSERT INTO collection(id, coll_name, rel_date) VALUES(8, 'codcoll', '2044')""")

connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(1, 1)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(1, 2)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(1, 3)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(2, 3)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(2, 4)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(3, 1)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(3, 2)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(4, 3)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(4, 5)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(5, 2)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(6, 1)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(7, 4)""")
connection.execute("""INSERT INTO perf_genre(perf_id, genre_id) VALUES(8, 5)""")

connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(1, 1)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(2, 2)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(3, 3)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(4, 4)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(5, 5)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(6, 6)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(7, 7)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(8, 6)""")
connection.execute("""INSERT INTO perf_album(perf_id, album_id) VALUES(8, 7)""")


connection.execute("""INSERT INTO track_collection(coll_id, track_id) VALUES(1, 2)""")
connection.execute("""INSERT INTO track_collection(coll_id, track_id) VALUES(3, 4)""")
connection.execute("""INSERT INTO track_collection(coll_id, track_id) VALUES(4, 4)""")
connection.execute("""INSERT INTO track_collection(coll_id, track_id) VALUES(4, 5)""")
connection.execute("""INSERT INTO track_collection(coll_id, track_id) VALUES(5, 4)""")