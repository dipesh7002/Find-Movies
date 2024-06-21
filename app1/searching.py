import psycopg2
import math

def get_db_connection():
    
    conn = psycopg2.connect(database="NewDB", 
                            host="localhost", 
                            user="postgres",
                            password="admin", 
                            port="5432")
    return conn

 

def TF_IDF(movie_name):
    conn = get_db_connection()
    cur = conn.cursor()
    words_list = movie_name.split(' ')
    IDF_res = IDF(movie_name)
    my_dict = {}
    all_movies_store = []
    TF_IDF_value = []

    for word in words_list:
        

        cur.execute("SELECT movie_name FROM fmovies WHERE movie_name ILIKE %s", ( ('% ' + word + ' %',)))
        all_movies_store = cur.fetchall()
        for full_movie_name in all_movies_store:
            for each_word_movie in full_movie_name:
                if word == each_word_movie:
                    my_dict[word] += 1/len(full_movie_name)
                else:
                    my_dict[word] = 1/len(full_movie_name)
            my_dict[word] = my_dict[word] * IDF_res[word]
                
            TF_IDF_value.append(my_dict)
    return (TF_IDF_value)

def IDF(movie_name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM fmovies")
    total_count = cur.fetchone()
    total_no_of_movies = int(total_count[0])

    my_dict = {}
    word_list = movie_name.split(' ')
    for word in word_list:
        cur.execute("SELECT COUNT(*) FROM fmovies WHERE movie_name ILIKE %s", ( ('% ' + word + ' %',)))
        result_count = cur.fetchone()
        result_count_word = int(result_count[0])
        if result_count_word == 0:
            my_dict[word] = (1 + math.log(total_no_of_movies/(result_count_word + 1)))
        else:
            my_dict[word] = (1 + math.log(total_no_of_movies / result_count_word))
    return my_dict


def cosineSimilarity(movie_name):
    
    value = TF_IDF(movie_name)
    tf_idf_value = value[0]
    store_list = value[1]
    word_list = movie_name.split(' ')
    word_length = len(word_list)

print(TF_IDF("and in"))


