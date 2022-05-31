from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re # This is the REGEX Module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# class to match database. ie. id, first_name, last_name etc..
class User:
    schema = "users"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # self.???? = []  # A user with many of ??? somtimes needed later

    @classmethod
    def register(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.schema).query_db(query, data)

    #@classmethod
    #def get_all(cls):
        #query = "SELECT * FROM users;"
        #results = connectToMySQL(cls.schema).query_db(query)
        #users = []
        #for row in results:
            #users.append(cls(row))
        #return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query,data)
        if len(results) == 0:
            return None
        else:
            return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user["first_name"]) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.")
        if len(user["last_name"]) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Email is invalid.")
        data = {
            "email": user["email"]
        }
        false_user = User.get_by_email(data)
        if false_user != False:
            is_valid = False
            flash("Email is already registered.")
        if len(user["password"]) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.")
        if user["password"] != user["confirm_password"]:
            is_valid = False
            flash("Passwords must agree.")
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        email_data = {
            "email": user["email"]
        }
        false_user = User.get_by_email(email_data)
        if false_user == False:
            is_valid = False
            flash("Invalid login.")
            return is_valid
        if not bcrypt.check_password_hash(false_user.password, user['password']):
            is_valid = False
            flash("Invalid login.")
        return is_valid


