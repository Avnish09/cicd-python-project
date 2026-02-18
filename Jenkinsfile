pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '========================================'
                echo 'CHECKOUT CODE FROM GITHUB'
                echo '========================================'
                checkout scm
                echo 'Code checked out successfully'
            }
        }
        
        stage('Environment') {
            steps {
                echo '========================================'
                echo 'ENVIRONMENT CHECK'
                echo '========================================'
                bat 'python --version'
                bat 'pip --version'
                bat 'dir'
            }
        }
        
        stage('Dependencies') {
            steps {
                echo '========================================'
                echo 'INSTALL DEPENDENCIES'
                echo '========================================'
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo '========================================'
                echo 'RUN TESTS'
                echo '========================================'
                bat 'call venv\\Scripts\\activate.bat && pip install pytest && python -m pytest tests/ -v'
            }
        }
        
        stage('Build') {
            steps {
                echo '========================================'
                echo 'BUILD COMPLETE'
                echo '========================================'
                echo "Build Number: ${env.BUILD_NUMBER}"
            }
        }
    }
    
    post {
        success {
            echo 'SUCCESS: Pipeline completed'
        }
        failure {
            echo 'FAILURE: Pipeline failed'
        }
    }
}