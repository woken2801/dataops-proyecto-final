pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t dataops-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run --rm \
                -v /var/jenkins_home/workspace/proyecto-final/output:/app/output \
                dataops-app
                '''
            }
        }
    }
}