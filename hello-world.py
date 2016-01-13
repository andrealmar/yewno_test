from flask import Flask
from redis import Redis

#used to get the ip addresses from http requests
from flask import request
from flask import jsonify

#used to get the timestamp of the server
import datetime

app = Flask(__name__)
redis = Redis(host='redis', port= 6379)

"""
@app.route('/')
def hello():
    redis.set('ip', request.remote_addr)
    redis.set('timestamp', datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
    ip = redis.get('ip')
    timestamp = redis.get('timestamp')
    return (ip + timestamp)
"""

#returns {“message”: “hello world”}
@app.route("/v1/<name>", endpoint="hello-world")
def hello_world(name):
    redis.set('ip', request.remote_addr)
    redis.set('timestamp', datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
    ip = str(redis.get('ip'))
    timestamp = str(redis.get('timestamp'))
    return jsonify({'message': "hello world"})

#return /v1/logs
@app.route("/v1/logs", methods=["GET"])
def logs():
    log_list = [
        {"endpoint": 'hello-world'},
        {"ip": ip},
        {"timestamp": timestamp}
    ]
    return jsonify(logset = log_list)

#returns /v1/hello-world/logs
@app.route("/v1/hello-world/logs", methods=["GET"])
def hello_world_logs():
    hello_world_logs_list = [
        {"ip": str(redis.get('ip'))},
        {"timestamp": str(redis.get('timestamp'))}
    ]
    return jsonify(logs = hello_world_logs_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
