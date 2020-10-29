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
        sh 'cd C:\Users\ADMIN\PycharmProjects\JenkinsDemo\src'
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