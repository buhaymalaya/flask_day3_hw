from marshmallow import Schema, fields

class DirectorSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    imdb_rating = fields.Str()
    first_name= fields.Str()
    last_name= fields.Str()

class MovieSchema(Schema):
    director = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    year = fields.Int(required=True)