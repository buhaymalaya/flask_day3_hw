from flask import request, jsonify, json
from flask.views import MethodView # import this to implement parent class to inherit from
from flask_smorest import abort

from uuid import uuid4 # generates unique id (randomized)

from . import bp

from schemas import MovieSchema
from db import directors, movies # from database py file


# group routes using the same endpoint; all post routes
@bp.route('/movie') # apply decorator route to each class; no need to do for each method
class MovieList(MethodView):

    @bp.arguments(MovieSchema) # we want the arguments coming in to be validated by schema (think:field requirements)
    def post(self, movie_data): # method name is now the type of http request(think:crud) built to receive
        if movie_data['director'] not in directors:
            return {"message": "director does not exist"}, 400 # bad request status code
        movie_id = uuid4().hex # assigning id to uuid, hex - returns hexadecimal string
        movies[movie_id] = movie_data # adds post_id as key to the post_data
        return {
            'message': "Movie created",
            'movie-id': movie_id
            }, 201

    @bp.response(200, MovieSchema(many=True)) # think of all items in dict
    def get(self):
        return list(movies.values())
    
@bp.route('/movie/<movie_id>') # grouping requests with specified post id (singular) endpoint
class Movie(MethodView): # remember to inherit from imported parent MethodView

    @bp.response(200, MovieSchema)
    def get(self, movie_id):
        try: 
            return movies[movie_id]
        except KeyError:
            return {'message':"invalid movie"}, 400

    @bp.arguments(MovieSchema)
    def put(self, movie_data, movie_id): # inject slug parameter from route decorator
        if movie_id in movies: # post_id no longer extracted from post_data; now coming from url parameter
            movies[movie_id] = {k:v for k,v in movie_data.items() if k != 'id'} 

            return {'message': f'post: {movie_id} updated'}, 201 # create request ok
        
        return {'message': "invalid post"}, 400


    def delete_movie(self, movie_id):
        if movie_id not in movies:
            return { 'message' : "Invalid Post"}, 400
        
        movies.pop(movie_id)
        return {'message': f'Post: {movie_id} deleted'}
