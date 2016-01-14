from flask import Flask, request, jsonify, render_template
from redis import Redis
import json

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
    return jsonify({'message': name })


#return /v1/logs
@app.route("/v1/logs", methods=["GET"])
def logs():
    log_list = {
        "endpoint": 'hello-world',
        "ip": redis.get('ip').decode('utf-8'),
        "timestamp": redis.get('timestamp').decode('utf-8'),
    }
    return jsonify({'logset': log_list})
    # log_list_data = {'logset': log_list}
    # return render_template('index.html', data=log_list_data)


#return /v1/logs
@app.route("/site/logs", methods=["GET"])
def site_logs():
    """
      data_list = []
      for ix in range(10):
        perform data fetching
        your_object = {
          "endpoint": 'aaaa',
          "ip": redis query,
          "timestamp": redis query
        }
        data_list.append(your_object)
    """
    log_dict = {
        "endpoint": 'hello-world',
        "ip": redis.get('ip').decode('utf-8'),
        "timestamp": redis.get('timestamp').decode('utf-8'),
    }
    # return jsonify({'logset': log_list})
    log_list_data = {
      'logset': [log_dict]
    }
    return render_template('index.html', data=log_list_data)


#returns /v1/hello-world/logs
@app.route("/v1/hello-world/logs", methods=["GET"])
def hello_world_logs():
    hello_world_logs_list = {
        "ip": redis.get('ip').decode('utf-8'),
        "timestamp": redis.get('timestamp').decode('utf-8'),
    }

    hello_world_data = {'logs': hello_world_logs_list}

    return jsonify({'logs': hello_world_logs_list})
    # return render_template('index.html', hello_world=hello_world_data)


#returns
@app.route("/site/hello-world/logs", methods=["GET"])
def site_hello_world_logs():
    hello_world_logs_list = {
        "ip": redis.get('ip').decode('utf-8'),
        "timestamp": redis.get('timestamp').decode('utf-8'),
    }

    hello_world_data = {'logset': [hello_world_logs_list]}

    # return jsonify({'logs': hello_world_logs_list})
    return render_template('index.html', data=hello_world_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
