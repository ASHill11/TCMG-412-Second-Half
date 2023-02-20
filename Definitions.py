#This is my attempt to create the API Definitions


#Import Modules
from flask import Flask, jsonify
import hashlib

#Not sure what this is fore but, I think it defines the same of the app that we want to use for this
app = Flask(__name__)

#Hex uri
@app.route('/md5/<string:input_string>')
def md5(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    result = {'input': input_string, 'output': md5_hash}
    return jsonify(result)




