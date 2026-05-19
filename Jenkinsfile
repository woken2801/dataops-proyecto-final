pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/TU_USUARIO/proyecto-dataops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t dataops-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm -v $(pwd)/output:/app/output dataops-app'
            }
        }
    }
}
