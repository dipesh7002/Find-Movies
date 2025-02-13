
import db_utils
def termFrequency():
    conn = db_utils.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
WITH word_extraction AS (
    SELECT
        LOWER(unnest(string_to_array(regexp_replace(name, '[^a-zA-Z0-9 ]', '', 'g'), ' '))) AS word
    FROM
        movies
),
word_frequency AS (
    SELECT
        word,
        COUNT(*) AS frequency
    FROM
        word_extraction
    WHERE
        word <> ''
    GROUP BY
        word
)
INSERT INTO word_counts (word, frequency)
SELECT
    word,
    frequency
FROM
    word_frequency;

""")

def searchForMovies(movie_name):
    conn = db_utils.get_db_connection()
    cur = conn.cursor()
    