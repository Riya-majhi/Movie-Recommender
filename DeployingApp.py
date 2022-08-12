import streamlit as st
from PIL import Image
import base64
import pickle
import pandas as pd
import requests
import random

# image for icon
img = Image.open('image/images.jpg')
st.set_page_config(page_title="Movie Recommender",page_icon=img)

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

#setting backgrond image
@st.cache
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.markdown('<link href="lib/font-awesome/css/font-awesome.min.css" rel="stylesheet">',unsafe_allow_html=True)
# bootstrap link
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css">', unsafe_allow_html=True)



def set_png_as_page_bg(png_file):
    bin_str = get_base64(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    # background-size: contain;
    # background-repeat: no-repeat;
    # background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
#passing bg image
set_png_as_page_bg('image/Netflix-content-titles.png')

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=17f6a4b903a6a455cfe7dc5c76bb62ec&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except :
        pass
    
def recommend(movie, rec, similarity):
    index = movies[movies[rec] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:15]:
        
        count=0
        if(movies.iloc[i[0]].TMDBid!=None):
            movie_id = movies.iloc[i[0]].TMDBid
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].Title)
            count+=1
            if(count==5):
                break
        else:
            pass

    return recommended_movie_names,recommended_movie_posters


def streamlitPost(recommended_movie_names,recommended_movie_posters):
    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            st.subheader(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        except :
            file_ = open("image/not_found.png", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/png;base64,{data_url}" alt="">',
                unsafe_allow_html=True,)
    with col2:
        try:
            st.subheader(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        except :
            file_ = open("image/not_found.png", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/png;base64,{data_url}" alt="">',
                unsafe_allow_html=True,)

    with col3:
        try:
            st.subheader(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        except :
            file_ = open("image/not_found.png", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/png;base64,{data_url}" alt="">',
                unsafe_allow_html=True,)

    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            st.subheader(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        except :
            file_ = open("image/not_found.png", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/png;base64,{data_url}" alt="">',
                unsafe_allow_html=True,)
    with col2:
        try:
            st.subheader(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
        except :
            file_ = open("image/not_found.png", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/png;base64,{data_url}" alt="">',
                unsafe_allow_html=True,)

    with col3:
        pass



def home():
    randMvi_dict=pickle.load(open('random_movie_dict.pkl','rb'))
    randomMvi=pd.DataFrame(randMvi_dict)
    st.subheader('Here are some movies for you')
    randomlist = random.sample(range(54),9)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(randomMvi['Title'][randomlist[0]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[0]]))
            
    with col2:
        st.subheader(randomMvi['Title'][randomlist[1]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[1]]))
    with col3:

        st.subheader(randomMvi['Title'][randomlist[2]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[2]]))
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(randomMvi['Title'][randomlist[3]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[3]]))
    with col2:
        st.subheader(randomMvi['Title'][randomlist[4]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[4]]))
    with col3:
        st.subheader(randomMvi['Title'][randomlist[5]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[5]]))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(randomMvi['Title'][randomlist[6]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[6]]))
    with col2:
        st.subheader(randomMvi['Title'][randomlist[7]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[7]]))
    with col3:
        st.subheader(randomMvi['Title'][randomlist[8]])
        st.image(fetch_poster(randomMvi['TMDBid'][randomlist[8]]))


    city = pd.DataFrame({
        'awesome cities' : ['Kolkata'],
        'lat' : [22.5726],
        'lon' : [88.3639]
        })
    # st.map(city)
    # st.subheader("Contact us")
    st.markdown('''<div style="text-align: center"> <h1>TEAM</h1> </div>''', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('image//Sudipta.png', caption="Sudipta Banerjee", width=150)

    with col2:
        st.image('image//Sathi.png',caption="Sathi Das", width=150)

    with col3:
        st.image('image//Apurba.png',caption="Apurba Bhattacharjee", width=150)

    with col4:
        st.image('image//riya.png',caption="Riya Majhi", width=150)

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        file_ = open("image/f.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)

    with col2:
        file_ = open("image/l1.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)
    with col3:
        file_ = open("image/f.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)

    with col4:
        file_ = open("image/l1.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)
    with col5:
        file_ = open("image/f.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)

    with col6:
        file_ = open("image/l1.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)
    with col7:
        file_ = open("image/f.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)

    with col8:
        file_ = open("image/l1.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
                f'<a href="https://www.linkedin.com/in/riya-majhi-667a62181/"><img src="data:image/png;base64,{data_url}"></a>',
                unsafe_allow_html=True,)























def movie():
    global movies
    
    similarity=pickle.load(open('similarity_mvi.pkl','rb'))
    movie = st.selectbox(
    '',
    movies['Title'].values)
    if st.button('Recommend'):
        recommended_movie_names,recommended_movie_posters = recommend(movie, 'Title', similarity)
        streamlitPost(recommended_movie_names,recommended_movie_posters)
    
def director():
    director_dict=pickle.load(open('director_dict.pkl','rb'))
    director=pd.DataFrame(director_dict)
    similarity=pickle.load(open('similarity_director.pkl','rb'))
    dir = st.selectbox(
    '',
    director['Director'].values)
    if st.button('Recommend'):
        recommended_movie_names,recommended_movie_posters = recommend(dir.replace(' ',''), 'Director', similarity)
        streamlitPost(recommended_movie_names,recommended_movie_posters)

def genre():
    genres_dict=pickle.load(open('genres_dict.pkl','rb'))
    genres=pd.DataFrame(genres_dict)
    similarity=pickle.load(open('similarity_genres.pkl','rb'))
    genr = st.selectbox(
    '',
    genres['genres'].values)
    if st.button('Recommend'):
        recommended_movie_names,recommended_movie_posters = recommend(genr, 'genres', similarity)
        streamlitPost(recommended_movie_names,recommended_movie_posters)
        
def actor():
    actor_dict=pickle.load(open('actor_dict.pkl','rb'))
    actor=pd.DataFrame(actor_dict)
    name = st.selectbox(
    '',
    actor['actorName'].values)
    if st.button('Recommend'):
        # pass
        from imdb import IMDb
        ia = IMDb()
        top_10=ia.get_top250_indian_movies()
        def recommend_actors(name):
            films=[]
            recommended_movie_names = []
            recommended_movie_posters = []
            name=name.replace(' ','')
            for i in range(4101):
                if name in movies['actors'][i] :
                    films.append(movies['Title'][i])
            if len(films)<5:
                id=0
                for k in range(0,6-len(films)):
                    films.append(top_10[id]['title'])
                    id=id+2*8
            l=5
            for j in films:
                if l==0:
                    break
                else:
                    l-=1
                    movie_id=movies[movies['Title']==(j)].TMDBid
                    recommended_movie_posters.append(fetch_poster([id for id in movie_id][0]))
                    recommended_movie_names.append(j)

            return recommended_movie_names,recommended_movie_posters

        try:
            recommended_movie_names,recommended_movie_posters = recommend_actors(name)
            streamlitPost(recommended_movie_names,recommended_movie_posters)
        except :
            file_ = open("image/404.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,)

  
               
if __name__ == '__main__':

    st.title('Bollywood Movie Recomendation')
    opt = st.selectbox(
        'How would you like to connected',
        ('Home','Movie','Genre','Actor','Director'))
    
    if opt=='Home':
        home()
    elif opt=='Movie':
        movie()
    elif opt=='Genre':
        genre()
    elif opt=='Actor':
        actor()
    elif opt=='Director':
        director()

#hide footer and setting menu
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

