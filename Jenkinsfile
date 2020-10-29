pipeline {
  agent any
  triggers {
        pollSCM('* * * * *')
    }

  stages {
    stage ("Code pull"){
      steps{
        checkout scm
      }
    }
    stage('build') {
      steps {
        sh 'python3 src/first.py'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest tests/'
      }
    }
  }
}