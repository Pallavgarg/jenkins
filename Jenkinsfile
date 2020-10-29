pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python --version'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest tests/'
      }
    }
  }
}