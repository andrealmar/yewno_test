from flask import Flask
from redis import Redis

#used to get the ip addresses from http requests
from flask import request
from flask import jsonify

app = Flask(__name__)
redis = Redis(host='redis', port= 6379)


@app.route('/')
def hello():
    redis.incr('hits')
    message =  'Hello This is YEWNO Engineering Test. I have been refreshed {0} times.'.format(redis.get('hits'))
    return message

#returns {“message”: “hello world”}
@app.route("/v1/hello-world", methods=["GET"])
def hello_world():
    return jsonify({'message': "hello world"})

#returns ip address from http request
@app.route("/get_ip", methods=["GET"])
def get_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
