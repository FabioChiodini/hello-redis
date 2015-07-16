import os
import uuid
import redis
import urlparse
import json

from flask import Flask
app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"
counterK = 0
COLOR = BLUE

rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])

r.set('connectionsK', '0')

@app.route('/')
def hello():
        global counterK 
	global connectionsvarK
        counterK = counterK +1
        r.incr ('connectionsK')
        return """
	<html>
	<body bgcolor="{}">

	<center><h1><font color="white">Hi, I'm GUID:<br/>
	{}
        <center><h1><font color="white">Page Hits for this deploy:<br/>
        {}
	</center>
        <center><h1><font color="white">GLOBAL Page Hits:<br/>
       

	</body>
	</html>
	""".format(COLOR,my_uuid, counterK)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
