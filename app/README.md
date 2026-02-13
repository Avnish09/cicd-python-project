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
- Home: http://localhost:5000/
- Health: http://localhost:5000/health
- Info: http://localhost:5000/api/info

## Environments
- **Development**: Port 5000
- **Staging**: Port 5001
- **Production**: Port 5002