"""
Everything in this comment section should remain static
This python program is for TCMG 412 group projects 5-11
Group 0
"""

"""
Everything in this comment section should change week to week
Assignment link:
https://canvas.tamu.edu/courses/187785/assignments/1572748

BEFORE YOU BEGIN YOU MUST INSTALL FLASK
Windows Users:
1) Open command line
2) Navigate to the directory your py file is in
3) Enter the following commands
4) py -3 -m venv venv
5) venv\\Scripts\\activate
6) pip install Flask


We need to build an API that runs on port 4000
Expose the following URLs:
/md5/<string>
/factorial/<int>
/fibonacci/<int>
/is-prime/<int>
/stack-alert/<string>
See link above for my detailed instructions

All returned values should be JSON
"""

# ALL IMPORTS GO HERE
from flask import flask
from flask_restful import Resource, Api, reqparse


class Users(Resource):
    # methods go here
    pass


class Locations(Resource):
    # methods go here
    pass


api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations
