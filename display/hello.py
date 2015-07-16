import os
import uuid
import redis
import urlparse
import json
import socket

from flask import Flask
from flask import request
from flask import jsonify
from flask import request
from flask import jsonify

app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"
counterK = 0
COLOR = BLUE

#REDIS Connection
rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])

#ONE TIME ONLY redis  counter reset
#r.set('connectionsK', '0')

whoamiK = "NO ONE"
ipK = "NO IP  DETECTED"

@app.route('/')
def hello():
        global counterK 
	global connectionsvarK
        global whoareyouK
        global ipK
        ipK = request.user_agent
        counterK = counterK +1
        r.incr ('connectionsK')
        connectionsvarK = r.get('connectionsK')
        whoamiK = socket.gethostname()
        return """
	<html>
	<body bgcolor="{}">

	<center><h1><font color="white">Hi, I'm GUID:<br/>
	{}
        <center><h1><font color="white">Page Hits for this deploy:<br/>
        {}
	</center>
        <center><h1><font color="white">GLOBAL Page Hits:<br/>
        {}
       <center><h2><small><font color="white">My hostname is:<br/>
        {}
      <center><h2><small><font color="white">YOUR Browser is:<br/>
        {}
	</body>
	</html>
	""".format(COLOR,my_uuid, counterK,connectionsvarK,whoamiK,ipK)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
