pipeline {
    agent { docker { image 'python:3.6.5-stretch' } }
    stages {
        stage('build') {
            steps {
		sh 'python --version'
            }
        }
    }
}
