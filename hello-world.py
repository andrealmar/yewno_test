from flask import Flask, request, jsonify, render_template
from redis import Redis

#used to get the timestamp of the server
import datetime

app = Flask("yewno")
redis = Redis(host='redis', port= 6379)


@app.route('/<nome>')
def hello(nome):
    return render_template("index.html", nome=nome)


#returns {“message”: “hello world”}
@app.route("/v1/<name>", endpoint="hello-world")
def hello_world(name):
    redis.set('ip', request.remote_addr)
    redis.set('timestamp', datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
    ip = str(redis.get('ip'))
    timestamp = str(redis.get('timestamp'))
    return jsonify({'message': name})


#return /v1/logs
@app.route("/v1/logs", methods=["GET"])
def logs():
    log_list = [
        {"endpoint": 'hello-world'},
        {"ip": str(redis.get('ip'))},
        {"timestamp": str(redis.get('timestamp'))}
    ]
    return jsonify({'logset': log_list})


#returns /v1/hello-world/logs
@app.route("/v1/hello-world/logs", methods=["GET"])
def hello_world_logs():
    hello_world_logs_list = [
        {"ip": str(redis.get('ip'))},
        {"timestamp": str(redis.get('timestamp'))}
    ]
    return jsonify({'logs': hello_world_logs_list})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
