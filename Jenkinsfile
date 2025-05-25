pipeline {
    agent { label "First" }

    stages {
        stage("Execute Shell Commands via Python") {
            steps {
                echo "Running Python Shell Executor"
                sh 'python3 scripts/executor.py'
            }
        }
    }
}