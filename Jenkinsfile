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
    stage('build && SonarQube analysis') {
            steps {
                withSonarQubeEnv('F:\sonar-scanner-cli-4.5.0.2216-windows\sonar-scanner-4.5.0.2216-windows\bin') {
                    // Optionally use a Maven environment you've configured already
                    withMaven(maven:'Maven 3.5') {
                        sonar-scanner.bat -D"sonar.projectKey=jenkins-pipeline" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=30b3f3338a4d7df78d7648df6ec9a2d703089a07"
                    }
                }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
                }
            }
        }

  }
}