from flask import Flask, request, render_template
import socket
import random
from prometheus_client import start_http_server, Counter, Summary

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_count', 'total app http request count',['app_name', 'endpoint'])
RANDOM_COUNT = Counter('app_random_count','increment counter by random value')

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('app_request_processing_seconds',
                       'Time spent processing request')

APP_PORT = 8000
METRICS_PORT = 8001

@app.route("/")
# Decorate function with metric.
@REQUEST_TIME.time()
def index():
    REQUEST_COUNT.labels('prom_python_app', request.path).inc()
    random_val = random.random()*10
    RANDOM_COUNT.inc(random_val)
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=APP_PORT)

    # Start up the server to expose the metrics.
    start_http_server(METRICS_PORT)

     # log the server start
    print("Server started at http://0.0.0.0:%s" % APP_PORT)
    print("Metrics server started at http://0.0.0.0:%s" % METRICS_PORT)
