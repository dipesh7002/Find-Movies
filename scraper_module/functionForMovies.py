from bs4 import BeautifulSoup
import requests
import random
import db_utils
import movie_urls

user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36', 
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36']

def printSucess():
        print("**********************")
        print("**********************")
        print("All added from Fmovies")
        print("**********************")
        print("**********************")
  

def addMoviesToDatabase(movie_list, url_list, sql_table_name):
    conn = db_utils.get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT COUNT(*) FROM {sql_table_name}")
    except:
        print("Table name invalid")
    num = cur.fetchone()

 
    try:
        
        for i, movie in enumerate(movie_list, start=1):
            singleMovie = movie.text.strip()
            cur.execute(f"INSERT INTO {sql_table_name}(SN, movie_name, movie_link) VALUES(%s, %s, %s)",
                        (num[0] + i, singleMovie, url_list[i-1]))
            print(" ")
            print(" ")


    except Exception as e:
        print(f"Unable to add movies to database: {e}")

    conn.commit()
    cur.close()
    conn.close()

def fmovies():

    response = requests.get(movie_urls.fmovies_url1)
    soup = BeautifulSoup(response.text, 'lxml')
    movie_list = soup.find_all('h2', class_='card-title text-light fs-6 m-0')
    sql_table_name = "fmovies"

    href_list = []
    for movie in movie_list:
        parent = movie.find_parent('a')
        if parent and parent.has_attr('href'):
            href = parent['href']
            href_list.append(href)

    addMoviesToDatabase(movie_list, href_list, sql_table_name)
    print("DONE: 1")

    try:

        for i in range(2, 617):
            url = movie_urls.fmovies_url2.format(i)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            movie_list = soup.find_all('h2', class_='card-title text-light fs-6 m-0')
            href_list = []
            for movie in movie_list:
                parent = movie.find_parent('a')
                if parent and parent.has_attr('href'):
                    href = parent['href']
                    href_list.append(href)

            addMoviesToDatabase(movie_list, href_list, sql_table_name)
            print(f"DONE: {i}")
    except:
        printSucess()

def hindimovies():
    response = requests.get(movie_urls.hindimovies_url1)
    soup = BeautifulSoup(response.text, 'lxml')
    movie_list = soup.findAll('a', class_='font-bold')
    movie_link = soup.findAll(class_='font-bold')
    href_list = []
    sql_table_name = "hindi_movies"


    for movie in movie_link:
        href_list.append("https://www.hindimovies.to" + movie.get('href'))
    addMoviesToDatabase(movie_list, href_list, sql_table_name)
    for i in range(2, 1029):
        url = movie_urls.hindimovies_url2.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        movie_list = soup.findAll('a', class_='font-bold')
        movie_link = soup.findAll(class_='font-bold')
        href_list = []


        for movie in movie_link:
            href_list.append("https://www.hindimovies.to" + movie.get('href'))
        addMoviesToDatabase(movie_list, href_list, sql_table_name)
        print(f"::::::::::I am in {i}th page::::::::::")

def one_two_three_movies():
    # response = requests.get(movie_urls.one_two_three_movies_url1)
    # print(response)
    # soup = BeautifulSoup(response.text, 'lxml')
    # movie_tags = soup.findAll('div', class_='data')
    movie_list = []
    movie_link = []
    # for tag in movie_tags:
    #     a_tag = tag.find('a')
    #     if a_tag:
    #         movie_list.append(a_tag)
    #         movie_link.append(a_tag['href'])
    sql_table_name = "one_two_three_movies"
    # print("Added 1 ")
    # addMoviesToDatabase(movie_list, movie_link, sql_table_name)
    for i in range(505, 605):
        url = movie_urls.one_two_three_movies_url2.format(i)
        response = requests.get(url, headers={'User-Agent': random.choice(user_agents)})    
        soup = BeautifulSoup(response.text, 'lxml')
        movie_tags = soup.findAll('div', class_='data')
        for tag in movie_tags:
            a_tag = tag.find('a')
            if a_tag:
                movie_list.append(a_tag)
                movie_link.append(a_tag['href'])
        addMoviesToDatabase(movie_list, movie_link, sql_table_name)
        print("Added", i)


def uwatchfree():
    for i in range(1, 3313):
        response = requests.get(movie_urls.uwatchfree.format(i), headers={'User_Agent': random.choice(user_agents)})
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        movie_tags = soup.findAll(class_='browse-movie-title')
        movie_link = []
        sql_table_name = "uwatchfree"
        for tag in movie_tags:
            movie_link.append(tag['href'])
        addMoviesToDatabase(movie_tags, movie_link, sql_table_name)

def popcornflix():
    for i in range(1, 3313):
        response = requests.get(movie_urls.popcornflix.format(i), headers={'User_Agent': random.choice(user_agents)})
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        movie_tags = soup.findAll(class_='browse-movie-title')
        movie_link = []
        sql_table_name = "popcornflix"
        for tag in movie_tags:
            movie_link.append(tag['href'])
        addMoviesToDatabase(movie_tags, movie_link, sql_table_name)

def onehd():
    for i in range(1, 1023):
        response = requests.get(movie_urls.onehd.format(i), headers={'User_Agent': random.choice(user_agents)})
        soup = BeautifulSoup(response.text, 'lxml')
        movie_tags = soup.findAll(class_='film-name sum-2')
        movie_link = [] 
        sql_table_name = "onehd"
        for tag in movie_tags:
            a_tag = tag.find('a')
            if a_tag:
                href = a_tag['href']
                movie_link.append(href)
        addMoviesToDatabase(movie_tags, movie_link, sql_table_name)
        print("Done", i)
        print("Done", i) 


def bmovies():
    # response = requests.get(movie_urls.bmovies_url1, headers={'User_Agent': random.choice(user_agents)})
    # print(response.status_code)
    # soup = BeautifulSoup(response.text, 'lxml')
    # movie_name = soup.findAll(class_='mli-info')
    # movie_tags = soup.findAll(class_='ml-mask jt')
    # movie_link = []
    sql_table_name = 'bmovies'
    # for tag in movie_tags:
    #     movie_link.append(tag.get('href'))
    # addMoviesToDatabase(movie_name, movie_link, sql_table_name)
    for i in range(1517, 2, -1):
        response = requests.get(movie_urls.bmovies_url2.format(i), headers={'User_Agent': random.choice(user_agents)})
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        movie_name = soup.findAll(class_='mli-info')
        movie_tags = soup.findAll(class_='ml-mask jt')
        movie_link = []
        for tag in movie_tags:
            movie_link.append(tag.get('href'))
        addMoviesToDatabase(movie_name, movie_link, sql_table_name)
        