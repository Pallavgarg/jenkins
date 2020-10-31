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

    stage('sonarqube') {
      steps {
        sonar-scanner.bat -D"sonar.projectKey=jenkins-pipeline" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=30b3f3338a4d7df78d7648df6ec9a2d703089a07"
      }
    }


  }
}