pipeline {
  agent any
  triggers {
        pollSCM('* * * * *')
    }

  stages {

    stage('build') {
      steps {
        sh 'python src/first.py'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest tests/'
      }
    }
  }
}