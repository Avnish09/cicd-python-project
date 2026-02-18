pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '========================================='
                echo 'STAGE 1: CHECKING OUT CODE FROM GITHUB1'
                echo '========================================='
                checkout scm
                echo '✅ Code checked out successfully!'
                echo "Repository: ${env.GIT_URL}"
                echo "Branch: ${env.GIT_BRANCH}"
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }
        
        stage('Environment Info') {
            steps {
                echo '========================================='
                echo 'STAGE 2: ENVIRONMENT INFORMATION'
                echo '========================================='
                bat '''
                    echo Checking Python version...
                    python --version
                    echo.
                    echo Checking pip version...
                    pip --version
                    echo.
                    echo Current directory:
                    cd
                    echo.
                    echo Files in project:
                    dir
                '''
                echo '✅ Environment check complete!'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo '========================================='
                echo 'STAGE 3: INSTALLING DEPENDENCIES'
                echo '========================================='
                bat '''
                    echo Creating virtual environment...
                    python -m venv venv
                    echo.
                    echo Activating virtual environment...
                    call venv\\Scripts\\activate.bat
                    echo.
                    echo Installing requirements...
                    pip install -r requirements.txt
                    echo.
                    echo Installed packages:
                    pip list
                '''
                echo '✅ Dependencies installed!'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '========================================='
                echo 'STAGE 4: RUNNING TESTS'
                echo '========================================='
                bat '''
                    call venv\\Scripts\\activate.bat
                    echo Installing pytest...
                    pip install pytest
                    echo.
                    echo Running tests...
                    python -m pytest tests/ -v --tb=short
                '''
                echo '✅ All tests passed!'
            }
        }
        
        stage('Build') {
            steps {
                echo '========================================='
                echo 'STAGE 5: BUILD'
                echo '========================================='
                echo 'Application: CI/CD Python Flask Project'
                echo 'Build Number: ' + env.BUILD_NUMBER
                echo 'Build URL: ' + env.BUILD_URL
                echo '✅ Build complete!'
            }
        }
        
        stage('Deploy Notification') {
            steps {
                echo '========================================='
                echo 'STAGE 6: DEPLOYMENT NOTIFICATION'
                echo '========================================='
                echo '🚀 Ready to deploy!'
                echo 'Environment: Development'
                echo 'Next: Configure AWS deployment'
            }
        }
    }
    
    post {
        success {
            echo ''
            echo '╔════════════════════════════════════════╗'
            echo '║  ✅ PIPELINE COMPLETED SUCCESSFULLY!   ║'
            echo '╚════════════════════════════════════════╝'
            echo ''
            echo 'Build Number: ' + env.BUILD_NUMBER
            echo 'Duration: Completed in ' + currentBuild.durationString
        }
        failure {
            echo ''
            echo '╔════════════════════════════════════════╗'
            echo '║  ❌ PIPELINE FAILED!                   ║'
            echo '╚════════════════════════════════════════╝'
            echo ''
            echo 'Check console output for errors'
        }
        always {
            echo ''
            echo 'Pipeline execution finished.'
            echo 'Timestamp: ' + new Date().toString()
        }
    }
}