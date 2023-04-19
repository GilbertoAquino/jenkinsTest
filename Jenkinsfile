pipeline {
    agent {label "Gilberto_PC"}
    parameters {
      string defaultValue: 'RA1C9', description: 'Rasberry shake station name.', name: 'station'
      string defaultValue: '2022-01-01', description: 'Write the date in format AAAA-MM-DD.', name: 'date'
      string defaultValue: '00:00:00.0', description: 'Write the time in format HH:mm:SS.s', name: 'time'
      string defaultValue: '1h', description: 'Write the duration of the trace.', name: 'duration'
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
                    bat(script: "python C:\\Users\\gilpi\\shake\\download.py --station "+station+" --date "+date+" --time "+time+" --delta "+duration)
                }
            }
        }
    }
}
