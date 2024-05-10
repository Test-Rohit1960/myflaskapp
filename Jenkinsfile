pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/yourusername/yourrepository.git'
            }
        }
      stage("Pushing changes to the remote server"){
            steps {
              script {
                  sh """
                  sudo scp -i /root/pla/mysecret app.py root@flaskserver:/root
                  sudo ssh -i /root/pla/mysecret root@flaskserver "python3" "/root/app.py" "&"
                  """"
            }
        }
    }
}
