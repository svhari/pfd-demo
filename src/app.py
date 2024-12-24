from flask import Flask, render_template
import socket
from datetime import datetime
import pytz

app = Flask(__name__)

# Define the timezone you want to use
local_tz = pytz.timezone('Asia/Kolkata')
deploy_time = datetime.now(local_tz).strftime("%Y-%m-%d %H:%M:%S")

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip, deploy_time=deploy_time)
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

