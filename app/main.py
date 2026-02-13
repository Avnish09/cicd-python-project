from flask import Flask, jsonify
import os
from app.config import config

app = Flask(__name__)

# Load configuration
env = os.getenv('ENVIRONMENT', 'development')
app.config.from_object(config[env])

# Get environment (dev, staging, prod)
ENV = os.getenv('ENVIRONMENT', 'development')

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to CI/CD Pipeline Demo!',
        'environment': ENV,
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'environment': ENV
    }), 200

@app.route('/api/info')
def info():
    return jsonify({
        'project': 'CI/CD Python Flask App',
        'environment': ENV,
        'endpoints': {
            '/': 'Home page',
            '/health': 'Health check',
            '/api/info': 'API information'
        }
    })

if __name__ == '__main__':
    # Run on different ports based on environment
    # Adding this comment to test the things
    port = int(os.getenv('PORT', 5000))
    debug = ENV == 'development'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )