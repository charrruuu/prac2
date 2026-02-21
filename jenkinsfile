pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                echo "Installing dependencies..."
                bat "python -m pip install -r requirements.txt"
            }
        }
        stage("Build & Test") {
            steps {
                echo "Running ML Pipeline..."
                bat "python ml_pipeline.py"
            }
        }
    }
    post {
        success {
            echo "pipeline SUCCESS - Model Validated"
        }
        failure {
            echo "pipeline FAILED - Check logs"
        }
    }
}