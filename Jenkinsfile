pipeline {
	agent {
		docker {
			image 'python:3.6.5-stretch'
			args '-u dalibor:dalibor'
		}
	}
	stages {
		stage('build') {
			steps {
				sh 'python --version'
			}
		}
	}
}
