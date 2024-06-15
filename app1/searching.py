import psycopg2
import math

def get_db_connection():
    
    conn = psycopg2.connect(database="NewDB", 
                            host="localhost", 
                            user="postgres",
                            password="admin", 
                            port="5432")
    return conn

def normalizedTF(movie_name):
    conn = get_db_connection()
    cur = conn.cursor()
    words_list = movie_name.split(' ')
    my_dict = {}
    store_list = []
    normalized_Frequency = []
    for word in words_list:
        cur.execute("SELECT movie_name FROM fmovies WHERE movie_name ILIKE %s", ( ('% ' + word + ' %',)))
        store_list = cur.fetchall()
        for stored_items in store_list:
            for items in stored_items:
                if word == items:
                    my_dict[word] += 1
                else:
                    my_dict[word] = 1
            normalized_Frequency.append(my_dict)
    return (normalized_Frequency, store_list)



def IDF(movie_name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM fmovies")
    count = cur.fetchone()
    total_no_of_movies = int(count[0])
    
    my_dict = {}
    result_TF = normalizedTF(movie_name)
    word_list = movie_name.split(' ')
    for word in word_list:
        print(len(result_TF[1]))
        print(total_no_of_movies)
        my_dict[word] = (1 + math.log(total_no_of_movies / len(result_TF[1]) ))
    return my_dict

print(IDF("and"))
