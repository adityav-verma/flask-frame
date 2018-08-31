pipeline {
    agent { docker { image 'coderadi/flask-frame' } }
    stages {
        stage('build') {
            steps {
                sh 'fab polish:ci'
            }
        },
        stage('test') {
            steps {
                sh 'pytest tests -svv'
            }
        }
    }
}
