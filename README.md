#Yewno Engineering Test

If you access yourhost:5000/ (in my case it was 192.168.99.100:5000) it will show you how many times the request was made to the Redis Datastore. (in the code lines 12 to 16)

Ex. response: Hello World! I have been seen 50 times.


When you access http://yourhost:5000/v1/hello-world (in my case it was http://192.168.99.100:5000/v1/hello-world) it will return a JSON message and log (also store into redis) the IP and Timestamp of who made that request. (in the code: lines 19 to 26)

JSON response:  

```
{
  "message": "hello-world"
}
```


When you access http://localhost:5000/site/logs (in my case it was http://192.168.99.100:5000/site/logs), it will show the screen below:  


![MyLogs][1]  

[1]: https://raw.githubusercontent.com/andrealmar/yewno_test/8e63afd6e2521867ebe3db26493c2017bf479334/static/MyLogs.png

In the NavBar you can see links to the JSON responses and to the Log tables in HTML format

http://192.168.99.100:5000/site/hello-world/logs it will show you the same table but with different JSON response. 

http://192.168.99.100:5000/v1/hello-world/logs
JSON response:  

```
{
  "logs": {
    "ip": "192.168.99.1",
    "timestamp": "Friday, 15. January 2016 06:38PM"
  }
}
```



http://192.168.99.100:5000/v1/logs
JSON response:  

```
{
  "logset": {
    "endpoint": "hello-world",
    "ip": "192.168.99.1",
    "timestamp": "Friday, 15. January 2016 06:38PM"
  }
}
```  

STILL TO DO:  

* Configure nginx (web server) properly to serve the static files.
* Configure Gunicorn to act as a medium between the webserver (nginx) and Python/Flask.
* Configure Supervisor to automate the restart of Gunicorn server each time we make a change in our app.
* Implement the minute level aggregate count of IP addresses.