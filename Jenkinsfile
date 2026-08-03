pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flower-mlops .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop flower-mlops || true'
                sh 'docker rm flower-mlops || true'
                sh 'docker run -d --name flower-mlops -p 8000:8000 flower-mlops'
            }
        }

    }
}