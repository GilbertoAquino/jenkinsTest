pipeline {
    agent {label "Gilberto_PC"}
    parameters {
      choice choices: ['DEVELOPMENT', 'STAGING', 'PRODUCTION'], description: 'Select an environment for deployment', name: 'ENVIRONMENT'
      password defaultValue: '123ABC', description: 'Enter the API key', name: 'API_KEY'
      string defaultValue: 'This is the changelog', description: 'Enter the changelog', name: 'CHANGELOG'
    }
    stages {
        stage('run sh') {
            steps {
                echo "Test how to run a sh file"
                echo "hello world"
                echo "good bye"
            }
        }
        stage('run sh 2') {
            steps {
                echo "Test how to run a sh file"
                echo "hello world"
                script{
                    bat(script: "dir")
                    bat(script: "python C:\\Users\\gilpi\\shake\\download.py")
                }
            }
        }
    }
}
