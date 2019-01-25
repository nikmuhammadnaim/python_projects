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
    movie = movie.replace(" ", "+").replace(')', '')

    # Check if year is provided
    m_yr = movie.split('+(')
    if len(m_yr) > 1:
        api_call = omdb_api + m_yr[0] + '&y=' + m_yr[1] + '&apikey=' + my_api

    else:
        api_call = omdb_api + movie + '&apikey=' + my_api

    # Retrieve the data
    m_data = requests.get(api_call, timeout=5)

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

    # Debugging purposes
    # print('Completed', m_title[i])

# Create a DataFrame
m_dataframe = pd.DataFrame({'title': m_title,
                            'year': m_year,
                            'rt_rating': m_rt,
                            'boxoffice': m_boxOffice})
# Check the DataFrame
m_dataframe.head()

# Store the result in csv
m_dataframe.to_csv('data/movie_rt_bo.csv', index=False)
