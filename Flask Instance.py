#Import Modules
from flask import Flask
import redis


app = Flask(__name__)

# create Redis client object
redis_host = "127.0.0.1"
redis_port = 4000
redis_client = redis.Redis(host='127.0.0.1', port=4000)

#key value code
@app.route('/')
def index():
    # use the Redis client object to interact with Redis
    redis_client.set('key', 'value@app.route('/')
    return f'The value of "key" is {value}'


#debug?
if __name__ == '__main__':
    app.run(debug=True)