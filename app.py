import streamlit as st
import pickle
import pandas as pd
import requests



movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies  = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similar.pkl', 'rb'))


def fetch_poster(movie_id_y):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=38839046c23fbf8aec84a7a0a49f5051&langauage=en-US'.format(movie_id_y))
    data = response.json()
    # print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id_y
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select the movie : ',
movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])