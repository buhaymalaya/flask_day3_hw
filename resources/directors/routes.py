from flask import request
from flask.views import MethodView
from uuid import uuid4

from schemas import DirectorSchema
from . import bp 

from db import directors

@bp.route('/director')
class DirectorList(MethodView):
    
    @bp.response(200, DirectorSchema(many=True))
    def get(self):
        return list(directors.values())

    @bp.arguments(DirectorSchema)
    @bp.response(201, DirectorSchema)
    def post(self, data):

        director_id = uuid4().hex
        directors[director_id] = data
        return directors[director_id]

@bp.route('/director/<int:id>')
class Director(MethodView):

    @bp.response(200, DirectorSchema)
    def get(self, id):
        if id in directors: 
            return directors[id]
        return {
            'ERROR' : 'INVALID DIRECTOR_ID'
        }, 400
    
    @bp.arguments(DirectorSchema)
    def put(self, data, id):
        data = request.get_json() 
        # REQUEST PACKAGE from FLASK: must include at the top import Flask, request; then, get json()
        if id in directors:
            directors[data['id']] = data
            return {'director updated': directors[id]}, 201
        return {'error' : 'no director found with that id'}, 401

    
    def delete(self, id):
        if id in directors:
            del directors[id]
            return {'director deleted': directors[id]}
        return {'error': 'no user found with that id'}




