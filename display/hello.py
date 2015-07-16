import os
import uuid
import redis
from flask import Flask
app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"
counterK = 0
COLOR = BLUE

@app.route('/')
def hello():
        global counterK 
	counterK = counterK +1
        return """
	<html>
	<body bgcolor="{}">

	<center><h1><font color="white">Hi, I'm GUID:<br/>
	{}
        <center><h1><font color="white">Page Hits:<br/>
        {}
	</center>

	</body>
	</html>
	""".format(COLOR,my_uuid, counterK)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
