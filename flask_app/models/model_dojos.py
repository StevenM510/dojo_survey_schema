from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 2:
            flash("location must be at least 2 characters.")
            is_valid = False
        if len(dojo['language']) < 5:
            flash("language must be at least 5 characters.")
            is_valid = False
        if len(dojo['comment']) <= 1:
            flash("leave a comment.")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        pass


    @classmethod
    def get_all(cls):
        pass


    @classmethod
    def get_by_id(cls, id):
        pass



    @classmethod
    def update_one(id):
        pass
