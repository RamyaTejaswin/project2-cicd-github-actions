from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Define metrics
REQUEST_COUNT = Counter(
    'app_request_count',
    'Total request count',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Request latency in seconds',
    ['endpoint']
)

@app.route('/')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return '''
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px; background: #f0f4f8;">
            <h1>🚀 Hello from Ramya's DevOps Pipeline!</h1>
            <p>Deployed via GitHub Actions CI/CD</p>
            <p>Monitored with Prometheus + Grafana</p>
            <p style="color: green;">✅ All systems operational</p>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    REQUEST_COUNT.labels(method='GET', endpoint='/health').inc()
    return jsonify({
        "status": "healthy",
        "message": "App is running!",
        "version": "3.0"
    })

@app.route('/metrics')
def metrics():
    REQUEST_COUNT.labels(method='GET', endpoint='/metrics').inc()
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(debug=True)