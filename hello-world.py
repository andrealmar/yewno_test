from flask import Flask
from redis import Redis

#used to get the ip addresses from http requests
from flask import request
from flask import jsonify

#used to get the timestamp of the server
import datetime

app = Flask(__name__)
redis = Redis(host='redis', port= 6379)


@app.route('/')
def hello():
    redis.set('ip', request.remote_addr)
    redis.set('timestamp', datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
    ip = redis.get('ip')
    timestamp = redis.get('timestamp')
    return (ip + timestamp)


#returns {“message”: “hello world”}
@app.route("/v1/hello-world", methods=["GET"])
def hello_world():
    return jsonify({'message': "hello world"})

#return /v1/logs
@app.route("/v1/logs", methods=["GET"])
def logs():
    return jsonify({'logs': [{"ip": request.remote_addr, "timestamp": datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")}]})

#returns /v1/hello-world/logs
@app.route("/v1/hello-world/logs", methods=["GET"])
def hello_world_logs():
    return jsonify({'logs': [{"ip": request.remote_addr, "timestamp": datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")}]})

#returns ip address from http request
@app.route("/get_ip", methods=["GET"])
def get_ip():
    return jsonify({'ip': request.remote_addr}), 200

#returns timestamp of the request
@app.route("/get_timestamp", methods=["GET"])
def timestamp():
    ts = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    return jsonify({'timestamp': ts})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
