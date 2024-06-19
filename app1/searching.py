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
    store_list = []
    TF_IDF_value = []

    for word in words_list:
        

        cur.execute("SELECT movie_name FROM fmovies WHERE movie_name ILIKE %s", ( ('% ' + word + ' %',)))
        store_list = cur.fetchall()
        for stored_items in store_list:
            for word in words_list:
                for items in store_list:
                    if word == items:
                        my_dict[word] += 1/len(stored_items)
                    else:
                        my_dict[word] = 1/len(stored_items)
                my_dict[word] = my_dict[word] * IDF_res[word]
                
                TF_IDF_value.append(my_dict)
        return (TF_IDF_value, store_list)



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
# def TF(movie_name):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     movie_name_to_list = movie_name.split(' ')
#     TF_value = []
#     movie_words = []
    
#     for each_word_in_movie in movie_name_to_list:
#         word_count = 0
#         total_words_in_all_movies = 0

#         # Use a SQL pattern to match the word in movie names
#         cur.execute("SELECT movie_name FROM fmovies WHERE movie_name ILIKE %s", ( ('% ' + each_word_in_movie + ' %',)))
#         query_store_list = cur.fetchall()

#         for query_each_movie in query_store_list:
#             movie_words = query_each_movie[0].split(' ')  # split the movie name into words
#             word_count += movie_words.count(each_word_in_movie)
#             total_words_in_all_movies += len(movie_words)
        
#         if total_words_in_all_movies > 0:
#             tf = word_count / total_words_in_all_movies
#         else:
#             tf = 0
        
#         TF_value.append({each_word_in_movie: tf})
    
#     cur.close()
#     conn.close()


# result = TF("and")
# print(result)

# A.B = |A| * |B| cos thita
#cosine similarity = A.B/(|A| * |B|)

