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

    stage('test') {
      steps {
        sh 'python -m pytest tests/'
      }
    }
  }
}