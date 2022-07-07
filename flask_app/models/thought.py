from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Thought:
    db_name="thoughts"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.date_made = db_data['date_made']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO thoughts (name, description, instructions, date_made, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM thoughts WHERE id = %(id)s"
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        return results[0] 

    @classmethod
    def update(cls, data):
        query = "UPDATE thoughts SET name=%(name)s, description =  %(description)s, instructions=%(instructions)s, date_made =%(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM thoughts;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_thoughtd= []
        for row in results:
            all_though†s.append(row)
        return all_though†s
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM thought WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_thought(thought):
        is_valid = True
        if len(thought['name'])<3:
            flash('Name of the thought must be at least 2 characters', "thought")
            is_valid=False
        if len(thought['instructions'])<3:
            flash('Instructions must be at least 3 characters', "thought")
            is_valid=False
        if len(thought['description'])<3:
            flash('Description must be at least 3 characters', "thought")
            is_valid=False
        if thought['date_made'] == "":
            flash('Please enter a date', "thought")
            is_valid=False
        return is_valid
    
    