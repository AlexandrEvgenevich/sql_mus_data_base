CREATE TABLE IF NOT EXISTS performer (id serial PRIMARY KEY, perf_name varchar(50) NOT NULL, nik_name varchar(50));

CREATE TABLE IF NOT EXISTS album (id serial PRIMARY KEY, album_name varchar(50) NOT NULL, rel_date integer NOT NULL);

CREATE TABLE IF NOT EXISTS track (id serial PRIMARY KEY, track_name varchar(50) NOT NULL, album_id integer REFERENCES album(id),

track_length integer NOT NULL);

CREATE TABLE IF NOT EXISTS perf_album (perf_id integer REFERENCES performer(id), album_id integer REFERENCES album(id));

CREATE TABLE IF NOT EXISTS genre (id serial PRIMARY KEY, genre_name varchar(50) NOT NULL);

CREATE TABLE IF NOT EXISTS perf_genre (perf_id integer REFERENCES performer(id), genre_id integer REFERENCES genre(id));

CREATE TABLE IF NOT EXISTS collection (id serial PRIMARY KEY, coll_name varchar(50) NOT NULL,rel_date integer NOT NULL);

CREATE TABLE IF NOT EXISTS track_collection (coll_id integer REFERENCES collection(id), track_id integer REFERENCES track(id));