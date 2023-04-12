"""
This python program is for TCMG 412 group projects 5-11
Group 0

When changes are made to this script, make sure to rebuild and push to dockerhub
"""

# ALL IMPORTS GO HERE
from flask import Flask, jsonify
import hashlib

# Defines app name
app = Flask(__name__)


# Testing home page here
@app.route('/')
def home():
    return 'Howdy, please use a valid URL to use this API.'


# Hex uri
@app.route('/md5/<string:input_string>')
def md5(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    result = {'input': input_string, 'output': md5_hash}
    return jsonify(result)


@app.route('/md5/')
def missing_hash():
    return 'Error: Missing argument'


# Factorial URI
@app.route('/factorial/<int:n>')
def factorial(n):
    if n < 0:
        return jsonify({'input': n, 'output': 'Error: input should be a positive integer'}), 400
    elif n == 0:
        return jsonify({'input': n, 'output': 1})
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        result = {'input': n, 'output': fact}
        return jsonify(result)


@app.route('/factorial/')
def missing_factorial():
    return 'Error: Missing argument'


# Fibonacci URI
@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    if n < 0:
        return jsonify({'input': n, 'output': 'Error: input should be a positive integer'})
    elif n == 0:
        return jsonify({'input': n, 'output': []})
    elif n == 1:
        return jsonify({'input': n, 'output': [0, 1, 1]})
    else:
        fib = [0, 1]
        while fib[-1] + fib[-2] <= n:
            fib.append(fib[-1] + fib[-2])
        result = {'input': n, 'output': fib}
        return jsonify(result)


@app.route('/fibonacci/')
def missing_fib():
    return 'Error: Missing argument'


# Prime URI
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


@app.route('/is-prime/')
def missing_prime():
    return 'Error: Missing argument'


# Slack URI
@app.route('/slack-alert/<string:message>')
def slack_alert(message):
    # Your code to post to Slack goes here
    result = {'input': message, 'output': True}  # Assuming that posting to Slack always succeeds
    return jsonify(result)

############## Redis Stuff Begins Here ############################################################################


"""
Commenting all of this out for now because I'm pretty sure we'll be running from the provided Redis container
# create Redis client object
redis_host = "127.0.0.1"
redis_port = 4000
redis_client = redis.Redis(host='127.0.0.1', port=4000)
"""


# This is the URI that each of the HTTP methods will interact with
@app.route('/keyval', methods=['POST'])
def keyval_post():
    return 'Howdy POST'


@app.route('/keyval/<string:input_string>', methods=['GET'])
def keyval_get(input_string):
    return f'This was your input: {input_string}'


@app.route('/keyval', methods=['PUT'])
def keyval_put():
    return 'Howdy PUT'


@app.route('/keyval', methods=['DELETE'])
def keyval_delete():
    return 'Howdy DELETE'


endpoints = app.url_map.iter_rules()
for endpoint in endpoints:
    print(endpoint.rule, endpoint.endpoint, endpoint.methods)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
