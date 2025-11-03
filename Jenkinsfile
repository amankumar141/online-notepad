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
                bat '"C:\\Users\\amanp\\AppData\\Local\\Programs\\Python\\Python313\\pip.exe" install -r requirements.txt' 
            }
        }
        stage('Run App') {
            steps {
                bat '"C:\\Users\\amanp\\AppData\\Local\\Programs\\Python\\Python313\\" app.py'
            }
        }
    }
}
