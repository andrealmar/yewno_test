#Yewno Engineering Test

If you access yourhost:5000/ (in my case it was 192.168.99.100:5000) it will show you how many times the request was made to the Redis Datastore. (in the code lines 12 to 16)

Ex. response: Hello World! I have been seen 50 times.


When you access http://yourhost:5000/v1/hello-world (in my case it was http://192.168.99.100:5000/v1/hello-world) it will return a JSON message and log the IP and Timestamp of who made that request. (in the code: lines 19 to 26)

Ex. response: 
{
  "message": "hello-world"
}


When you access http://localhost:5000/site/logs (in my case it was http://192.168.99.100:5000/site/logs), it will show the screen below:  


![MyLogs][1]  

[1]: https://raw.githubusercontent.com/andrealmar/yewno_test/8e63afd6e2521867ebe3db26493c2017bf479334/static/MyLogs.png

In the NavBar you can see links to the JSON responses and to the Log tables in HTML format

