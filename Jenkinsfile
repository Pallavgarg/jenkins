pipeline {
  agent { docker { image 'python:3.5.1' } }
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
        sh 'python first.py'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest tests/'
      }
    }
  }
}