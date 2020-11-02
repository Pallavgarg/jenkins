pipeline {
  agent any
  triggers {
        pollSCM('*/15 * * * *')
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
        sh 'pytest tests/'
      }
    }

  }
}