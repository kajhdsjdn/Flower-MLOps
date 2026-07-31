pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kajhdsjdn/Flower-MLOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flower-mlops .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker stop flower-mlops || exit 0'
                bat 'docker rm flower-mlops || exit 0'
                bat 'docker run -d --name flower-mlops -p 8000:8000 flower-mlops'
            }
        }
    }
}