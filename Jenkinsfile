pipeline {
    agent any
    parameters {
      choice choices: ['DEVELOPMENT', 'STAGING', 'PRODUCTION'], description: 'Select an environment for deployment', name: 'ENVIRONMENT'
      password defaultValue: '123ABC', description: 'Enter the API key', name: 'API_KEY'
      text defaultValue: 'This is the changelog', description: 'Enter the changelog', name: 'CHANGELOG'
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
            }
        }
    }
}
