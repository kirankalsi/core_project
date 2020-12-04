pipeline{
        agent any
        stages{
            stage('Install Ansible'){
                steps{
                    sh "./scripts/ansible.sh"
                }
            }
            stage('Test'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Build Images'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Push'){
                steps{
                    sh "./scripts/push.sh"
                }
            }
            stage('Deploy'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
}