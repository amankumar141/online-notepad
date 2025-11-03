pipeline {
    agent any
    stages {
        stage('Clone') {
    steps {
        git branch: 'main', url: 'https://github.com/amankumar141/online-notepad.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
