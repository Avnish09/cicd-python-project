# CI/CD Python Flask Application

A demonstration project for learning CI/CD pipeline with Git, GitHub, Jenkins, and AWS.

## Project Overview
- **Language**: Python 3.12
- **Framework**: Flask
- **CI/CD**: Jenkins
- **Deployment**: AWS S3 / EC2
- **Environments**: Dev, Staging, Production

## Local Development

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Application
```bash
python app/main.py
```

### Access Application
After running the application, visit these URLs in your browser:
- **Home**: http://localhost:5000/ - Welcome message and app status
- **Health Check**: http://localhost:5000/health - System health status
- **API Info**: http://localhost:5000/api/info - Available endpoints

## Environments
- **Development**: Port 5000
- **Staging**: Port 5001
- **Production**: Port 5002