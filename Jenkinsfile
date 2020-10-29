pipeline {
  agent { docker { image 'python:3.5.1' } }
  triggers {
        pollSCM('* * * * *')
    }

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