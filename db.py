# Temp! Do not need after we connect to db 
# Once server is deactivated, added entries will disappear unless hardcoded

directors = {
    1:{
        'id': 1,
        'username': 'jordan_peele',
        'email': 'jp@gm.com',
        'imdb_rating' : '9/10'
    },
    2:{
        'id': 2,
        'username': 'coen_brothers',
        'email': 'cb@gm.com',
        'imdb_rating': '9/10'
    }
}

# simulate something created linked to directors

movies = {
    "1" :{
        'director': 2,
        'title': 'Burn After Reading',
        'description': "A mysterious comedy about two friends with different motives and similar IQ levels",
        'year': 2008
    },
    "2" :{
        'director': 1,
        'title': 'Nope',
        'description': "Horse-wrangling siblings attempting to capture evidence of an unidentified flying object in Agua Dulce, California",
        'year': 2022
    }
}