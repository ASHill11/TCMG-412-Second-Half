"""
This python program is for TCMG 412 group projects 5-11
Group 0

When changes are made to this script, make sure to rebuild and push to Dockerhub and GitHub
"""

# ALL IMPORTS GO HERE
from flask import Flask, jsonify, request, abort, make_response
import hashlib
import redis

# Defines app name
app = Flask(__name__)

# Gonna need this to initialize later
# docker run --name g0-api --network g0-network -p 4000:4000 my_flask_image
redis_client = redis.Redis(host='localhost', port=6379)

####Project 9 Stuff########
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


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


# Redis Stuff Begins Here ############################################################################


# This is the URI that each of the HTTP methods will interact with
def return_json(key, value, command, result, error):
    json_dict = {"storage-key": key,
                 "storage-value": value,
                 "command": command,
                 "result": result,
                 "error": error}
    return json_dict


@app.route('/keyval/', methods=['POST'])
def keyval_post():
    command = "CREATE new key/some value"
    try:
        data = request.get_json()
    except:
        error = "Unable to add pair: bad JSON"
        json_dict = return_json("", "", command, False, error)
        response = make_response(json_dict, 400)
        return response

    # Iterate over key-value pairs in JSON dictionary

    for key, value in data.items():
        # Check if key already exists in Redis
        if redis_client.get(key):
            error = "Unable to add pair: key already exists"
            json_dict = return_json(key, value, command, False, error)
            response = make_response(json_dict, 409)
            return response

        redis_client.set(key, value)

    error = ""
    json_dict = return_json(key, value, command, True, error)
    response = make_response(json_dict, 200)
    return response


@app.route('/keyval/<string:input_string>', methods=['GET'])
def keyval_get(input_string):
    command = "GET key/value pair"
    value = redis_client.get(input_string)
    print(value)
    if value is None:
        error = "Unable to get pair: key does not exist"
        json_dict = return_json(input_string, value, command, False, error)
        response = (json_dict, 404)
        return response

    json_dict = return_json(input_string, value.decode('utf-8'), command, True, "")
    return json_dict


@app.route('/keyval/', methods=['PUT'])
def keyval_put():
    command = "PUT new value on existing key"
    try:
        data = request.get_json()
    except:
        error = "Unable to change value: invalid JSON"
        json_dict = return_json("", "", command, False, error)
        response = make_response(json_dict, 400)
        return response

    # Iterate over key-value pairs in JSON dictionary
    for key, value in data.items():
        # Check if key already exists in Redis
        if redis_client.get(key):
            redis_client.set(key, value)

        else:
            error = "Unable to change value: key does not exist"
            json_dict = return_json(key, value, command, False, error)
            response = make_response(json_dict, 404)
            return response

    json_dict = return_json(key, value, command, True, "")
    response = make_response(json_dict, 200)
    return response


@app.route('/keyval/<string:key>', methods=['DELETE'])
def keyval_delete(key):
    command = f"DELETE {key}"
    value = redis_client.get(key)
    print(key)
    print(value)
    # Check if key exists in Redis
    if not redis_client.get(key):
        error = "Unable to delete pair: key does not exist"
        json_dict = return_json(key, value.decode('utf-8'), command, False, error)
        response = make_response(json_dict, 404)
        return response

    # Delete key-value pair from Redis
    json_dict = return_json(key, value.decode('utf-8'), command, True, "")
    response = make_response(json_dict, 200)

    redis_client.delete(key)
    return response


# DEBUG
@app.route('/keyval/all', methods=['GET'])
def keyval_get_all():
    keys = redis_client.keys('*')
    keyvals = {}
    for key in keys:
        keyvals[key.decode()] = redis_client.get(key).decode()
    return jsonify(keyvals)


"""
DEBUG CODE
endpoints = app.url_map.iter_rules()
for endpoint in endpoints:
    print(endpoint.rule, endpoint.endpoint, endpoint.methods)
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
