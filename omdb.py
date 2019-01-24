# Load the required libraries
import requests
import pandas as pd

# Retrieved API
with open('data/omdb_api.txt', 'r') as my_file:
    my_api = my_file.read()

my_api

# Movie to download
movies = pd.read_table('data/movie_list.txt').values.flatten().tolist()

# List to store results
m_title = []
m_year = []
m_rt = []
m_boxOffice = []

# API main url
omdb_api = 'http://www.omdbapi.com/?t='

for i, movie in enumerate(movies):
    # Set-up the API URL
    movie.replace(" ", "+")
    api_call = omdb_api + movie + '&apikey=' + my_api

    # Retrieve the data
    m_data = requests.get(api_call, timeout=10)

    # Convert the data in JSON
    m_json = m_data.json()

    # Retrieve Movie Title
    m_title.append(m_json.get('Title'))

    # Retrieve Year Release
    m_year.append(m_json.get('Year'))

    # Retrieve Rotten Tomatoes Ratings
    ratings = m_json.get('Ratings', [])

    m_rt.append('NaN')

    for rating in ratings:
        if rating.get('Source') == 'Rotten Tomatoes':  # Find the correct source
            m_rt.pop()
            m_rt.append(rating.get('Value'))

    # Retrieve Box Office
    m_boxOffice.append(m_json.get('BoxOffice'))

    print('Completed', m_title[i])  # debugging purposes

# Create a DataFrame
m_dataframe = pd.DataFrame({'title': m_title,
                            'year': m_year,
                            'rt_rating': m_rt,
                            'boxoffice': m_boxOffice})

m_dataframe

movies2 = pd.read_table('data/movie_list.txt')
movies2.values.flatten().tolist()[13].replace(')', '').split(' (')
