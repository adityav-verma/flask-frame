pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'fab polish:ci'
            }
        }
        stage('test') {
            steps {
                sh 'cp app/configs.py.sample app/configs.py'
                sh 'pytest tests -svv'
            }
        }
    }
}
