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
        bat 'python src/first.py'
      }
    }
    stage('test') {
      steps {
        bat 'python -m pytest tests/'
      }
    }
  }
}