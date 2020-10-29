pipeline {
  agent any
  triggers {
        pollSCM('* * * * *')
    }

  stages {

    stage('build') {
      steps {
        'python src/first.py'
      }
    }
    stage('test') {
      steps {
        'python -m pytest tests/'
      }
    }
  }
}