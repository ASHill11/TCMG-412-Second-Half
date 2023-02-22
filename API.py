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
2) Navigate to your python projects directory
3) Enter the following commands
4) mkdir myproject
5) cd myproject
6) py -3 -m venv venv
7) venv\Scripts\activate
8) pip install Flask
9) Copy and paste the given command to update Flask


We need to build an API that runs on port 4000
Expose the following URIs:
/md5/<string>
/factorial/<int>
/fibonacci/<int>
/is-prime/<int>
/stack-alert/<string>
See link above for my detailed instructions

All returned values will and should be JSON 
"""

# ALL IMPORTS GO HERE
from flask import Flask, jsonify
import hashlib
import requests

#Not sure what this is fore but, I think it defines the same of the app that we want to use for this
app = Flask(__name__)

#Hex uri
@app.route('/md5/<string:input_string>')
def md5(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    result = {'input': input_string, 'output': md5_hash}
    return jsonify(result)

#Factorial URI
@app.route('/factorial/<int:n>')
def factorial(n):
    if n < 0:
        return jsonify({'input': n, 'output': 'Error: input should be a positive integer'})
    elif n == 0:
        return jsonify({'input': n, 'output': 1})
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        result = {'input': n, 'output': fact}
        return jsonify(result)
    
#Fibonacci URI
    @app.route('/fibonacci/<int:n>')
    def fibonacci(n):
        if n < 0:
            return jsonify({'input': n, 'output': 'Error: input should be a positive integer'})
        elif n == 0:
            return jsonify({'input': n, 'output': []})
        elif n == 1:
            return jsonify({'input': n, 'output': [0]})
        else:
            fib = [0, 1]
            while fib[-1] + fib[-2] <= n:
                fib.append(fib[-1] + fib[-2])
            result = {'input': n, 'output': fib}
            return jsonify(result)

 #Prime URI
    @app.route('/is-prime/<int:n>')
    def is_prime(n):
        if n < 1:
            return jsonify({'input': n, 'output': 'Error: input should be a positive integer'})
        elif n == 1:
            return jsonify({'input': n, 'output': False})
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    result = {'input': n, 'output': False}
                    return jsonify(result)
            result = {'input': n, 'output': True}
            return jsonify(result)

#Slack URI      
@app.route('/slack-alert/<string:message>')
def slack_alert(message):
    # Your code to post to Slack goes here
    result = {'input': message, 'output': True} # Assuming that posting to Slack always succeeds
    return jsonify(result)

class Users(Resource):
    # methods go here
    pass


class Locations(Resource):
    # methods go here
    pass
