from flask import Flask, render_template
import socket
from datetime import datetime

app = Flask(__name__)
deploy_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

