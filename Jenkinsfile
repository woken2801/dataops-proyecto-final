pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t dataops-app .'
            }
        }

        stage('Create Output Folder') {
            steps {
                sh 'mkdir -p output'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run --rm \
                -v /var/jenkins_home/workspace/proyecto-final/output:/output \
                dataops-app
                '''
            }
        }

        stage('Show Files') {
            steps {
                sh 'ls -lah output'
            }
        }
    }
}