pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'capgemini-dockerhub-credentials' 
        DOCKER_HUB_REPO = 'yashpahalwani/flask-docker-app'
        GITHUB_REPO = 'https://github.com/yash8209/CapgeminiExamRepo.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: "${env.GITHUB_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${env.DOCKER_HUB_REPO}")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${env.DOCKER_HUB_CREDENTIALS}", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    dockerImage.push()
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker rmi ${DOCKER_HUB_REPO} || true'
        }
    }
}
